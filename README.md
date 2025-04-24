
# THINGS-Mooney Database

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14040189.svg)](https://doi.org/10.5281/zenodo.14040189)

<img src="/mooney_toolbox/example.gif" alt="Output GIF" width="150"/>

## Overview
The **THINGS-Mooney database** provides a collection of "Mooney-style" distorted images created from the original, license-free [THINGS-plus images](https://osf.io/jum2f/). This repository includes:
- A set of mooney-style images, plus the unambiguous grayscale versions.
- A toolbox that allows you to create your own mooney-style images.
- Subjective identification scores for each Mooney image collected from 947 participants.

## Contents
This repository includes the following components:
- **`stim/`**: Contains the Mooney-transformed stimuli images (`mooney` folder), along with the gray-scale, unambiguous versions of the images (`gray` folder).
- **`mooney_toolbox/`**: A toolbox for generating Mooney images.
- **`gui/`**: A web-based graphical user interface (GUI) to help you create your own dataset by specifying various criteria (e.g., initial semantic distance, identification rates).
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

## Create Your Own Mooney-Style Dataset

### 🔗 **Quick Start: Use the Web Interface**

**[Launch the Dataset Creator](https://things-mooney.onrender.com/)**  
Create your dataset directly in your browser — no coding required.  
Customize criteria like semantic distances and identification rates to generate your own Mooney-style dataset.

---

### ⚙️ Prefer to Run Locally?

If you'd rather use the tool on your own machine, follow these steps:

0. **Install FLASK** (if not already done):
   ```bash
   pip install Flask
   ```

1. **Navigate to the `gui` folder** in your cloned repository

2. **Start the local server** from your terminal:
   ```bash
   python3 app.py
   ```

3. **Open your browser at**:
   ```
   http://127.0.0.1:5000
   ```
You’ll now have access to the same intuitive GUI, locally hosted.

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
