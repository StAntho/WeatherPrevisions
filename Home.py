from functions import *
import streamlit as st
import json
import pickle
import datetime

st.set_page_config(page_title="Weather App Prévision", page_icon="🌦️", layout="wide")

# Title
st.title("Weather App Prévision")

# sidebar
st.sidebar.title("Weather App Prévision 🌦️")
st.sidebar.write("Projet Deep Learning, TimeSeries")
st.sidebar.link_button("📄 Lien vers la consigne", "https://meteo.data.gouv.fr/hackathon",)

# Dates
dates = []
index = []
today = '03/29/24'
today = datetime.datetime.strptime(today, "%m/%d/%y")
dates.append(today)
for i in range(7):
    today = today + datetime.timedelta(days=1)
    dates.append(today)
    index.append(i)
# st.write(dates)

# Prédictions
st.write("## Prédictions") 
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
cols = [col1, col2, col3, col4, col5, col6, col7]
for i, (date, temp_pred, humid_pred, press_pred, vent_pred, vent_direction) in enumerate(zip(dates, temperature_prediction(), humidite_prediction(), pression_prediction(), vent_moyen_prediction(), vent_direction_prediction())):
    with cols[i]:
        src, width, height = model_classification(temp_pred, press_pred, humid_pred, vent_pred)
        st.components.v1.iframe(src, width, height, scrolling=False)
        st.markdown(f"#### Date: {date.strftime('%A %d %B %Y')}")
        st.markdown(f"**Température:** {round(temp_pred,2)} °C")
        st.markdown(f"**Humidité:** {round(humid_pred, 2)} %")
        st.markdown(f"**Pression:** {round(press_pred, 2)} hPa")
        st.markdown(f"**Vent:** {round(vent_pred, 2)} km/h")
        st.markdown(f"**Direction:** {degre_vers_direction(vent_direction)}")