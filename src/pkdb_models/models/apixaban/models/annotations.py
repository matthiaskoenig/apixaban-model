"""Annotations of the apixaban models: the model, its compartments and species."""

from pkpdsim.annotations import compartments as shared_compartments
from sbmlutils.metadata import BQB

model: list = [
    # taxonomy
    (BQB.HAS_TAXON, "taxonomy/9606"),  # human
    (BQB.HAS_TAXON, "snomedct/337915000"),  # human
    # modelling approach
    (BQB.HAS_PROPERTY, "mamo/MAMO_0000046"),  # ordinary differential equation model
    # biological process explained by model (GO/NCIT)
    (BQB.HAS_PROPERTY, "NCIT:C61308"),  # apixaban
    (BQB.HAS_PROPERTY, "NCIT:C180619"),  # Direct Oral Anticoagulant
    (BQB.HAS_PROPERTY, "NCIT:C15299"),  # pharmacokinetics
    (BQB.HAS_PROPERTY, "NCIT:C15720"),  # pharmacodynamics
    # model relevance to a particular area
    (BQB.HAS_PROPERTY, "GO:0007596"),  # blood coagulation
    # model reference
    # (BQB.IS_DESCRIBED_BY, "doi/10.20944/preprints202507.1945.v1"),  # preprint
    (BQB.IS_DESCRIBED_BY, "doi/10.5281/zenodo.18877904"),  # apixaban-model
]


species: dict[str, list] = {
    "api": [  # apixaban
        (BQB.IS, "pubchem.compound/10182969"),
        (BQB.IS, "inchikey/QNZCBYKSOIHPEH-UHFFFAOYSA-N"),
        (BQB.IS, "CHEBI:72296"),
        (BQB.IS, "NCIT:C61308"),
        (BQB.IS, "SNOMEDCT:698090000"),
    ],
    "m1": [  # O-Demethyl apixaban sulfate
        (BQB.IS, "pubchem.compound/91667715"),
        (BQB.IS, "inchikey/HRIFVOGTDGFZKP-UHFFFAOYSA-N"),
        (BQB.IS, "CHEBI:760768"),
    ],
    "m2": [  # O-Demethyl apixaban
        (BQB.IS, "pubchem.compound/10203943"),
        (BQB.IS, "inchikey/HGHLWAZFIGRAOT-UHFFFAOYSA-N"),
        (BQB.IS, "CHEBI:760769"),
    ],
    # hydroxy apixaban, one of two isomers whose position of the hydroxylation
    # is not determined (Raghavan2009): a version of apixaban
    "m7": [
        (BQB.IS_VERSION_OF, "pubchem.compound/10182969"),
        (BQB.IS_VERSION_OF, "CHEBI:72296"),
    ],
}


# the shared compartments, the liver with the term of the PBPK ontology
compartments: dict[str, list] = {
    **shared_compartments,
    "li": [
        *shared_compartments["li"],
        (BQB.IS, "https://bioregistry.io/PBPKO:00558"),  # liver compartment
    ],
}
