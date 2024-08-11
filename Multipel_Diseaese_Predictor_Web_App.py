# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:27:15 2024

@author: athar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading models

dibeates = pickle.load(open("Dibeates_Prediction.sav",'rb'))
heart = pickle.load(open("Heart_Diseases_Prediction.sav",'rb'))

def dibeates_prediction(input_data):
    ip_data_as_numpy_array = np.asarray(input_data)

    # reshape array as we are predicting for 1 instance
    ip_data_reshape = ip_data_as_numpy_array.reshape(1,-1)

    prediction = dibeates.predict(ip_data_reshape)
    print(prediction)

    if(prediction[0] == 0):
      return "The person has no diabetes"
    else:
      return "The person has diabetes"
  

def Heart_Diseases_prediction(input_data):
    # Convert the input data to float
    try:
        input_data_as_float = [float(i) for i in input_data]
    except ValueError:
        return "Please enter valid numeric values for all inputs."
    
    ip_data_as_numpy_array = np.asarray(input_data_as_float)

    # reshape array as we are predicting for 1 instance
    ip_data_reshape = ip_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    prediction = heart.predict(ip_data_reshape)

    if prediction[0] == 0:
        return "The person has no Heart Diseases"
    else:
        return "The person has Heart Diseases"




#sidebar for naviagation
with st.sidebar:
    selected = option_menu('Multipel Diseases Prediction System',
                           ['Dibeates Prediction','Heart Diseases Prediction'],
                           icons=['heart','activity'],
                           default_index=0)

if (selected=='Dibeates Prediction'):
    st.title('Dibeates Prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BloodPressure of subject')
    with col1:
        SkinThickness = st.text_input('SkinThickness of subject')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI of Subject')
#    with col2:
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
#    with col3:
    Age = st.text_input('Age of Subject')
    
    #code for prediction
    diagnosis = ''
    
    #creating function for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = dibeates_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if (selected=='Heart Diseases Prediction'):
    st.title('Heart Diseases Prediction using ML')
    
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of Subject')
    with col2:
        sex = st.text_input('Enter 1 for Male 0 for Female')
    with col3:
        cp = st.text_input('Enter cp Level')
    with col1:
        trestbps = st.text_input('trestbps of subject')
    with col2:
        chol = st.text_input('chol of subject')
    with col3:
        fbs = st.text_input('fbs Level')
    with col1:
        restecg = st.text_input('restecg of Subject')
    with col2:
        thalach = st.text_input('thalach of Subject')
    with col3:
        exang = st.text_input('exang of Subject')
    with col1:
        oldpeak = st.text_input('oldpeak of Subject')
    with col2:
        slope = st.text_input('slope of Subject')
    with col3:
        ca = st.text_input('ca of Subject')
#    with col1:
    thal = st.text_input('thal of Subject')
    
    #code for prediction
    diagnosis = ''
    
    #creating function for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = Heart_Diseases_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
