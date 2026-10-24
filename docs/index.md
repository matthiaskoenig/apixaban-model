# Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of apixaban

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18877904.svg)](https://doi.org/10.5281/zenodo.18877904)
[![Release](https://img.shields.io/github/v/release/matthiaskoenig/apixaban-model)](https://github.com/matthiaskoenig/apixaban-model/releases)
[![Documentation](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/docs.yml/badge.svg)](https://matthiaskoenig.github.io/apixaban-model/)
[![CI](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/ci.yml/badge.svg)](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/docker/v/matthiaskoenig/apixaban?sort=semver&label=docker)](https://hub.docker.com/r/matthiaskoenig/apixaban)
[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-blue)](https://opensource.org/license/MIT)
[![Model license: CC BY-SA 4.0](https://img.shields.io/badge/model%20license-CC%20BY--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-sa/4.0/)

This repository provides the apixaban physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption, the hepatic metabolism by CYP3A4, the renal excretion and the intestinal secretion of apixaban, its metabolites and the anticoagulant effects (anti-factor Xa activity, INR, PT, aPTT).

![model overview](images/apixaban_model.png)

## How to cite

> Myshkina, M., Chang, L., Metternich, J., Badon, S., Babaeva, M., Elias, M. & König, M. (2026). *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of apixaban*. Zenodo. https://doi.org/10.5281/zenodo.18877904

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

## Funding

Matthias König was supported by the Federal Ministry of Research, Technology and Space (BMFTR, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This work was supported by the BMBF-funded de.NBI Cloud within the German Network for Bioinformatics Infrastructure (de.NBI) (031A537B, 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A, 031A532B).

&copy; 2025-2026 Mariia Myshkina, Linh Chang, Johannes Metternich, Shelee Badon, Mariia Babaeva, Michelle Elias and Matthias König
