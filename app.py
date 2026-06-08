import pandas as pd
import joblib
import re
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')

def load_models():

    category_model = joblib.load("category_model.pkl")

    priority_model = joblib.load("priority_model.pkl")

    vectorizer = joblib.load("vectorizer.pkl")

    return category_model, priority_model, vectorizer


category_model, priority_model, vectorizer = load_models()

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

stop_words.discard('not')
stop_words.discard('no')

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r'[^a-zA-Z\s]','',text)

    words = text.split()

    words = [lemmatizer.lemmatize(word)
              for word in words
              if word not in stop_words]
    return " ".join(words)


def predict_ticket(ticket):

    cleaned = clean_text(ticket)

    vector = vectorizer.transform([cleaned])

    category = category_model.predict(vector)[0]

    priority = priority_model.predict(vector)[0]

    return category, priority


st.title("Customer Support Ticket Classifier")

st.sidebar.header("Sample Tickets")

st.sidebar.info("""
Unable to access my account after password reset.

Invoice shows duplicate payment.

Service outage affecting multiple users.
""")

ticket = st.text_area("Enter Ticket Description")

if st.button("Predict"):

    category, priority = predict_ticket(ticket)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Category",
            category
        )

    with col2:

        if priority == "high":

            st.error(
                f"Priority: {priority}"
            )

        elif priority == "medium":

            st.warning(
                f"Priority: {priority}"
            )

        else:

            st.success(
                f"Priority: {priority}"
            )

df = pd.read_csv("Customer IT Support.csv")

page = st.sidebar.selectbox("Select Page",["Prediction", "Analytics"])

if page == "Analytics":

    st.subheader("Priority Distribution")

    st.bar_chart(df["priority"].value_counts())

    st.subheader("Queue Distribution")

    st.bar_chart(df["queue"].value_counts())