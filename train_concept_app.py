import streamlit as st
import pandas as pd

# Title
st.title("🧠 Topic & Concept Trainer")

# Sidebar for File Upload
st.sidebar.header("📂 Upload Training Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV or JSON", type=["csv", "json"])

# Initialize Data Storage
if "training_data" not in st.session_state:
    st.session_state.training_data = pd.DataFrame(columns=["Topic", "Concept", "Content"])

# Load Data from File (if uploaded)
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)

    st.session_state.training_data = pd.concat([st.session_state.training_data, df], ignore_index=True)
    st.success("✅ File uploaded successfully!")

# Display Existing Training Data
st.subheader("📊 Current Training Data")
st.dataframe(st.session_state.training_data)

# Manual Data Entry Section
st.subheader("📝 Add Training Data Manually")
topic = st.text_input("Topic")
concept = st.text_input("Concept")
content = st.text_area("Content (text, explanation, etc.)")

if st.button("Add to Training Set"):
    new_data = pd.DataFrame([[topic, concept, content]], columns=["Topic", "Concept", "Content"])
    st.session_state.training_data = pd.concat([st.session_state.training_data, new_data], ignore_index=True)
    st.success("✅ Data added successfully!")

# Info
st.info("ℹ️ You can either upload a file or manually enter data. Both options will be combined.")
