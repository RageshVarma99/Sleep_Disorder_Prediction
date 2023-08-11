#pip install streamlit

import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("model.pkl",'rb'))

# Create Streamlit app
st.title("Sleep Disorder Prediction")

# Input widgets in the sidebar
st.sidebar.header("User Input")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
gender_encoded = 0 if gender == "Male" else 1 

age = st.sidebar.slider("Age", 18, 80, 30)

occupation = st.sidebar.selectbox("Occupation", ["Nurse", "Doctor", "Engineer", "Lawyer", "Sales Representative", "Teacher", "Accountant", "Salesperson", "Software Engineer", "Scientist", "Manager"])
occupation_encoded = 0 if occupation == "Accountant" else 1 if occupation == "Doctor" else 2 if occupation == "Engineer" else 3 if occupation == "Lawyer" else 4 if occupation == "Manager" else 5 if occupation == "Nurse" else 6 if occupation == "Sales Representative" else 7 if occupation == "Salesperson" else 8 if occupation == "Scientist" else 9 if occupation == "Software Engineer" else 10

physical_activity = st.sidebar.slider("Physical Activity", 30, 90, 40)

stress_level = st.sidebar.slider("Stress Level", 0, 10, 3)

bmi_category = st.sidebar.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
bmi_category_encoded = 0 if bmi_category == "Normal" else 1 if bmi_category == "Obese" else 2 if bmi_category == "Overweight" else 3

heart_rate = st.sidebar.slider("Heart Rate", 50, 120, 80)

daily_steps = st.sidebar.slider("Daily Steps", 0, 25000, 5000)

systolic_bp = st.sidebar.slider("Systolic BP", 80, 180, 120)

diastolic_bp = st.sidebar.slider("Diastolic BP", 50, 120, 80)

# User clicks the "Predict" button
if st.sidebar.button("Predict"):
    # Prepare the input data for prediction
    input_data = [[gender_encoded, age, occupation_encoded, physical_activity, stress_level,
                   bmi_category_encoded, heart_rate, daily_steps,
                   systolic_bp, diastolic_bp]]  # Replace ... with other input features

    # Create a DataFrame with the input data
    input_df = pd.DataFrame(input_data, columns=['Gender', 'Age', 'Occupation', 'Physical Activity Level',
                                                 'Stress Level', 'BMI Category', 'Heart Rate', 'Daily Steps',
                                                 'Systolic_BP', 'Diastolic_BP'])

    # Make a prediction using the model
    prediction = model.predict(input_df)

    prediction_result = (
            "You are having Insomnia, \n which involves difficulty in falling or staying asleep."
            if prediction == 0
            else "You are having a good Sleep"
            if prediction == 1
            else "You are having Sleep Apnea. Sleep apnea disrupts sleep from a repeated air blockage or a pause in breathing."
        )
    # Display the prediction result
    st.write("Predicted Sleep Disorder:", prediction_result)

# Add additional content if needed
st.write("Created by Ragesh Varma.")
