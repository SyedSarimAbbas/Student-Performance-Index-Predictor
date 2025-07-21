import streamlit as st
import base64
import pickle
# Set background from local image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🔹 Set your background image
add_bg_from_local("Backgorund cover.jpg")

# 🔹 Add custom black text title
st.markdown(
    """
    <div style='
        position: absolute left;
        top: 50%;
        left: 5%;
        transform: translateY(-50%);
    '>
        <h1 style='
            color: white;
            font-family: Arial;
            font-size: 48px;
        '>
             AI Student Performance Index Predictor!
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.write("#### This app predicts your performance index based on the following:")

st.markdown("### 📚 Enter the student's academic details below:")


study_hours = st.number_input("Study Hours Per Day", min_value=0.0, max_value=9.0, step=1.0)
previous_scores = st.number_input("Previous Scores", min_value=0, max_value=100, step=1)
extracurricular = st.selectbox("Participated in Extracurricular Activities?", ["Yes", "No"])
Extracurricular_activities = 1 if extracurricular == "Yes" else 0
sleep_hours = st.number_input("Enter Your Sleep Hours", min_value=0, max_value=24, step=1)
sample_papper_practice=st.number_input("Enter The Number Of Sample Pappers Practiced", min_value=0, max_value=9, step=1)


# Predict button

if st.button("Predict Performance Index"):
    input_data = (study_hours,previous_scores,Extracurricular_activities,sleep_hours,sample_papper_practice)
    prediction = model.predict([input_data])
   
    st.markdown(
        f"""
        <div style='
            background-color: #0b3d0b;
            color: white;
            padding: 14px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 25px;
        '>
            Predicted Performance Index: {prediction[0]:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )