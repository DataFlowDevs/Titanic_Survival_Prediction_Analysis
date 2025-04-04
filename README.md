# Titanic_Survival_Prediction_Analysis
The objective of this project is to build a data processing and machine learning pipeline that  takes raw Titanic passenger data, cleans it, perform EDA, extracts  useful features, trains a predictive model, and evaluates its performance. The pipeline will be  modular, ensuring efficient data handling and reusability.
# 🚢 Titanic Survival Prediction Pipeline

## 📌 Objective

The objective of this project is to build a **modular data processing and machine learning pipeline** that takes **raw Titanic passenger data**, performs **data cleaning**, **exploratory data analysis (EDA)**, **feature extraction**, and **predictive modeling**, and finally **evaluates the model's performance**.  

This pipeline is designed to ensure:
- Efficient handling of raw and processed data
- Clean and reusable code through modularization
- Structured analysis and model evaluation outputs

---

## 🧱 Project Structure


---

## 🧹 Data Cleaning

- Implemented modular cleaning functions in `utils.py`
- Key cleaning steps:
  - Removed exact duplicate rows
  - Handled missing values (`fillna`) based on context (e.g., mean for numerical, mode for categorical)
  - Fixed inconsistencies in columns like `age`, `fare`, `embarked`, and `gender`

---

## 📊 Exploratory Data Analysis (EDA)

Performed insightful EDA using the cleaned dataset:
- Survival rates across different classes and genders
- Age and fare distributions
- Heatmaps and bar plots for categorical and numerical features

Visuals and findings are saved to `datasets/results/`.

---

## 🤖 Machine Learning Pipeline

Planned (or implemented) steps:
- Feature selection and encoding
- Splitting data into training/testing sets
- Training a classifier (e.g., logistic regression, decision tree, etc.)
- Evaluating the model using accuracy, precision, recall, etc.

---

## 🔁 Modularity

Each stage of the pipeline is designed to be **independent and reusable**:
- `utils.py` holds generic, reusable functions (e.g., null handling, data type casting, duplicate removal)
- Processing and analysis scripts import and apply these functions

---

## 📦 Installation

To set up the project locally:

```bash
git clone https://github.com/YourUsername/Titanic_Survival_Prediction_Analysis.git
cd Titanic_Survival_Prediction_Analysis
pip install -r requirements.txt
