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
|-------------|--------------------|
|    subject	|    Ticket title    |
|      body	  | Ticket description |
|     queue	  |   Ticket category  |
|    priority	|   Ticket priority  |
|    language	|   Ticket language  |
|      tags	  |   Ticket keywords  |

Only English tickets were used for training.

# 🔄 Workflow

1. Data Preprocessing
   
      - Converted text to lowercase
      - Removed special characters
      - Removed stopwords
      - Applied lemmatization
  
2. Feature Engineering
   
   Converted text into numerical features using TF-IDF Vectorization

4. Model Training
   - Category Classification Model
   - Priority Prediction Model
  
  
4. Model Evaluation
   
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - Confusion Matrix
  
6. Deployment
   
   - Models were saved using Joblib
   - Application deployed using Streamlit
  
## 📊 Model Performance

**Category Classification**

- Algorithm: Logistic Regression
  
- Accuracy: ~51%



**Priority Prediction**

- Algorithm: Logistic Regression

- Accuracy: ~60%


## 📊 Key Insights

- **Technical Support Tickets Were Most Frequent**
  

Technical Support had the highest number of tickets in the dataset, indicating that customers most frequently required assistance with technical issues and system-related problems.



- **Class Imbalance Was Present**


Some categories such as Technical Support and Product Support contained significantly more tickets than categories like Human Resources and General Inquiry. This imbalance affected model performance across classes.


## Live App

https://futureml02-gu6fr64aoepjwqgdtqkg7x.streamlit.app/

## 👨‍💻 Author

Sweta Agarwal

MSc. Statistics Student | Machine Learning Enthusiast
