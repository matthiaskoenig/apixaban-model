"""The definition of the apixaban model on the PBPK library `pkpdsim.pbpk`.

Apixaban is a direct factor Xa inhibitor, bound to albumin in plasma. It is
metabolized by CYP3A4 in the liver into O-demethyl apixaban (M2) and hydroxy
apixaban (M7); M2 is sulfated in the liver into O-demethyl apixaban sulfate
(M1). M1 and M7 reach the plasma and are filtered into the urine, all three
metabolites are excreted into the bile, which reaches the feces. Apixaban
itself is filtered into the urine and secreted from the enterocytes into the
intestinal lumen (P-gp, BCRP). The library builds the whole body, the
segmented intestine with the dose dependent dissolution of the tablet, the
incomplete absorption, the regional absorption of the lower ileum and the
colon (Byon2018) and the efflux of the mucosa, the liver with the metabolism
and the biliary excretion and the kidney with the filtration. The coagulation
model (`model_coagulation.py`) is a PD component which reads the total
apixaban concentration of the arm vein plasma. The model has a male and a
female build (`SEXES`), the studies and groups of mostly women run on the
female build.

The values of the fitted parameters come from the adopted fits
(`MODEL.adopted_fits()`, `models/fits.py`).
"""

from pkpdsim.pbpk import (
    Binding,
    Direction,
    DoseDependentDissolution,
    Excretion,
    FirstOrder,
    Kp,
    Membrane,
    Metabolism,
    Organ,
    PBPKDefinition,
    PDComponent,
    RegionalAbsorption,
    Route,
    SegmentedIntestine,
    Sex,
    Substance,
    Transport,
    U,
    Value,
    Variants,
    fitted,
    ids,
    reference_individual,
)

from pkdb_models.models.apixaban.models import annotations, templates
from pkdb_models.models.apixaban.models.fits import FITS
from pkdb_models.models.apixaban.models.model_coagulation import model_coagulation

#: the fraction unbound of apixaban in plasma (He2011)
FU_API = 0.131

#: the liver of the reference individual of the library (male, ICRP 89) [l]
_VLI_REF = reference_individual(Sex.MALE).volumes[Organ.LIVER]

#: the exchange of the liver per litre of liver [1/min]: 100 l/min of the
#: unbound substance for the whole liver of the reference individual
_KPS_LIVER = 100.0 / _VLI_REF

#: M2 is confined to the liver cells of the library
_M2_TURNOVER = (
    "M2 sits in the liver cells of the library (`LI__Vic`), it has no passive "
    "exchange; its fate is the sulfation into M1 and the biliary excretion."
)


def _liver_exchange(name: str) -> Value:
    """Get the fast exchange of a substance between the liver and its plasma."""
    return Value(
        _KPS_LIVER,
        U.per_min,
        notes=(
            "Fast exchange (not fitted), the role of the instant import and export "
            f"of {name} (`1000/min * Vli`) of the hand-written model: 100 l/min "
            "of the unbound substance for the whole liver of the reference "
            f"individual, per litre of liver 100 l/min / {_VLI_REF:.3g} l = "
            f"{_KPS_LIVER:.3g} 1/min. It "
            "does not limit the hepatic clearance of apixaban: the total clearance "
            "after an iv dose is 52.65 ml/min with it, 52.69 ml/min with 100 times "
            "the exchange (hepatic 23.2 ml/min, 0.1 %); the exchange of the "
            "unbound M1 and M7 is 1150 and 320 times their biliary clearance of the "
            "unbound metabolite (0.087 and 0.31 l/min)."
        ),
    )


