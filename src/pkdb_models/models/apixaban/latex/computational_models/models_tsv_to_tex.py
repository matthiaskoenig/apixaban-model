"""Module for creating latex table from empagliflozin computational models table."""

import re
from pathlib import Path
import pandas as pd

# Characters that need escaping in LaTeX
LATEX_ESCAPE_MAP = [
    ('\\', r'\textbackslash{}'),
    ('&', r'\&'),
    ('%', r'\%'),
    ('$', r'\$'),
    ('#', r'\#'),
    ('_', r'\_'),
    ('{', r'\{'),
    ('}', r'\}'),
    ('~', r'\textasciitilde{}'),
    ('^', r'\textasciicircum{}'),
]

# Unicode characters replaced with LaTeX math equivalents
UNICODE_REPLACE_MAP = [
    ('≈', r'$\approx$'),
    ('→', r'$\rightarrow$'),
]


def escape_latex(text: str) -> str:
    for char, replacement in UNICODE_REPLACE_MAP:
        text = text.replace(char, replacement)
    for char, replacement in LATEX_ESCAPE_MAP:
        text = text.replace(char, replacement)
    # Restore math snippets that had their $ escaped
    text = text.replace(r'\$\approx\$', r'$\approx$')
    text = text.replace(r'\$\rightarrow\$', r'$\rightarrow$')
    return text


def urls_to_named_hrefs(text: str) -> str:
    named_pattern = re.compile(
        r'(GitHub|Zenodo|PK-DB)\s*:\s*(https?://[^\s,;]+)',
        re.IGNORECASE,
    )

    def replace_named(match):
        label = match.group(1)
        url = match.group(2).rstrip('.,;:)')
        return rf'\href{{{url}}}{{{label}}}'

    text = named_pattern.sub(replace_named, text)

    # Replace any remaining bare URLs
    bare_pattern = re.compile(r'(https?://[^\s,;]+)')

    def replace_bare(match):
        url = match.group(1).rstrip('.,;:)')
        return rf'\href{{{url}}}{{{url}}}'

    text = bare_pattern.sub(replace_bare, text)
    return text


def process_cell(text: str) -> str:
    splitter = re.compile(
        r'((?:GitHub|Zenodo|PK-DB)\s*:?\s*https?://[^\s,;]+|https?://[^\s,;]+)',
        re.IGNORECASE,
    )
    parts = splitter.split(text)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            result.append(escape_latex(part))
        else:
            named = re.match(
                r'(GitHub|Zenodo|PK-DB)\s*:?\s*(https?://[^\s,;]+)',
                part,
                re.IGNORECASE,
            )
            if named:
                label = named.group(1)
                url = named.group(2).rstrip('.,;:)')
                result.append(rf'\href{{{url}}}{{{label}}}')
            else:
                url = part.rstrip('.,;:)')
                result.append(rf'\href{{{url}}}{{{url}}}')
    joined = ''.join(result)
    import re as _re
    joined = _re.sub(
        r'(\\href\{[^}]+\}\{[^}]+\})\s+(\\href\{)',
        r'\1, \2',
        joined,
    )
    return joined


