import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Student Performance Predictor")
st.title("🎓 Student Performance Predictor")
st.markdown("Enter the student details to predict their performance score.")

# Input sliders
study_hours = st.slider("📚 Study Hours per Day", 1.0, 10.0, 6.0, 0.1)
sleep_hours = st.slider("🛌 Sleep Hours per Day", 4.0, 9.0, 7.0, 0.1)
attendance = st.slider("📅 Attendance (%)", 50, 100, 85)
previous_score = st.slider("🧠 Previous Exam Score", 30, 100, 70)

# Predict
if st.button("Predict Performance"):
    input_data = np.array([[study_hours, sleep_hours, attendance, previous_score]])
    result = model.predict(input_data)[0]
    st.success(f"📈 Predicted Performance Score: {result:.2f}/100")
