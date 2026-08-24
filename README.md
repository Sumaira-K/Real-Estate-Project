# Real Estate Price Predictor 

An end-to-end machine learning project that predicts real estate prices based on property-related features. The project covers data analysis, preprocessing, model training, evaluation, model persistence, and deployment through an interactive Streamlit web application.

## Overview

The **Real Estate Price Predictor** demonstrates the complete workflow of taking a machine learning model from development in a Jupyter Notebook to an interactive web application.

The project includes:

* Exploratory Data Analysis (EDA)
* Data preprocessing
* Feature preparation
* Machine learning model training
* Model evaluation
* Model serialization using Joblib
* Interactive prediction using Streamlit
* Multi-page Streamlit application
* Git and GitHub version control
* Deployment of the machine learning application

## Features

### Property Price Prediction

Users can provide the required property-related inputs through the Streamlit interface and receive a predicted property price.

### Model Information

The application includes a dedicated page containing information about the machine learning model used in the project.

### Multi-Page Application

The Streamlit application is organized into separate pages for:

* Prediction
* Model information
* About the project

### Saved Machine Learning Model

The trained model is stored as a Joblib file and loaded by the Streamlit application for making predictions.

## Machine Learning Workflow

The project follows the standard machine learning workflow:

```text
Dataset
   ↓
Data Exploration
   ↓
Data Preprocessing
   ↓
Feature Preparation
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Streamlit Application
   ↓
Price Prediction
```

## Dataset

The project uses a real estate dataset containing property-related features and a target variable representing property prices.

The dataset is explored and prepared before being used for model training.

The analysis includes:

* Dataset inspection
* Statistical analysis
* Exploratory Data Analysis
* Data visualization
* Feature preparation
* Train-test splitting

## Machine Learning Model

A supervised machine learning approach is used to predict property prices.

The trained model is saved using Joblib:

```text
RealEstate.joblib
```

The Streamlit application loads this saved model and uses it to generate predictions based on the user's input.

## Tech Stack

### Programming Language

* Python

### Data Science and Machine Learning

* NumPy
* Pandas
* Scikit-learn
* Joblib

### Data Visualization

* Matplotlib
* Seaborn

### Application Development

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

## Project Structure

```text
Real-Estate-Project/
│
├── app.py
│
├── pages/
│   ├── 1_🏠_Predict.py
│   ├── 2_📊_Model.py
│   └── 3_ℹ️_About.py
│
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
| `RealEstate.joblib`     | Saved trained machine learning model                   |
| `house_all.csv`         | Dataset used for the project                           |
| `requirements.txt`      | Python dependencies required to run the project        |

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

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Exploring the Machine Learning Workflow

The complete machine learning development process can be explored through:

```text
Real_Estate.ipynb
```

The notebook contains the data analysis, preprocessing, model development, and evaluation workflow.

The saved model can also be explored through:

```text
Model_Usage.ipynb
```

## Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment workflow:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Select Repository
       ↓
Select app.py
       ↓
Deploy
```

### Live Application

**Live Demo:** Yet to deploy

## Disclaimer

The predicted property price is an estimate generated by a machine learning model. It should not be considered a professional property valuation, financial recommendation, or guaranteed market price.

Actual property prices can vary depending on factors such as location, market conditions, property condition, amenities, demand, and other variables represented or not represented in the dataset.

## Future Improvements

Potential improvements to the project include:

* Experimenting with additional machine learning algorithms
* Hyperparameter tuning
* Comparing model performance
* Improving prediction accuracy
* Adding additional property features
* Improving the user interface
* Adding more detailed visualizations
* Using a larger and more diverse dataset
* Adding automated testing

## Author

**Sumaira K**

B.Tech Computer Science Engineering Student

GitHub: https://github.com/Sumaira-K

## License

This project is created for educational and portfolio purposes.
