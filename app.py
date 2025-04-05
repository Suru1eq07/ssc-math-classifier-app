
import streamlit as st
import pandas as pd
import pickle
from utils import clean_text

st.title("Percentage Question Classifier (Concept-wise)")

st.write("Upload a CSV file of questions and get them sorted by concept using a trained ML model.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "question" not in df.columns:
        st.error("The uploaded file must have a 'question' column.")
    else:
        df['cleaned'] = df['question'].apply(clean_text)

        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        df['predicted_concept'] = model.predict(df['cleaned'])

        st.success("Classification Complete!")
        st.write(df[['question', 'predicted_concept']])

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Result CSV", csv, "sorted_questions.csv", "text/csv")
