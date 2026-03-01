# Sentiment Analysis of Real-time Flipkart Product Reviews

An end-to-end machine learning project that analyzes Flipkart customer reviews to classify sentiment as **positive** or **negative**, deployed as a real-time web application on **AWS EC2**.

---

## 📌 Project Overview

Online product reviews play a critical role in influencing customer decisions and business strategies. This project builds a complete sentiment analysis system — from data preprocessing and model training to cloud deployment — enabling real-time sentiment prediction for user-entered reviews.

---

## 🎯 Objectives

- Analyze customer review text to understand sentiment
- Clean and preprocess textual data
- Convert text into numerical representations using TF-IDF
- Train and evaluate machine learning models
- Deploy the trained model as a Streamlit web application on AWS EC2

---

## 📂 Project Structure

```
Flipkart_Sentiment_Review_Analysis/
│
├── Sentiment Analysis.ipynb       # Main notebook
├── Sentiment_app.py               # Streamlit web application
├── data.csv                       # Dataset
├── sentiment_model.pkl            # Trained Logistic Regression model
├── tfidf_vectorizer.pkl           # Saved TF-IDF vectorizer
└── Project_Explanation.pdf        # Project documentation
```

---

## 📊 Dataset

The dataset consists of Flipkart product reviews containing:
- **Review text**
- **Sentiment labels** — Positive / Negative

---

## ⚙️ Workflow

### 1. Data Loading & EDA
- Loaded the dataset and checked shape, missing values, and class distribution
- Analyzed the balance between positive and negative reviews

### 2. Data Cleaning & Preprocessing
- Converted text to lowercase
- Removed punctuation, special characters, and stopwords
- Tokenized and normalized the review content

### 3. Feature Engineering
- Used **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text into numerical vectors
- Chosen for its effectiveness and strong performance in text classification

### 4. Model Training
- Trained and compared multiple machine learning models
- **Logistic Regression** was selected as the final model based on best F1-score

### 5. Model Evaluation
- Evaluated using **F1-Score**
- Logistic Regression achieved the best balance between precision and recall

### 6. Web Application
- Built a **Streamlit** web app (`Sentiment_app.py`)
- Users can enter a product review and receive instant sentiment prediction
- App loads the saved `sentiment_model.pkl` and `tfidf_vectorizer.pkl`

### 7. Deployment on AWS EC2
- Launched an AWS EC2 Ubuntu instance
- Installed Python, pip, virtual environment, and Streamlit
- Uploaded model files and app code to the instance
- Configured security groups to allow access on **port 8501**
- Ran the application live on the cloud

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Libraries | pandas, numpy, scikit-learn, nltk, streamlit |
| ML Model | Logistic Regression |
| Text Representation | TF-IDF |
| Cloud Platform | AWS EC2 |
| Dev Tools | Jupyter Notebook, VS Code |

---

## 🚀 Getting Started

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run Sentiment_app.py
```

---

## ✅ Results

- Successfully built an end-to-end sentiment analysis pipeline
- Achieved reliable sentiment predictions using TF-IDF + Logistic Regression
- Deployed a real-time, cloud-hosted web application accessible via browser

---

## 🙋‍♂️ Author

**Shaik Muzahid**  
Data Science & Gen AI Intern | Innomatics Research Labs  
[GitHub](https://github.com/muzahidshaik04)

