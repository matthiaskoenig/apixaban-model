"""Create the LaTeX table of the studies used for modeling apixaban from its TSV."""

from pathlib import Path

import pandas as pd


def create_latex_table(df: pd.DataFrame) -> str:
    """Transform .tsv into .tex table."""
    latex_header = r"""\begin{landscape}
\begin{table}[H]
\tiny
\centering
\tabcolsep=3.5pt\relax
\caption{\textbf{Summary of studies for modeling.}
Overview of study identifiers, PubMed IDs, PK-DB IDs, route, dosing, co-administered substance,
and subject characteristics, including health status (\apih{H}), renal impairment (\apih{RI}),
hepatic impairment (\apih{HI}), fasting status.
\apih{P} = apixaban plasma, \apih{MP} = apixaban plasma metabolites,
\apih{U} = apixaban urine, \apih{MU} = apixaban urine metabolites,
\apih{F} = apixaban feces, \apih{MF} = apixaban feces metabolites,
\apih{B} = apixaban bile, \apih{MB} = apixaban bile metabolites,
\apih{INR} = International Normalized Ratio, \apih{PT} = prothrombin time, \apih{mPT} = (modified) prothrombin time,
\apih{aPTT} = activated partial thromboplastin, \apih{FXa} = (anti-)FXa activity}
\label{table:curated_data_overview_api}
\rowcolors{2}{white}{gray!8}
\setlength{\arrayrulewidth}{0.6pt}
\begin{tabularx}{\linewidth}{
    >{\raggedright\arraybackslash}m{2.7cm} | % Study
    >{\raggedright\arraybackslash}m{1.4cm}  % PubMed
    >{\raggedright\arraybackslash}m{1.4cm} | % PK-DB ID
    >{\raggedright\arraybackslash}m{0.9cm}  % Route
    >{\raggedright\arraybackslash}m{1.cm}  % Dosing
    >{\centering\arraybackslash}m{1.2cm} | % Dose [mg]
    >{\centering\arraybackslash}m{1.0cm}  % Co-adm.
    >{\centering\arraybackslash}m{0.6cm}  % H
    >{\centering\arraybackslash}m{0.6cm}  % RI
    >{\centering\arraybackslash}m{0.6cm} | % HI
    >{\centering\arraybackslash}m{0.6cm}  % Fast
    >{\centering\arraybackslash}m{0.6cm} | % Fed
    c                                      % P
    c                                      % U
    c                                      % F
    c                                      % B
    c                                      % MP
    c                                      % MU
    c                                      % MF
    c                                     | % MB
    >{\centering\arraybackslash}m{0.6cm}  % INR
    >{\centering\arraybackslash}m{0.6cm}  % PT
    >{\centering\arraybackslash}m{0.6cm}  % mPT
    >{\centering\arraybackslash}m{0.6cm}  % aPTT
    >{\centering\arraybackslash}m{0.6cm}  % FXa
}
\arrayrulecolor{black}\toprule"""

    # Rename columns
    df = df.rename(
        columns={
            "study": "Study",
            "pmid": "PubMed",
            "pkdb": "PK-DB",
            "route": "Route",
            "dosing": "Dosing",
            "dose": "Dose [mg]",
            "Co-administration": "Co-adm.",
            "healthy": "H",
            "renal impairment": "RI",
            "hepatic impairment": "HI",
            "fasted": "Fast",
            "fed": "Fed",
            "api plasma": "P",
            "api urine": "U",
            "api feces": "F",
            "api bile": "B",
            "apimet plasma": "MP",
            "apimet urine": "MU",
            "apimet feces": "MF",
            "apimet bile": "MB",
            "FXa": "FXa",
            "aPTT": "aPTT",
            "mPT": "mPT",
            "PT": "PT",
            "INR": "INR",
        }
    )

    columns_bool = [
        "H",
        "RI",
        "HI",
        "Co-adm.",
        "Fast",
        "Fed",
        "P",
        "U",
        "F",
        "B",
        "MP",
        "MU",
        "MF",
        "MB",
        "INR",
        "PT",
        "mPT",
        "aPTT",
        "FXa",
    ]
    for col in columns_bool:
        df[col] = df[col].apply(
            lambda x: r"\checkmark" if str(x).strip().upper() == "TRUE" else ""
        )

    # Select and order columns for output
    output_columns = [
        "Study",
        "PubMed",
        "PK-DB",
        "Route",
        "Dosing",
        "Dose [mg]",
        "Co-adm.",
        "H",
        "RI",
        "HI",
        "Fast",
        "Fed",
        "P",
        "MP",
        "U",
        "MU",
        "F",
        "MF",
        "B",
        "MB",
        "INR",
        "PT",
        "mPT",
        "aPTT",
        "FXa",
    ]
    df = df[output_columns]

    # Header row
    column_headers = (
        " & ".join([f"\\textbf{{{col}}}" for col in df.columns.tolist()]) + r" \\"
    )
    latex_body = (
        "\n"
        "\\hiderowcolors\n"
        f"{column_headers}\n"
        "\\showrowcolors\n"
        "\\arrayrulecolor{black}\\midrule\n"
    )

    for _, row in df.iterrows():
        values = list(row.astype(str).values)

        # Study -> \cite
        values[0] = f"{values[0]} \\cite{{{values[0]}}}"

        # PubMed -> href
        pmid = values[1].split(".")[0] if "." in values[1] else values[1]
        values[1] = f"\\href{{https://pubmed.ncbi.nlm.nih.gov/{pmid}/}}{{{pmid}}}"

        # PK-DB -> href
        pkdb = values[2]
        values[2] = f"\\href{{https://identifiers.org/pkdb:{pkdb}}}{{{pkdb}}}"

        row_str = (
            " & ".join(
                v.replace("TRUE", r"\checkmark").replace("-", "") for v in values
            )
            + r" \\"
        )

        latex_body += row_str + "\n"

    latex_footer = (
        "\\arrayrulecolor{black}\\bottomrule\n"
        "\\end{tabularx}\n"
        "\\end{table}\n"
        "\\end{landscape}"
    )

    return latex_header + latex_body + latex_footer


if __name__ == "__main__":
    tsv_path = Path(__file__).parent / "studies_for_modeling.tsv"
    latex_path = Path(__file__).parent / "studies_for_modeling.tex"

    columns = [
        "study",
        "pmid",
        "pkdb",
        "route",
        "dosing",
        "dose",
        "Co-adm.",
        "healthy",
        "renal impairment",
        "hepatic impairment",
        "fasted",
        "fed",
        "api plasma",
        "api urine",
        "api feces",
        "api bile",
        "apimet plasma",
        "apimet urine",
        "apimet feces",
        "apimet bile",
        "INR",
        "PT",
        "mPT",
        "aPTT",
        "FXa",
    ]

    df = pd.read_csv(
        tsv_path,
        sep="\t",
        skiprows=1,
        usecols=columns,
        engine="python",
        dtype={"pmid": str},
    )[columns]

    df = df.fillna("")

    latex_str = create_latex_table(df)

    with open(latex_path, "w") as f_tex:
        f_tex.write(latex_str)
