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

def vent_direction_prediction():
    vent_moyen = pickle.load(open("./models/vent_direction_model.pickle", "rb"))
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
            show = ["https://giphy.com/embed/77di5IQoTBRyGzDxgE", 150, 100]
            # T = 15, Pression = 1200, Humidité = 100, Vent = 100
            return show
        
        show = ["https://giphy.com/embed/W0c3xcZ3F1d0EYYb0f", 150, 125]
            # T = 15, Pression = 1200, Humidité = 100, Vent = 19
        return show   
    
    # il ne pleut pas
    if vent_moyen > 20:
        show = ["https://giphy.com/embed/G5n8sqIOxBqow", 150, 107]
        # T = 15, Pression = 1000, Humidité = 100, Vent = 100
        return show
    
    show = ["https://giphy.com/embed/qhO10687JYjl4CsPyE", 150, 87]
    # T = 15, Pression = 1000, Humidité = 0, Vent = 19
    return show

def degre_vers_direction(degre):
    directions = {
        'nord': range(0, 23),
        'nord': range(338, 360),
        'nord-est': range(23, 68),
        'est': range(68, 113),
        'sud-est': range(113, 158),
        'sud': range(158, 203),
        'sud-ouest': range(203, 248),
        'ouest': range(248, 293),
        'nord-ouest': range(293, 338)
    }
    
    degre_entier = int(round(degre))
    
    for direction, intervalle in directions.items():
        if degre_entier % 360 in intervalle:
            return direction
    
    return "inconnu"
