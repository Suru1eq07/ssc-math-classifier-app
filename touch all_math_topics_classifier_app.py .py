import streamlit as st
import pandas as pd

# 🔍 Keyword-based concept classifier
def classify_concept(text):
    text = text.lower()
    keywords_map = {
        "percentage": "Percentage",
        "percent": "Percentage",
        "profit": "Profit & Loss",
        "loss": "Profit & Loss",
        "discount": "Profit & Loss",
        "simple interest": "Simple Interest",
        "compound interest": "Compound Interest",
        "ratio": "Ratio & Proportion",
        "proportion": "Ratio & Proportion",
        "average": "Average",
        "time and work": "Time & Work",
        "work": "Time & Work",
        "pipes": "Time & Work",
        "time": "Time, Speed & Distance",
        "speed": "Time, Speed & Distance",
        "distance": "Time, Speed & Distance",
        "train": "Time, Speed & Distance",
        "boat": "Time, Speed & Distance",
        "number": "Number System",
        "divisible": "Number System",
        "lcm": "Number System",
        "hcf": "Number System",
        "mensuration": "Mensuration",
        "area": "Mensuration",
        "volume": "Mensuration",
        "surface area": "Mensuration",
        "geometry": "Geometry",
        "angle": "Geometry",
        "triangle": "Geometry",
        "circle": "Geometry",
        "quadrilateral": "Geometry",
        "algebra": "Algebra",
        "equation": "Algebra",
        "polynomial": "Algebra",
        "trigonometry": "Trigonometry",
        "sine": "Trigonometry",
        "cos": "Trigonometry",
        "tan": "Trigonometry",
        "data": "Data Interpretation",
        "graph": "Data Interpretation",
        "table": "Data Interpretation",
        "bar": "Data Interpretation",
        "mixture": "Mixture & Alligation",
        "alligation": "Mixture & Alligation"
    }

    for keyword, concept in keywords_map.items():
        if keyword in text:
            return concept
    return "Uncategorized"

# 🔵 Title
st.title("🧮 SSC Maths MCQ Concept Classifier")

# 📤 File Upload
st.sidebar.header("📂 Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Upload your MCQs file (CSV)", type=["csv"])

# 💾 Session storage
if "classified_mcqs" not in st.session_state:
    st.session_state.classified_mcqs = pd.DataFrame(columns=["Question", "Concept"])

# 📥 Manual MCQ Entry
st.subheader("✍️ Manually Add MCQ")
manual_question = st.text_area("Type your question:")

if st.button("🔍 Classify Manually Entered Question"):
    concept = classify_concept(manual_question)
    st.success(f"🔖 Concept: {concept}")
    new_row = pd.DataFrame([[manual_question, concept]], columns=["Question", "Concept"])
    st.session_state.classified_mcqs = pd.concat([st.session_state.classified_mcqs, new_row], ignore_index=True)

# 📁 Process Uploaded File
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "Question" not in df.columns:
        st.error("❌ The uploaded CSV must have a 'Question' column.")
    else:
        df["Concept"] = df["Question"].apply(classify_concept)
        st.session_state.classified_mcqs = pd.concat([st.session_state.classified_mcqs, df], ignore_index=True)
        st.success("✅ MCQs classified successfully!")

# 📊 Show Results
if not st.session_state.classified_mcqs.empty:
    st.subheader("📋 Classified Questions")
    st.dataframe(st.session_state.classified_mcqs, use_container_width=True)

    # ⬇️ Download CSV
    csv = st.session_state.classified_mcqs.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="ssc_maths_classified_mcqs.csv",
        mime='text/csv'
    )

# ℹ️ Info
st.info("📌 This app classifies SSC Maths questions into topics based on keywords. It's ideal for educators and content creators.")
