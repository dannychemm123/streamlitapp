# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:08:31 2022

@author: HP PROBOOK
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model=pickle.load(open('DesDiabetes_model.sav','rb'))

breast_cancer=pickle.load(open('Breast_Cancer_model.sav','rb'))

parkinsons_model=pickle.load(open('Parkinsons_model.sav','rb'))

#sidebar to navigate

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction Systems",
                           ['Diabetes Prediction',
                           'Breast Cancer Prediction',
                           'Parkinsons Prediction'],
                           
                           icons=['activity','person','person'],
                           
                           default_index=0)
    
if (selected =='Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    #columns for the input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    with col2:
        Glucose  = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood pressure value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    #code for prediction
    
    diabetes_diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,
                                                     SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,
                                                     Age]])
        if (diabetes_prediction[0]==1):
            diabetes_diagnosis='The person is Diabetic'
        else:
            diabetes_diagnosis='The person is not diabetic'
    st.success(diabetes_diagnosis)        
    
    
    
    
    
    
    
if (selected =='Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction using ML')
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        meanradius=st.text_input('mean radius value')
    with col2:
        meantexture=st.text_input('mean texture value')
    with col3:
        meanperimeter=st.text_input('mean perimeter value')
    with col4:
        meanarea=st.text_input('mean area value')
    with col5:
        meansmoothness=st.text_input('mean smoothness value')
    with col1:
        meancompactness=st.text_input('mean compactness value')
    with col2:
        meanconcavity=st.text_input('mean concativity value')
    with col3:
        meanconcavepoints=st.text_input('mean concave points value')
    with col4:
        meansymmetry=st.text_input('mean symmetry')
    with col5:
        meanfractaldimension=st.text_input('mean fractal dimension')
    with col1:
        radiuserror=st.text_input('radius error value')
    with col2:
        textureerror=st.text_input('texture error value')
    with col3:
        perimetererror=st.text_input('perimeter error value')
    with col4:
        areaerror=st.text_input('area error value')
    with col5:
        smoothnesserror=st.text_input('smoothness error value')
    with col1:
        compactnesserror=st.text_input('compactness error value')
    with col2:
        concavityerror=st.text_input('concativity error value')
    with col3:
        concavepointserror=st.text_input('concave pointserror value')
    with col4:
        symmetryerror=st.text_input('symmetry error value')
    with col5:
        fractaldimension =st.text_input('fractal dimension')
    with col1:
        worstradius=st.text_input('worst radius value')
    with col2:
        worsttexture=st.text_input('worst texture value')
    with col3:
        worstperimeter=st.text_input('worst perimeter value')
    with col4:
        worstarea=st.text_input('worst area value')
    with col5:
        worstsmoothness=st.text_input('worst smoothness value')
    with col1:
        worstcompactness=st.text_input('worst compactness value')
    with col2:
        worstconcavity=st.text_input('worst concativity value')
    with col3:
        worstconcavepoints=st.text_input('worst concave points value')
    with col4:
        worstsymmetry=st.text_input('worst symmetry value')
    with col5:
        worstfractaldimension=st.text_input('worst fractal dimension value')
        
    Breast_cancer_diagnosis = ''
     
     # creating a button for prediction
    if st.button('Breast Cancer Result'):
         Breast_cancer_prediction=breast_cancer_model.predict([[meanradius,meantexture,meanperimeter,meanarea,
                                                                meansmoothness,meancompactness,meanconcavity,
                                                                meanconcavepoints,meansymmetry,meanfractaldimension,
                                                                radiuserror,textureerror,perimetererror,areaerror,
                                                                smoothnesserror,compactnesserror,concavityerror,
                                                                concavepointserror,symmetryerror,fractaldimension,
                                                                worstradius,worsttexture,worstperimeter,worstarea,
                                                                worstsmoothness,worstcompactness,worstconcavity,
                                                                worstconcavepoints,worstsymmetry,worstfractaldimension]])
       
       
       
       
       
       
         if (Breast_cancer_prediction[0]==1):
             Breast_cancer_diagnosis='The person has Breast Cancer'
         else:
             Breast_cancer_diagnosis='The person does not have Breast Cancer'
    st.success(Breast_cancer_diagnosis)        
     
        
        
    
    
if (selected =='Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction using ML')
    
    col1,col2,col3,col4,col5=st.columns(5)
     
    with col1:
         Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
         Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
         Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
         Jitter_percent=st.text_input('MDVP:Jitter(%)')
    with col5:
         Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
         RAP=st.text_input('MDVP:RAP')
    with col2:
         PPQ=st.text_input('MDVP:PPQ')
    with col3:
         DDP=st.text_input('Jitter:DDP')
    with col4:
         Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
         Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    with col1:
         Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col2:
         Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col3:
         APQ=st.text_input('MDVP:APQ')
    with col4:
         Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col5:
         NHR=st.text_input('NHR')
    with col1:
         HNR=st.text_input('HNR')
    with col2:
         RPDE=st.text_input('RPDE')
    with col3:
         DFA=st.text_input('DFA')
    with col4:
         spread1=st.text_input('spread1')
    with col5:
         spread2 =st.text_input('spread2')
    with col1:
         D2=st.text_input('D2')
    with col2:
         PPE=st.text_input('PPE')
         
    parkinsons_diagnosis=''
    
    if st.button('Parkisona Test Result'):
       parkinsons_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter_percent,
                                                        Jitter_Abs,RAP,PPQ,DDP,Shimmer,
                                                        Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,
                                                        APQ,Shimmer_DDA,NHR,HNR,RPDE,
                                                        DFA,spread1,spread2,D2,PPE
                                                 
                                                      ]])
       if (parkinsons_prediction[0]==1):
            parkinsons_diagnosis='The person has Parkinson'
       else:
        parkinsons_diagnosis='The person does not have Parkinson'
        
    st.success(parkinsons_diagnosis)
      
        
    