def _metabolite(sid: str, name: str, fu_notes: str) -> Substance:
    """Get a metabolite which reaches the plasma: M1 or M7.

    The hand-written model had M1 and M7 in the plasma and in the liver, with
    an instant export on equal total concentrations of liver and plasma, and
    no tissue distribution (`tissue_distribution` was set for apixaban only):
    the metabolite enters only the liver (Kp 1 of the liver of the old model)
    with an exchange of its own. Its fraction unbound is fitted, it is the
    renal clearance relative to the GFR.
    """
    return Substance(
        sid,
        name=name,
        mr={"api_m1": 525.5, "api_m7": 475.5}[sid],
        annotations=annotations.species[sid.removeprefix("api_")],
        binding=Binding(
            fu=fitted(
                FITS.parameter(f"fu_ref_{sid}", unit=U.dimensionless),
                notes=(
                    f"The renal clearance of {name} relative to the GFR (the renal "
                    "clearance of the library is `fu*GFR`); the fraction unbound of "
                    f"{name} is not known, it is part of the fitted value. "
                    f"{fu_notes} Not a binding measurement, so the CKD factor of "
                    "the binding capacity of the plasma proteins does not act on "
                    "this lumped renal factor (`ckd=False`, as for the glimepiride "
                    "metabolites): with it the fraction unbound, and with it the "
                    f"renal and biliary clearance of {name}, rose as the GFR fell."
                ),
            ),
            protein="unknown",
            # a lumped renal factor, not a binding: no CKD factor
            ckd=False,
        ),
        distribution=Kp(
            value=Value(
                1.0,
                U.dimensionless,
                notes=(
                    f"Kp 1 in the liver: the liver holds {name} at the total "
                    "concentration of its plasma, as the export of the old liver "
                    "model on equal concentrations of liver and plasma; no other "
                    "tissue (the old model had no tissue distribution of the "
                    "metabolites)."
                ),
            ),
            organs=frozenset({Organ.LIVER}),
            ps={Organ.LIVER: _liver_exchange(name)},
        ),
        excretion=Excretion(urine=True),
    )


APIXABAN = Substance(
    "api",
    name="apixaban",
    mr=459.5,
    annotations=annotations.species["api"],
    binding=Binding(
        fu=Value(
            FU_API,
            U.dimensionless,
            notes=(
                "Apixaban is 87 % bound to plasma proteins, mainly albumin, the "
                "fraction unbound 13.1 % (He2011). The binding does not change in "
                "renal impairment, so the CKD factor of the binding capacity does "
                "not act on it (`ckd=False`): 'Protein binding was similar "
                "(92%-94%) between healthy controls and ESRD subjects during the "
                "on-dialysis and off-dialysis periods.' (ELIQUIS US prescribing "
                "information, revised 04/2025, 12.3 Pharmacokinetics, Specific "
                "Populations, Hemodialysis in ESRD subjects)."
            ),
        ),
        protein="albumin",
        ckd=False,
    ),
    distribution=Kp(
        value=fitted(
            FITS.parameter("Kp_api", unit=U.dimensionless),
            notes=(
                "The tissue to the total plasma concentration; the volume of "
                "distribution at steady state is about 21 l (Vakkalagadda2016 20.4 "
                "l, Frost2021 21.6 l, ELIQUIS US label)."
            ),
        ),
        ftissue=fitted(
            FITS.parameter("ftissue_api", unit=U.l_per_min),
            notes=(
                "The whole-body exchange of the unbound apixaban, shared over every "
                "tissue by volume; informed by the early phase after an iv dose "
                "(Frost2021, Vakkalagadda2016)."
            ),
        ),
        # per litre of liver (`LI__kps_api`, the organ has `kps*Vli`)
        ps={Organ.LIVER: _liver_exchange("apixaban")},
    ),
    excretion=Excretion(urine=True),
)
"""Apixaban, filtered into the urine and secreted into the intestinal lumen."""

M1 = _metabolite(
    "api_m1",
    "O-demethyl apixaban sulfate (M1)",
    "Informed by the urinary M1 and its plasma concentration (Raghavan2009, "
    "Frost2015b).",
)
"""O-demethyl apixaban sulfate (M1), filtered into the urine and excreted into the bile."""

