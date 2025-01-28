
# THINGS-Mooney Database

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14040189.svg)](https://doi.org/10.5281/zenodo.14040189)

<img src="/mooney_toolbox/example.gif" alt="Output GIF" width="150"/>

## Overview
The **THINGS-Mooney database** provides a collection of "Mooney-style" distorted images created from the original, license-free [THINGS-plus images](https://osf.io/jum2f/). This repository includes:
- A set of mooney-style images, plus the unambiguous grayscale versions.
- A toolbox that allows you to create your own mooney-style images.
- Subjective recognition scores for each Mooney image collected from 947 participants.

## Contents
This repository includes the following components:
- **`stim/`**: Contains the Mooney-transformed stimuli images (`mooney` folder), along with the gray-scale, unambiguous versions of the images (`gray` folder).
- **`mooney_toolbox/`**: A toolbox for generating Mooney images.
- **`gui/`**: A web-based graphical user interface (GUI) to help you create your own dataset by specifying various criteria (e.g., initial semantic distance, recognition rates).
- **`data_checks.py`**: Python script for verifying the integrity of the dataset.
- **`things_mooney.csv`**: Metadata for the stimuli in the Mooney dataset.
- **`LICENSE`**: MIT license for the project.

## Installation
To clone this repository, use the following command:
```bash
git clone https://github.com/wobc/things-mooney.git
```

After cloning the repository, run the **data integrity check** by executing the following in your terminal:
```bash
python data_checks.py
```

This will ensure that the dataset is properly set up.

## Create Your Own Dataset

To create your own dataset using the web-based GUI, follow these steps:

0. **Install FLASK if not already done**:
   ```bash
   pip install Flask
   ```

1. **Navigate to the `gui` folder**:
   Open a terminal and go to the `gui` folder in your cloned repository.

2. **Run the web application**:
   In the terminal, run the following command:
   ```bash
   python3 app.py
   ```
   This will start a local web server.

3. **Access the GUI**:
   Open your preferred web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

4. **Start creating your dataset**:
   Use the web interface to specify various criteria (e.g., semantic distances, recognition rates) and generate your own Mooney-style dataset.

---

## Citation

If you use this dataset in your research, please cite this repository as follows:

Linde-Domingo, J.*, Ortiz-Tudela, J.*, Voeller, J., & González-García, C. (2024). THINGS-Mooney database (v1.0.0). Zenodo. [https://doi.org/10.5281/zenodo.14040189](https://doi.org/10.5281/zenodo.14040189)

_(* denotes equal contribution)_

---

## License
This project is licensed under the MIT License. For details, please see the `LICENSE` file.

## Contact
For further questions or support, please open an issue in this repository or send an email to:
- `lindedomingo at ugr dot es`
- `ortiztudela at ugr dot es`
