# Real Estate Price Predictor

An end-to-end machine learning application that predicts real estate prices using property and socioeconomic features. The project demonstrates the complete machine learning workflow, from exploratory data analysis and model development to model serialization and deployment as an interactive Streamlit web application.

**Live Demo:** https://realestate-predictor.streamlit.app/

**Repository:** https://github.com/Sumaira-K/Real-Estate-Project

---

## Overview

The Real Estate Price Predictor demonstrates how a machine learning model can be developed, evaluated, serialized, and deployed as an interactive web application.

The project covers:

* Exploratory Data Analysis (EDA)
* Data preprocessing and feature preparation
* Train-test splitting
* Machine learning model training
* Model evaluation
* Model serialization using Joblib
* Interactive prediction using Streamlit
* Multi-page Streamlit application development
* Git and GitHub version control
* Cloud deployment using Streamlit Community Cloud

---

## Features

### Property Price Prediction

Users can provide property-related and socioeconomic inputs through the web interface and receive an estimated property price.

### Model Information

A dedicated page provides information about the machine learning model used for prediction.

### Multi-Page Application

The Streamlit application is organized into three pages:

* Prediction
* Model Information
* About the Project

### Model Persistence

The trained machine learning model is serialized using Joblib and stored as:

```text
RealEstate.joblib
```

The deployed application loads the saved model to generate predictions without retraining the model.

### Web Deployment

The application is deployed using Streamlit Community Cloud and is publicly accessible through the live demo.

---

## Machine Learning Workflow

```text
Dataset
   |
   v
Data Exploration
   |
   v
Exploratory Data Analysis
   |
   v
Data Preprocessing
   |
   v
Feature Preparation
   |
   v
Train-Test Split
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
Model Serialization
   |
   v
Streamlit Application
   |
   v
Interactive Price Prediction
   |
   v
Cloud Deployment
```

---

## Dataset

The project uses a real estate dataset containing property-related and socioeconomic features along with a target variable representing property prices.

The dataset is analyzed and prepared before being used for model training.

### Features

| Feature   | Description                                          |
| --------- | ---------------------------------------------------- |
| `CRIM`    | Per-capita crime rate                                |
| `ZN`      | Proportion of residential land zoned for large lots  |
| `INDUS`   | Proportion of non-retail business acres              |
| `CHAS`    | Charles River location indicator                     |
| `NOX`     | Nitric oxide concentration                           |
| `RM`      | Average number of rooms per dwelling                 |
| `AGE`     | Proportion of owner-occupied homes built before 1940 |
| `DIS`     | Weighted distance to employment centres              |
| `RAD`     | Accessibility to radial highways                     |
| `TAX`     | Property tax rate                                    |
| `PTRATIO` | Pupil-teacher ratio                                  |
| `B`       | Population-related index                             |
| `LSTAT`   | Percentage of lower-status population                |

### Data Analysis

The exploratory analysis includes:

* Dataset inspection
* Descriptive statistics
* Feature analysis
* Distribution analysis
* Data visualization
* Feature preparation
* Train-test splitting

---

## Machine Learning Model

The project uses a supervised machine learning approach for regression-based property price prediction.

### Model

**Random Forest Regression**

The Random Forest Regression model is trained using the selected property and socioeconomic features.

The trained model is serialized using Joblib:

```text
RealEstate.joblib
```

The Streamlit application loads this saved model and uses it to generate predictions based on user-provided inputs.

---

## Model Evaluation

The model is evaluated using standard regression metrics on the test dataset.

The evaluation process includes metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

The complete model development and evaluation process is available in:

```text
Real_Estate.ipynb
```

---

## Technology Stack

| Category             | Technologies              |
| -------------------- | ------------------------- |
| Programming Language | Python                    |
| Data Analysis        | Pandas, NumPy             |
| Machine Learning     | Scikit-learn              |
| Data Visualization   | Matplotlib, Seaborn       |
| Model Persistence    | Joblib                    |
| Web Application      | Streamlit                 |
| Development          | Jupyter Notebook, VS Code |
| Version Control      | Git, GitHub               |
| Deployment           | Streamlit Community Cloud |

---

## Project Structure

```text
Real-Estate-Project/
|
├── app.py
|
├── pages/
│   ├── 1_🏠_Predict.py
│   ├── 2_📊_Model.py
│   └── 3_ℹ️_About.py
|
├── Real_Estate.ipynb
├── Model_Usage.ipynb
├── RealEstate.joblib
├── house_all.csv
├── requirements.txt
└── README.md
```

### File Description

| File / Directory        | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| `app.py`                | Main entry point of the Streamlit application          |
| `pages/1_🏠_Predict.py` | Interface for generating property price predictions    |
| `pages/2_📊_Model.py`   | Displays information about the machine learning model  |
| `pages/3_ℹ️_About.py`   | Provides information about the project                 |
| `Real_Estate.ipynb`     | Main notebook containing the machine learning workflow |
| `Model_Usage.ipynb`     | Notebook demonstrating model usage                     |
| `RealEstate.joblib`     | Serialized trained machine learning model              |
| `house_all.csv`         | Dataset used for the project                           |
| `requirements.txt`      | Python dependencies required to run the application    |
| `README.md`             | Project documentation                                  |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sumaira-K/Real-Estate-Project.git
```

### 2. Navigate to the Project Directory

```bash
cd Real-Estate-Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the default web browser.

The deployed application can also be accessed at:

**https://realestate-predictor.streamlit.app/**

---

## Exploring the Machine Learning Workflow

The complete machine learning workflow is available in:

```text
Real_Estate.ipynb
```

The notebook covers:

* Data exploration
* Exploratory data analysis
* Data preprocessing
* Feature preparation
* Model development
* Model evaluation

Model loading and prediction using the serialized model can be explored in:

```text
Model_Usage.ipynb
```

---

## Deployment

The application is deployed using Streamlit Community Cloud.

### Deployment Workflow

```text
GitHub Repository
       |
       v
Streamlit Community Cloud
       |
       v
Repository Selection
       |
       v
app.py
       |
       v
Dependency Installation
       |
       v
Application Deployment
```

### Live Application

**https://realestate-predictor.streamlit.app/**

---

## Future Improvements

Potential improvements include:

* Experimenting with additional regression algorithms
* Hyperparameter tuning
* Comparing multiple machine learning models
* Improving prediction accuracy
* Adding additional property-related features
* Using a larger and more diverse dataset
* Adding more detailed visualizations
* Improving the user interface and user experience
* Implementing automated testing
* Implementing model monitoring
* Adding prediction uncertainty estimates

---

## Disclaimer

The predicted property price is an estimate generated by a machine learning model.

It should not be considered a professional property valuation, financial recommendation, or guaranteed market price.

Actual property prices may vary depending on factors such as location, market conditions, property condition, amenities, demand, economic conditions, and other variables represented or not represented in the dataset.

---

## Author

**Sumaira K**

B.Tech Computer Science Engineering Student

* GitHub: https://github.com/Sumaira-K
* Project Repository: https://github.com/Sumaira-K/Real-Estate-Project
* Live Application: https://realestate-predictor.streamlit.app/

---

## License

This project is created for educational and portfolio purposes.