M7 = _metabolite(
    "api_m7",
    "hydroxy apixaban (M7)",
    "Not identifiable (profile likelihood open on both sides, the estimate "
    "0.00128 near the lower bound 0.001): M7 has urinary and fecal data only "
    "(Raghavan2009), TODO.md.",
)
"""Hydroxy apixaban (M7), filtered into the urine and excreted into the bile."""

M2 = Substance(
    "api_m2",
    name="O-demethyl apixaban (M2)",
    mr=445.5,
    annotations=annotations.species["m2"],
    distribution=None,
)
"""O-demethyl apixaban (M2): formed in the liver cell, sulfated into M1 or
excreted into the bile, no passive exchange (the hand-written model had no M2
in plasma)."""

#: the biliary excretion of M2, fixed at that of M1 (the rule of the fit table
#: for a biliary rate which the profile likelihood shows not identifiable)
_M2EXBI_K = 0.03695055770620532  # 1/min (per litre of liver)


def _biliary_excretion(sid: str, k: Value) -> Transport:
    """Get the excretion of a metabolite into the bile, which reaches the lumen."""
    return Transport(
        f"{sid.removeprefix('api_').upper()}EXBI",
        Organ.LIVER,
        sid,
        Direction.EFFLUX,
        Membrane.APICAL,
        FirstOrder(k=k, per_volume=True),
    )


def _fitted_biliary_excretion(sid: str, name: str) -> Transport:
    """Get the fitted excretion of M1 or M7 into the bile."""
    pid = f"LI__{sid.removeprefix('api_').upper()}EXBI_k"
    return _biliary_excretion(
        sid,
        fitted(
            FITS.parameter(pid, unit=U.per_min),
            notes=(
                f"The excretion of the unbound {name} into the bile per litre of "
                "liver (the library reads the unbound concentration of the cell), "
                "informed by the fecal metabolites (Raghavan2009)."
            ),
        ),
    )


CHEMISTRY = [
    Metabolism(
        "API2M",
        Organ.LIVER,
        "api",
        {"api_m2": 0.78, "api_m7": 0.22},
        FirstOrder(
            k=fitted(
                FITS.parameter("LI__API2M_k", unit=U.per_min),
                notes=(
                    "The metabolism of the unbound apixaban by CYP3A4/5 per litre "
                    "of liver. The fraction 0.78 into M2 (O-demethylation, M2 and "
                    "its products M1, M10, M13), the rest into M7 (hydroxylation): "
                    "about 17-18 % vs 5 % of the dose in the urine and feces "
                    "(Raghavan2009, Table 4)."
                ),
            ),
            per_volume=True,
        ),
        protein="CYP3A4",
    ),
    Metabolism(
        "M22M1",
        Organ.LIVER,
        "api_m2",
        {"api_m1": 1.0},
        FirstOrder(
            k=fitted(
                FITS.parameter("LI__M22M1_k", unit=U.per_min),
                notes=(
                    "The sulfation of M2 into M1 (SULT1A1) per litre of liver. "
                    f"{_M2_TURNOVER}"
                ),
            ),
            per_volume=True,
        ),
        protein="SULT1A1",
    ),
    _fitted_biliary_excretion("api_m1", "M1"),
    _biliary_excretion(
        "api_m2",
        Value(
            _M2EXBI_K,
            U.per_min,
            notes=(
                "Not fitted, the rate of the biliary excretion of M1 per unbound "
                "concentration and litre of liver (`LI__M1EXBI_k` 0.03695 1/min of "
                "a fit with all 15 parameters, cost 105.215, whose record is not "
                "kept): the profile likelihood of `LI__M2EXBI_k` in that fit was "
                "open upwards (95 % CI 0.0111 1/min to its upper bound 0.676), the "
                "rate of M1, the sulfate of M2, lies within it (that of M7, 0.132 "
                "1/min, as well); the fit was repeated with this value "
                "(PK_20261026_144013__f7a78). "
                f"{_M2_TURNOVER}"
            ),
        ),
    ),
    _fitted_biliary_excretion("api_m7", "M7"),
    Transport(
        "APISEC",
        Organ.SMALL_INTESTINE,
        "api",
        Direction.EFFLUX,
        Membrane.APICAL,
        FirstOrder(
            k=fitted(
                FITS.parameter("GU__APISEC_k", unit=U.per_min),
                notes=(
                    "The efflux of the unbound apixaban from the enterocytes into "
                    "the lumen (P-gp, BCRP lumped, `f_abcb1`), per litre of small "
                    "intestine. Apixaban is eliminated unchanged into the gut "
                    "(Frost2021, Wang2014: activated charcoal lowers the AUC); the "
                    "efflux acts on the absorbed apixaban as well."
                ),
            ),
            per_volume=True,
        ),
        protein="ABCB1",
    ),
]
"""The metabolism of apixaban and M2 in the liver, the biliary excretion of the
metabolites and the intestinal efflux of apixaban; no metabolism of the gut wall
(TODO.md)."""


