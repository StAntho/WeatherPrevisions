from functions import *
import streamlit as st
import json
import pickle

st.set_page_config(page_title="Weather App Prévision", page_icon="🌦️", layout="wide")

# Title
st.title("Weather App Prévision")

# sidebar
st.sidebar.title("Weather App Prévision 🌦️")
st.sidebar.write("Projet Deep Learning, TimeSeries")
st.sidebar.link_button("📄 Lien vers la consigne", "https://meteo.data.gouv.fr/hackathon",)

st.write("## Prédictions")
st.write("Température (en °C)")
temp = st.number_input("Température", min_value=-15, max_value=40)

st.write("Pression (en hPa)")
pression = st.number_input("Pression", min_value=1000, max_value=1200)

st.write("Humidité (en %)")
humid = st.number_input("Humidité", min_value=0, max_value=100)

st.write("Vent (en km/h)")
vent = st.number_input("Vent", min_value=0, max_value=150)

if temp != "" and pression != "" and humid != "" and vent != "":
    if st.button("Prédire"):
        src, width, height = model_classification(temp, pression, humid, vent)
        st.components.v1.iframe(src, width, height, scrolling=False)
else:
    st.write("Veuillez remplir les champs pour obtenir une prédiction.")        