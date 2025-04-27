import streamlit as st
import pandas as pd
import pickle
import time
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Patient Health Monitor", page_icon="🦧", layout="wide")


@st.cache_resource
def load_diabetes_model():
    return pickle.load(open('C:/Users/saura/Desktop/Prediction of disease outbreak/Saved models/diabetes_model.sav','rb'))

@st.cache_resource
def load_heart_disease_model():
    return pickle.load(open('C:/Users/saura/Desktop/Prediction of disease outbreak/Saved models/heart_disease_model.sav','rb'))

@st.cache_resource
def load_parkinsons_model():
    return pickle.load(open('C:/Users/saura/Desktop/Prediction of disease outbreak/Saved models/parkinsons_model.sav','rb'))


diabetes_model = load_diabetes_model()
heart_disease_model = load_heart_disease_model()
parkinsons_model = load_parkinsons_model()


with st.sidebar:
    selected = option_menu('Real-Time Monitoring and Multiple Disease Prediction System',
                           ['Real-Time Monitoring',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['bar-chart', 'activity','heart','person'],
                           default_index=0)


if selected == 'Real-Time Monitoring':
    st.title("📊 Real-Time Patient Monitoring Dashboard")
    excel_file = 'C:/Users/saura/Desktop/Prediction of disease outbreak/patient_data.xlsx'
    refresh_interval = 5  # seconds

    placeholder = st.empty()

    while True:
        with placeholder.container():
            try:
                df = pd.read_excel(excel_file)
                if not df.empty:
                    st.subheader("📈 Latest Readings")
                    st.dataframe(df.tail(10))

                    if not pd.api.types.is_datetime64_any_dtype(df['Timestamp']):
                        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

                    st.line_chart(df.set_index('Timestamp')[['BPM', 'Temperature']])

                else:
                    st.warning("No data yet. Waiting for readings...")

            except Exception as e:
                st.error(f"Failed to load data: {e}")

            time.sleep(refresh_interval)
            st.rerun()


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'

    st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is suffering from Heart disease'
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'

    st.success(heart_diagnosis)


if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'

    st.success(parkinsons_diagnosis)
