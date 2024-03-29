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
st.write(temperature_prediction())    