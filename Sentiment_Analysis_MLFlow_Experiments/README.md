# Sentiment Analysis - MLFlow Experiments

A machine learning project that uses **MLflow** for experiment tracking and model management, comparing multiple sentiment classification models to identify and register the best performer.

---

## 📌 Project Overview

This project runs sentiment analysis experiments across multiple ML models with different configurations, logging all parameters, metrics, and artifacts using MLflow. It focuses on reproducibility, model comparison, and selecting the optimal model for sentiment classification.

---

## 🎯 Objectives

- Run and track multiple sentiment analysis experiments using MLflow
- Compare model performance across different algorithms
- Perform hyperparameter tuning and log results
- Register the best model in MLflow Model Registry

---

## 📂 Project Structure

```
Sentiment_Analysis_MLFlow_Experiments/
│
├── Sentiment Analysis ML flow.ipynb   # Main notebook
├── data.csv                           # Dataset
├── confusion_matrix.png               # Model evaluation output
├── Screenshot 2026-02-07 202519.png   # MLflow UI screenshot
├── Screenshot 2026-02-07 203350.png   # MLflow UI screenshot
└── Screenshot 2026-02-07 203725.png   # MLflow UI screenshot
```

---

## ⚙️ Workflow

### 1. Import Libraries
- pandas, numpy, scikit-learn, nltk, mlflow, prefect

### 2. Load Dataset
- Loaded Flipkart review dataset with review text and sentiment labels

### 3. EDA (Exploratory Data Analysis)
- Checked dataset shape, data types, missing values, and class distribution

### 4. Text Preprocessing
- Lowercasing, punctuation removal, stopword removal, tokenization

### 5. Train-Test Split
- Split data into training and testing sets

### 6. TF-IDF Feature Extraction
- Converted text into numerical vectors using TF-IDF

### 7. Set MLflow Experiment
- Configured MLflow tracking URI and experiment name

### 8. Train Multiple Models & Log to MLflow
Trained and logged the following models:
- **Logistic Regression**
- **Naive Bayes**
- **Random Forest**
- **Decision Tree**

Each run logs:
- Model parameters
- Accuracy, F1-score, precision, recall
- Confusion matrix artifacts

### 9. Hyperparameter Tuning
- Ran additional experiments with different hyperparameter configurations
- All runs logged to MLflow for comparison

### 10. Final Model Selection & Registration
- Compared all experiment runs in the MLflow UI
- Registered the best-performing model to the MLflow Model Registry

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Libraries | pandas, numpy, scikit-learn, nltk |
| Experiment Tracking | MLflow |
| Pipeline Orchestration | Prefect |
| Text Representation | TF-IDF |
| Dev Tools | Jupyter Notebook |

---

## 🚀 Getting Started

### Install Dependencies
```bash
pip install pandas numpy scikit-learn nltk mlflow prefect
```

### Run the Notebook
```bash
jupyter notebook "Sentiment Analysis ML flow.ipynb"
```

### Launch MLflow UI
```bash
mlflow ui
```
Open `http://localhost:5000` to view and compare all experiment runs.

---

## ✅ Results

- Trained and compared multiple ML models with full experiment tracking
- All runs logged in MLflow with parameters, metrics, and artifacts
- Best model identified and registered in MLflow Model Registry
- Confusion matrix generated for final model evaluation

---

## 🙋‍♂️ Author

**Shaik Muzahid**  
Data Science & Gen AI Intern | Innomatics Research Labs  
[GitHub](https://github.com/muzahidshaik04)