#: the builds of the model: the male and the female reference individual of
#: the library (the studies and groups of mostly women run on the female build)
SEXES: tuple[Sex, ...] = (Sex.MALE, Sex.FEMALE)

#: the regional absorption of apixaban relative to the small intestine: the
#: factor of the lower ileum (`f_ka_ile2_api`) and of the segments of the
#: large intestine (`f_ka_colon_api`), derived with the model from the
#: regional absorption study CV185007 (Byon2018)
REGIONAL_ABSORPTION: dict[str, float] = {"ile2": 0.149, "colon": 0.0567}

#: the notes of the factors of the regional absorption
_REGIONAL_NOTES = (
    "Released by a capsule (Enterion) as a solution of 2.5 mg, apixaban gave an "
    "AUC(0-t) about 60 % lower in the distal small bowel and 84 % lower in the "
    "ascending colon than the oral solution, the relative AUC 0.40 and 0.16 "
    "(Byon2018, abstract; ELIQUIS NDA 202155, Clinical Pharmacology Review, "
    "study CV185007, Reference ID 3088157); the label: 'absorbed throughout the "
    "gastrointestinal tract with the distal small bowel and ascending colon "
    "contributing about 55% of apixaban absorption' (ELIQUIS US prescribing "
    "information, 12.3 Absorption). The distal small bowel is the lower ileum "
    "(`ile2`) of the library, the colon one factor of its segments (caecum to "
    "rectum, the group `colon`). The factors are derived with the model, not "
    "fitted: a solution of 2.5 mg put into the lumen of the lower ileum and of "
    "the colon ascendens gives the AUC of `Carm_api` relative to an oral "
    f"solution of 0.40 and 0.16 with the factors {REGIONAL_ABSORPTION['ile2']} "
    f"(lower ileum) and {REGIONAL_ABSORPTION['colon']} (colon) "
    "(`regional_absorption.py` of the model, which derives them again after a "
    "refit; `test_the_regional_absorption_is_that_of_byon2018` of "
    "`tests/models/test_apixaban.py`), without them 0.99 and 0.93. The "
    "factors depend on the fitted absorption (`ka_api`, `fabs_api`, the efflux "
    "`GU__APISEC_k`), so they and the fit were iterated to a common point: the "
    "factors derived on the adopted fit give the same factors. The colon "
    "factor replaces the fitted `f_ka_colon_api`, which the data of the plasma "
    "did not determine (profile likelihood open towards 0)."
)


def _regional(segment: str) -> Value:
    """Get the factor of the regional absorption of a segment or of the colon."""
    return Value(
        REGIONAL_ABSORPTION[segment],
        U.dimensionless,
        source="Byon2018",
        notes=_REGIONAL_NOTES,
    )


def coagulation_component() -> PDComponent:
    """Get the coagulation model as PD component of the body.

    The model reads the total apixaban concentration of the arm vein plasma
    (`Carm_api`), as the assays measure the total apixaban of the plasma
    sample; it changes no parameter of the body.
    """
    return PDComponent(
        model=model_coagulation,
        inputs={"C_api": "Carm_api"},
        outputs={},
    )


