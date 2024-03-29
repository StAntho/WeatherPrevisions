from functions import *
import streamlit as st
import pickle

st.write("## Classification")
temp = st.number_input("Température (en °C)", min_value=-15, max_value=40)

pression = st.number_input("Pression (en hPa)", min_value=1000, max_value=1300)

humid = st.number_input("Humidité (en %)", min_value=0, max_value=100)

vent = st.number_input("Vent (en km/h)", min_value=0, max_value=200)

if temp != "" and pression != "" and humid != "" and vent != "":
    if st.button("Prédire"):
        src, width, height = model_classification(temp, pression, humid, vent)
        st.components.v1.iframe(src, width, height, scrolling=False)
else:
    st.write("Veuillez remplir les champs pour obtenir une prédiction.") 