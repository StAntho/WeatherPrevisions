import pickle
import numpy as np
import datetime

def temperature_prediction():
    temperature = pickle.load(open("./models/temperature_model.pickle", "rb"))
    return temperature.forecast(7)

def humidite_prediction():
    humidite = pickle.load(open("./models/humidite_model.pickle", "rb"))
    return humidite.forecast(7)

def pression_prediction():
    pression = pickle.load(open("./models/pression_model.pickle", "rb"))
    return pression.forecast(7)

def vent_moyen_prediction():
    vent_moyen = pickle.load(open("./models/vent_moyen_model.pickle", "rb"))
    return vent_moyen.forecast(7)

def model_classification(temperature, pression, humidite, vent_moyen):
    classif = pickle.load(open("./models/classification_model.pickle", "rb"))
    parameters = np.array([[temperature, pression, humidite, vent_moyen]])

    # Prédiction selon mes données de test
    prediction = classif.predict(parameters)

    # Afficher le résultat de la prédiction
    if prediction[0] == 1:
        # il pleut
        if vent_moyen > 20:
            show = ["https://giphy.com/embed/77di5IQoTBRyGzDxgE", 480, 320]
            return show
        
        show = ["https://giphy.com/embed/W0c3xcZ3F1d0EYYb0f", 480, 400]
        return show   
    
    # il ne pleut pas
    if vent_moyen > 20:
        show = ["https://giphy.com/embed/G5n8sqIOxBqow", 480, 337]
        return show
    
    show = ["https://giphy.com/embed/qhO10687JYjl4CsPyE", 480, 282]
    return show
