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
st.write(dates)

# Prédictions
st.write("## Prédictions") 
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
cols = [col1, col2, col3, col4, col5, col6, col7]
# st.write("<table> <tr> <th>Température</th> <th>Humidité</th> <th>Pression</th> <th>Vent moyen</th> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> <tr> <td>12.0</td> <td>80.0</td> <td>1000.0</td> <td>30.0</td> </tr> </table>", unsafe_allow_html=True)
for index, dates, temperature_prediction, humidite_prediction, pression_prediction, vent_moyen_prediction in zip(index, dates, temperature_prediction(), humidite_prediction(), pression_prediction(), vent_moyen_prediction()):
    with cols[index]:
        st.write(dates)
        st.write(temperature_prediction)
        st.write(index, dates, temperature_prediction, humidite_prediction, pression_prediction, vent_moyen_prediction)
        src, width, height = model_classification(temperature_prediction, pression_prediction, humidite_prediction, vent_moyen_prediction)
        pred = st.components.v1.iframe(src, width, height, scrolling=False)
