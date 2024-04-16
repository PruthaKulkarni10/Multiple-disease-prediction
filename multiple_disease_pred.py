# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:28:21 2024

@author: Prutha Kulkarni
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


#loading saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_model = pickle.load(open('heart_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], icons = ['activity', 'heart', 'person'], default_index = 1)
    
if(selected == 'Diabetes Prediction'):
    st.title("Diabetes Prediction using ml")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input('Pregnancies')
        
    with col2:
        glucose = st.number_input('Glucose')
        
    with col3:
        blood_pressure = st.number_input('Blood Pressure')
        
        
    with col1:
        skin_thickness = st.number_input('Skin Thickness')
        
    with col2:
        insulin = st.number_input('Insulin')
        
    with col3:
        bmi = st.number_input('BMI')
        
    with col1:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value')
        
    with col2:
        age = st.number_input('Age')
        
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                      bmi, diabetes_pedigree_function, age]
        
        diab_prediction = diabetes_model.predict([user_input])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Diabetic'
        else:
            diab_diagnosis = 'Non-diabetic'
          
    st.success(diab_diagnosis)

    
if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction using ml")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('CP')
        
        
    with col1:
        trestbps = st.number_input('Trestbps')
        
    with col2:
        chol = st.number_input('Cholestrol')
        
    with col3:
        fbs = st.number_input('FBS')
        
    with col1:
        restecg = st.number_input('Rest ECG')
        
    with col2:
        thalach = st.number_input('Thalach')
        
    with col3:
         exang = st.number_input('Exang')
         
    with col1:
         oldpeak = st.number_input('Oldpeak')
         
    with col2:
         slope = st.number_input('Slope')
         
    with col3:
         ca = st.number_input('CA')
         
    with col1:
         thal = st.number_input('Thal')
        
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                      exang, oldpeak, slope, ca, thal]
        
        heart_prediction = heart_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'Heart disease detected'
        else:
            heart_diagnosis = 'No heart disease detected'
          
    st.success(heart_diagnosis)
    
    
if(selected == 'Parkinsons Prediction'):
    st.title("Parkinsons Prediction using ml")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP1 = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        MDVP2 = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        MDVP3 = st.number_input('MDVP:Flo(Hz)')
        
        
    with col1:
        MDVP4 = st.number_input('MDVP:Jitter(%)')
        
    with col2:
        MDVP5 = st.number_input('MDVP:RAP')
        
    with col3:
        MDVP6 = st.number_input('MDVP:PPQ')
        
    with col1:
        Jitter = st.number_input('Jitter:DDP')
        
    with col2:
        MDVP7 = st.number_input('MDVP:Shimmer')
        
    with col3:
         MDVP8 = st.number_input('MDVP:Shimmer(dB)')
         
    with col1:
         Shimmer1 = st.number_input('Shimmer:APQ3')
         
    with col2:
         Shimmer2 = st.number_input('Shimmer:APQ5')
         
    with col3:
         MDVP9 = st.number_input('MDVP:APQ')
         
    with col1:
         Shimmer3 = st.number_input('Shimmer:DDA')
         
    with col2:
        NHR = st.number_input('NHR')
        
    with col3:
        HNR = st.number_input('HNR')
        
    with col3:
         status = st.number_input('Status')
         
    with col1:
         RPDE = st.number_input('RPDE')
         
    with col2:
         DFA = st.number_input('DFA')
         
    with col3:
         spread1 = st.number_input('Spread1')
         
    with col1:
         spread2 = st.number_input('Spread2')
         
    with col2:
         D2 = st.number_input('D2')
         
    with col3:
         PPE = st.number_input('PPE')
        
    parkinsons_diagnosis = ''
    
    if st.button('Parkinsons Disease Test Result'):
        user_input = [MDVP1, MDVP2, MDVP3, MDVP4,
       MDVP5, MDVP6, Jitter,
       MDVP7, MDVP8, Shimmer1, Shimmer2,
       MDVP9, Shimmer3, NHR, HNR, status, RPDE, DFA,
       spread1, spread2, D2, PPE]
        
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'Parkinsons disease detected'
        else:
            parkinsions_diagnosis = 'Parkinsons disease detected'
          
    st.success(parkinsons_diagnosis)
    