import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    with open('../model/impact_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit app 
st.title("Performance Impact vs Gaming Habits Perdictor")
st.markdown("Enter your habits to get a **real-time performance impact estimate** based on your gaming hours and other factors.")

st.sidebar.header("Gamer Details")

age = st.sidebar.slider("Age", 18, 35, 18)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
ocupation = st.sidebar.selectbox("Occupation", ["Working Professional", "Student"])
game_type = st.sidebar.selectbox("Type of Games Played", ["Action", "Simulation","Sports", "Puzzle", "Casual", "Strategy"])
daily_gaming_hours = st.sidebar.slider("Daily Gaming Hours", 0, 24, 1)
primary_gameing_time = st.sidebar.selectbox("Primary Gaming Time", ["Morning", "Evening", "Night"])
sleep_hours = st.sidebar.slider("Average Sleep Hours per Night", 0, 24, 7)
stress_level = st.sidebar.slider("Stress Level (1-10)", 1, 10, 5)
focus_level = st.sidebar.slider("Focus Level (1-10)", 1, 10, 5)


# Make prediction
if st.button("Estimate Performance Impact"):
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Occupation': [ocupation],
        'Game_Type': [game_type],
        'Daily_Gaming_Hours': [daily_gaming_hours],
        'Primary_Gaming_Time': [primary_gameing_time],
        'Sleep_Hours': [sleep_hours],
        'Stress_Level': [stress_level],
        'Focus_Level': [focus_level]
    })

    # Predict using the loaded model
    prediction = model.predict(input_data)[0]

    # Get probabilities (confidence) if supported (percentage of trees that voted the same answer)
    probs = model.predict_proba(input_data)
    confidence = np.max(probs) * 100

    # 5. Display Results
    st.subheader("Prediction Result")
    
    if prediction == "Positive":
        st.success(f"🌟 **Positive Impact!** ({confidence:.1f}% confidence)")
        st.write("Your habits appear to be well-balanced. Keep up the good work!")
        
    elif prediction == "Neutral":
        st.info(f"⚖️ **Neutral Impact** ({confidence:.1f}% confidence)")
        st.write("Your gaming habits aren't significantly hurting your performance, but they aren't helping either.")
        
    else: # Negative
        st.error(f"⚠️ **Negative Impact** ({confidence:.1f}% confidence)")
        st.write("Your current routine (likely low sleep + high gaming) may be hurting your scores.")
        
        # Simple advice logic
        if sleep_hours < 6:
            st.warning("💡 **Tip:** Try increasing your sleep to at least 7 hours.")
        if daily_gaming_hours > 4:
            st.warning("💡 **Tip:** Consider reducing daily gaming to under 3 hours.")