def create_latex_table(df: pd.DataFrame) -> str:
    """Transform DataFrame into LaTeX table."""

    latex_header = r"""
\begin{landscape}
\begin{table}[H]
\centering
\tabcolsep=3pt
\renewcommand{\arraystretch}{1.2}
\tiny
\begin{threeparttable} 
\caption{\scriptsize{\textbf{Summary of published apixaban computational models.} 
Overview of published computational models, including modeling framework, model source and scope, modeling software/platform, whether pharmacokinetics (PK) and/or pharmacodynamics (PD) are modeled,
reproducibility criteria (open access, open software, open model, open code, open data, reproducibility confirmation (Reproducibility), following FAIR criteria, long-term storage, open license), resources, and
apixaban timecourse data sources (Data Sources).}}
\label{tab:computational_models_overview}
\begin{tabularx}{\linewidth}{
    >{\RaggedRight\arraybackslash}m{1.4cm}  % Study
    >{\RaggedRight\arraybackslash}m{0.8cm}  % PubMed ID
    >{\RaggedRight\arraybackslash}m{1.3cm}  % Modeling Framework
    >{\RaggedRight\arraybackslash}m{1.3cm}  % Model Source
    >{\RaggedRight\arraybackslash}m{2.5cm}  % Model Scope
    >{\RaggedRight\arraybackslash}m{1.1cm}  % Platform/Software
    >{\RaggedRight\arraybackslash}m{0.7cm}  % PK
    >{\RaggedRight\arraybackslash}m{0.8cm}  % PD 
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open Access
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open Software
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open Model
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open Code
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open Data
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Reproducibility
    >{\RaggedRight\arraybackslash}m{0.7cm}  % FAIR
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Long-term Storage
    >{\RaggedRight\arraybackslash}m{0.7cm}  % Open License
    >{\RaggedRight\arraybackslash}m{2.1cm}  % Resources
    >{\RaggedRight\arraybackslash}m{2.1cm}  % Data Source
}
\scalebox{0.1}{
\toprule
""".strip('\n')

    column_names = df.columns.tolist()
    header_cells = []
    for col in column_names:
        if col == 'Reproducibility':
            header_cells.append(r'\textbf{Reprodu\-cibility}')
        else:
            header_cells.append(f"\\textbf{{{escape_latex(col)}}}")
    column_headers = " & ".join(header_cells) + r" \\"

    latex_body = f"{column_headers}\n\\midrule\n"

    n_rows = len(df)

    df_columns = df.columns.tolist()
    boolean_columns = detect_boolean_columns(df)

    for row_idx, (_, row) in enumerate(df.iterrows()):
        raw_values = list(row.astype(str).values)

        # Replace 'nan' / empty with empty string
        raw_values = ['' if v in ('nan', 'NaN') else v for v in raw_values]

        # Process each cell: escape LaTeX + convert URLs
        values = [process_cell(v) for v in raw_values]

        is_last_row = (row_idx == n_rows - 1)

        # Column 0 (Study): add \cite (skip for last row)
        cite_key = raw_values[0]
        if not is_last_row:
            values[0] = f"{values[0]} \\cite{{{cite_key}}}"

        # Column 1 (PubMed ID): clickable link — skip for last row
        pmid = raw_values[1].strip().split('.')[0]
        if pmid and pmid not in ('-', '') and not is_last_row:
            values[1] = (
                rf"\href{{https://pubmed.ncbi.nlm.nih.gov/{pmid}/}}{{{pmid}}}"
            )

        # Apply Yes/No cell colouring
        for col_name in boolean_columns:
            col_idx = df_columns.index(col_name)  # Dynamically get the column index
            if col_idx < len(values):  # Ensure index is valid
                val = raw_values[col_idx].strip().capitalize()  # Normalize to match 'True'/'False'
                if val == 'True':
                    values[col_idx] = r'\cellcolor{green!20}\centering\faCheck'
                elif val == 'False':
                    values[col_idx] = r'\cellcolor{red!20}\centering\faTimes'
                elif val == '?':
                    values[col_idx] = r'\centering?'

        if is_last_row:
            latex_body += r"\midrule" + "\n"
        row_str = " & ".join(values) + r" \\"
        latex_body += row_str + "\n"
        latex_body += r"\addlinespace[0.5pt]" + "\n"

    latex_footer = r"""
\bottomrule
}
\end{tabularx}

\end{threeparttable} 
\end{table}
\end{landscape}
""".strip('\n')

    full_latex = latex_header + "\n" + latex_body + latex_footer
    return full_latex

def detect_boolean_columns(df: pd.DataFrame) -> list:
    """
    Detect columns that should apply True/False coloring.
    This function identifies columns where values are True/False or equivalent strings.
    """
    boolean_columns = []
    for col in df.columns:
        unique_values = df[col].dropna().astype(str).str.strip().str.capitalize().unique()
        if set(unique_values).issubset({'True', 'False', 'FALSE', 'TRUE', '?', ''}):
            boolean_columns.append(col)
    return boolean_columns


if __name__ == "__main__":
    tsv_path = Path(__file__).parent / 'computational_models.tsv'
    latex_path = Path(__file__).parent / 'computational_models.tex'

    df = pd.read_csv(tsv_path, sep="\t")
    df = df.fillna("")

    latex_str = create_latex_table(df)

    with open(latex_path, 'w') as f_tex:
        f_tex.write(latex_str)

    print(f"LaTeX table written to: {latex_path}")