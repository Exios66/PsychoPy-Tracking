# PsychoPy-Tracking

# Eye Tracking Analysis Pipeline

## Overview
The **Eye Tracking Analysis Pipeline** is a **production-ready** Python package designed for **processing, analyzing, and visualizing** eye-tracking data. This package provides **data preprocessing, fixation & saccade detection, feature extraction, and visualization**, along with **logging, error handling, unit testing, and a CLI tool** for automation.

It is built for **researchers, data scientists, and engineers** working with eye-tracking datasets in psychology, neuroscience, UX/UI research, and human-computer interaction.

---

## Features
- **Data Loading & Preprocessing**: Clean raw eye-tracking datasets by interpolating missing values and smoothing noisy signals.
- **Fixation & Saccade Detection**: Identify eye movement patterns based on velocity thresholds.
- **Feature Extraction**: Compute fixation durations, saccadic amplitudes, and gaze transitions.
- **Visualization**: Generate heatmaps and time-series plots for insightful data analysis.
- **Logging & Error Handling**: Detailed logs and robust error management.
- **CLI & API Support**: Automate processing with a command-line interface or integrate with external applications.
- **Parallel Processing**: Optimize performance when handling large datasets.
- **Continuous Integration & Testing**: Ensures code stability and reliability.

---

## Project Structure

```bash
eye_tracking_analysis/
│── eye_tracking_analysis/   # Main package
│   │── __init__.py
│   │── data_loader.py
│   │── preprocessing.py
│   │── fixation_saccade.py
│   │── feature_extraction.py
│   │── visualization.py
│   │── cli.py  # Command-line interface
│   │── logger.py  # Logging functionality
│   │── api.py  # API for extensibility
│
│── scripts/  # Example scripts for users
│   │── run_analysis.py
│
│── tests/  # Unit tests
│   │── test_preprocessing.py
│   │── test_feature_extraction.py
│   │── test_fixation_saccade.py
│   │── test_api.py
│
│── docs/  # Documentation
│   │── user_guide.md
│   │── developer_guide.md
│
│── setup.py  # Installation script
│── requirements.txt  # Dependencies
│── README.md  # Documentation
│── LICENSE  # Open-source license
│── .gitignore  # Ignore unnecessary files
│── .github/workflows/ci.yml  # Continuous Integration
```

---

## Installation

### **Prerequisites**
Ensure you have **Python 3.7+** installed. Install dependencies using:

```sh
pip install -r requirements.txt
```

### **Installing the Package**
To install the package locally, run:

```sh
git clone https://github.com/YOUR_USERNAME/eye_tracking_analysis.git
cd eye_tracking_analysis
pip install .
```

For development use:

```sh
pip install .[dev]
```

---

## Usage

### **Command-Line Interface (CLI)**
Run the analysis pipeline using the CLI tool:

```sh
eye_tracking_analysis data/eye_tracking.csv
```

### **Python API**
Use the package in a Python script:

```python
from eye_tracking_analysis.api import process_eye_tracking

df = process_eye_tracking("data/eye_tracking.csv")
print(df.head())
```

---

## Logging
Logs are stored in **eye_tracking.log** and provide details on processing status, errors, and warnings.

---

## Continuous Integration
This package includes **GitHub Actions** for automated testing and deployment. The CI pipeline ensures:
- **Unit tests are run on every push and pull request**
- **Code follows best practices and formatting**

---

## Running Tests
To validate the code, run the test suite:

```sh
pytest tests/
```

---

## Contributing
Contributions are welcome! To contribute:
1. **Fork the repository**
2. **Create a feature branch**
3. **Submit a pull request**

Ensure all changes pass tests and follow best coding practices.

---

## License
This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## Contact
For questions or support, contact **your-email@example.com** or create an issue on [GitHub](https://github.com/YOUR_USERNAME/eye_tracking_analysis/issues).

---

## Future Enhancements
- **Real-time Eye Tracking Support**
- **Web Interface for Interactive Analysis**
- **Advanced Machine Learning-based Movement Classification**

Let us know your suggestions and feature requests!

