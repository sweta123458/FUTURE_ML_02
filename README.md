# 🎫 Customer Support Ticket Classification & Priority Prediction System

## 📌 Project Overview

This project is an NLP-based Customer Support Ticket Classification System developed using Python, Scikit-learn, NLTK, and Streamlit.

The system automatically predicts:

- Ticket Category (Support Queue)
  
- Ticket Priority (High / Medium / Low)

The goal is to help support teams route tickets efficiently and respond faster.

## 🚀 Features

- Text Cleaning & Preprocessing
- Stopword Removal
- Lemmatization
- TF-IDF Vectorization
- Ticket Category Classification
- Priority Prediction
- Interactive Streamlit Web App

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## 📂 Dataset

Customer IT Support Dataset

**Important Columns:**

|     Column	|      Description   |
|---------------|--------------------|
|     subject	|    Ticket title    |
|      body	| Ticket description |
|     queue	|   Ticket category  |
|    priority	|   Ticket priority  |
|    language	|   Ticket language  |
|      tags	|   Ticket keywords  |

Only English tickets were used for training.

## 🔄 Workflow

-  Data Preprocessing

  - Handle missing values
  - Convert text to lowercase
  - Remove special characters
  - Remove stopwords
  - Lemmatize words

- Feature Engineering

Convert text into numerical features using TF-IDF Vectorization.

- Model Training

Two Logistic Regression models were trained:

- *Category Classification Model*


- *Priority Prediction Model*


- Model Evaluation

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

- Deployment

The trained models were saved using Joblib and deployed using Streamlit.

## 📊 Model Performance

- Category Classification

**Algorithm:** Logistic Regression

**Accuracy:** ~51%



- Priority Prediction

**Algorithm:** Logistic Regression

**Accuracy:** ~60%

## 📊 Key Insights

- **Technical Support Tickets Were Most Frequent**

Technical Support had the highest number of tickets in the dataset, indicating that customers most frequently required assistance with technical issues and system-related problems.



- **Class Imbalance Was Present**

Some categories such as Technical Support and Product Support contained significantly more tickets than categories like Human Resources and General Inquiry. This imbalance affected model performance across classes.

## 👨‍💻 Author

Sweta Agarwal

MSc. Statistics Student | Machine Learning Enthusiast
