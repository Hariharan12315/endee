import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

st.set_page_config(page_title="Student Performance Predictor")

st.title("🎓 Student Performance Predictor")

st.write("Enter student details to predict final score.")

# Inputs
study_hours = st.slider("Study Hours per Day", 0, 12)
attendance = st.slider("Attendance (%)", 0, 100)
previous_score = st.slider("Previous Score", 0, 100)

# Prediction
if st.button("Predict"):
    input_data = np.array([[study_hours, attendance, previous_score]])
    prediction = model.predict(input_data)

    st.success(f"📊 Predicted Final Score: {prediction[0]:.2f}")

    # Simple feedback
    if prediction[0] >= 75:
        st.info("🔥 Excellent performance expected!")
    elif prediction[0] >= 50:
        st.warning("👍 Average performance. Can improve.")
    else:
        st.error("⚠️ Needs improvement. Increase study time!")
