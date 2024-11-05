

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14040189.svg)](https://doi.org/10.5281/zenodo.14040189)


# THINGS-Mooney Database

## Overview
The THINGS-Mooney database provides a set of "mooney-style" distorted images (created from the original license-free [THINGS-plus images](https://osf.io/jum2f/)). Additionally, this repository contains a toolbox to create your own mooney-style images, plus subjective recognition scores for each mooney image collected on a large sample of participants (n = 947).

## Contents
- `stim/`: Contains the Mooney-transformed stimuli images ("mooney" folder) plus the gray-scale, unambiguous version of each image ("gray" folder).
- `mooney_toolbox/`: Toolbox for creating Mooney images.
- `data_checks.py`: Python script for performing data integrity checks on the dataset.
- `things_mooney.csv`: Metadata for the stimuli in the Mooney dataset.
- `LICENSE`: MIT license file.

## Installation
To clone this repository, use:
```bash
git clone https://github.com/wobc/things-mooney.git
```

After cloning the repository, check data integrity by running `python data_checks.py` in a terminal.

## Citation

If you use this dataset in your research, please cite this repository as follows:

Linde-Domingo, J.\*, Ortiz-Tudela, J.\*, Voeller, J., & González-García, C. (2024). THINGS-Mooney database (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.14040189

_(* denotes equal contribution)_



## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For further questions or support, please open an issue in this repository or send an email to `lindedomingo at ugr dot es` or `ortiztudela at ugr dot es`.


