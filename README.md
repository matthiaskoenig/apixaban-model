[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18877904.svg)](https://doi.org/10.5281/zenodo.18877904)
[![Release](https://img.shields.io/github/v/release/matthiaskoenig/apixaban-model)](https://github.com/matthiaskoenig/apixaban-model/releases)
[![Documentation](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/docs.yml/badge.svg)](https://matthiaskoenig.github.io/apixaban-model/)
[![CI](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/ci.yml/badge.svg)](https://github.com/matthiaskoenig/apixaban-model/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/docker/v/matthiaskoenig/apixaban?sort=semver&label=docker)](https://hub.docker.com/r/matthiaskoenig/apixaban)
[![Python](https://img.shields.io/badge/python-3.14%20%7C%203.15-blue)](https://www.python.org)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-blue)](https://opensource.org/license/MIT)
[![Model license: CC BY-SA 4.0](https://img.shields.io/badge/model%20license-CC%20BY--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-sa/4.0/)

# Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of apixaban

This repository provides the apixaban physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption, the hepatic metabolism by CYP3A4, the renal excretion and the intestinal secretion of apixaban, its metabolites and the anticoagulant effects (anti-factor Xa activity, INR, PT, aPTT).

Documentation: <https://matthiaskoenig.github.io/apixaban-model/>

Credibility of the model for its contexts of use: [https://matthiaskoenig.github.io/apixaban-model/credibility.html](https://matthiaskoenig.github.io/apixaban-model/credibility.html)

## Model

![apixaban_body](models/apixaban_body.svg)

![apixaban_body_body](models/apixaban_body_body.svg)

## Quick start

```bash
git clone https://github.com/matthiaskoenig/apixaban-model.git && cd apixaban-model
uv sync
uv run python -m sbmlsim.run simulate specs/simulate.json --out results/simulate
```

## How to cite

> Myshkina, M., Chang, L., Metternich, J., Badon, S., Babaeva, M., Elias, M. & König, M. (2026). *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of apixaban*. Zenodo. https://doi.org/10.5281/zenodo.18877904

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

&copy; 2025-2026 Mariia Myshkina, Linh Chang, Johannes Metternich, Shelee Badon, Mariia Babaeva, Michelle Elias and Matthias König
