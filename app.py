import streamlit as st
import pickle
import os 
from streamlit_option_menu import option_menu 


st.set_page_config(page_title="Multiple Disease Prediction",layout="wide",page_icon="👩‍⚕️")



Diabetes_model=pickle.load(open(r"C:\Users\Admin\Desktop\AI\Project Streamlit (ML)\saved_models\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"C:\Users\Admin\Desktop\AI\Project Streamlit (ML)\saved_models\heart_disease_model.sav",'rb'))



with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                            
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
if selected=="Diabetes Prediction":
    st.title("Diabetes Prediction Using Machine Learning")

    col1,col2,col3=st.columns(3)

    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    
    with col2:
        Glucose=st.text_input("Glucose Level")

    with col3:
        BloodPressure=st.text_input("BloodPressure Value")

    with col1:
        SkinThickness = st.text_input("SkinThickness Value")

    with col2:
        Insulin = st.text_input("Insulin Value")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")

    with col2:
        Age = st.text_input("Age")
    
    Diabetes_Result=""
    if st.button("Diabetes Test Result"):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float (x) for x in user_input]
        prediction=Diabetes_model.predict([user_input])

        if prediction[0]==1:
            Diabetes_Result="The Person has diabetics"
        
        else:
            Diabetes_Result="The Person has no diabetics"

    st.success(Diabetes_Result)


if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction Using Machine Learning")

    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input("Age")

    with col2:
        sex=st.text_input("Sex")

    with col3:
        cp=st.text_input("Chest Pain types")
    
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
    
    with col2:
        chol=st.text_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg=st.text_input("Resting Electrocardiographic results")

    with col2:
        thalach=st.text_input("Maximum Heart Rate achieved")

    with col3:
        exang=st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak=st.text_input("ST depression induced by exercise")

    with col2:
        slope=st.text_input("Slope of the peak exercise ST segment")

    with col3:
        ca=st.text_input("Major vessels colored by flourosopy")

    with col1:
        thal=st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    heart_Result=""
    if st.button("Heart Test Result"):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float (x) for x in user_input]
        prediction=heart_model.predict([user_input])

        if prediction[0]==1:
            heart_Result="The person is having heart disease"
        
        else:
            heart_Result="The person does not have any heart disease"

    st.success(heart_Result)
    