DEFINITION = PBPKDefinition(
    sid="apixaban_body",
    substances=[APIXABAN, M1, M2, M7],
    chemistry=CHEMISTRY,
    variants=Variants(
        organs={
            Organ.SMALL_INTESTINE: SegmentedIntestine(
                ka=fitted(
                    FITS.parameter("ka_api", unit=U.per_hr),
                    notes=(
                        "The absorption of apixaban from every segment, the lower "
                        "ileum and the colon with the factors of the regional "
                        "absorption (Byon2018): a fast onset, an oral solution "
                        "peaks at 0.5 hr (Song2015)."
                    ),
                ),
                fabs=fitted(
                    FITS.parameter("fabs_api", unit=U.dimensionless),
                    notes=(
                        "The fraction of the absorbed flux which enters the body, "
                        "the rest goes into the feces. Apixaban is absorbed "
                        "incompletely with a fast onset: 'Following administration "
                        "of [14C] Apixaban solution, ... ~ 56 % in feces (34% "
                        "unchanged). Factoring in the absolute bioavailability of "
                        "apixaban (F~ 0.5) ...' (ELIQUIS NDA 202155, Clinical "
                        "Pharmacology Review, Reference ID 3232801); the segmented "
                        "intestine gives an incomplete absorption otherwise only "
                        "with a slow ka or the recycling of the efflux through the "
                        "colon: a refit with the full colon absorption had an iv "
                        "half-life of 14.8 hr, with a colon factor alone an F of "
                        "the solution of 0.97 (of the tablet 0.74) and a CL of "
                        "70.6 ml/min."
                    ),
                ),
                regional=RegionalAbsorption(
                    {"ile2": _regional("ile2"), "colon": _regional("colon")}
                ),
            )
        }
    ),
    routes=[
        Route.iv("api"),
        Route.oral(
            "api",
            DoseDependentDissolution(
                k=fitted(
                    FITS.parameter("Ka_dis_api", unit=U.per_hr),
                    notes="The dissolution of a small dose of the tablet.",
                ),
                dose50=fitted(
                    FITS.parameter("D50_dis_api", unit=U.mg),
                    notes=(
                        "The undissolved dose of half the dissolution rate: the "
                        "dissolution saturates with the dose (solubility), the "
                        "exposure is less than dose proportional above 10 mg "
                        "(Frost2013)."
                    ),
                ),
            ),
        ),
        Route.oral_solution("api"),
    ],
    pd=[coagulation_component()],
    # the sums of the fluxes of the segmented intestine: the absorption of
    # apixaban, its efflux into the lumen and its loss to the feces; the gross
    # absorbed fraction of the oral dose
    readouts=(
        ids.absorption_rate("api"),
        ids.efflux_rate("api"),
        ids.feces_rate("api"),
        ids.absorbed_fraction("api"),
    ),
    name="Apixaban body model",
    notes="""
    # Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model apixaban (body model)

    Whole-body physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD)
    model of apixaban, built with the PBPK library `pkpdsim.pbpk`: the
    dissolution of the tablet and the incomplete absorption of apixaban in the
    intestine, its efflux into the intestinal lumen (P-gp, BCRP), the
    distribution into the tissues, the metabolism by CYP3A4 in the liver to
    O-demethyl apixaban (M2), hydroxy apixaban (M7) and O-demethyl apixaban
    sulfate (M1), the renal excretion of apixaban, M1 and M7 and the biliary
    excretion of the metabolites, and the anticoagulant effects (anti-factor Xa
    activity, INR, PT, mPT, aPTT) of the total apixaban concentration of the
    plasma, with the effects of impaired renal and hepatic function, of the
    body weight and of the interactions of CYP3A4 and P-gp.

    """
    + templates.terms_of_use,
    creators=templates.creators,
)
"""The apixaban model."""
