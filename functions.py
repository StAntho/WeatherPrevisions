import pickle
import numpy as np

def temperature_prediction():
    temperature = pickle.load(open("./models/temperature_model.pickle", "rb"))
    return temperature.forecast(7)

def model_classification(temperature, pression, humidite, vent_moyen):
    classif = pickle.load(open("./models/classification_model.pickle", "rb"))
    parameters = np.array([[temperature, pression, humidite, vent_moyen]])

    # Prédiction selon mes données de test
    prediction = classif.predict(parameters)

    # Afficher le résultat de la prédiction
    if prediction[0] == 1:
        show = ["https://giphy.com/embed/W0c3xcZ3F1d0EYYb0f", 480, 400]
        return show   
    
    show = ["https://giphy.com/embed/qhO10687JYjl4CsPyE", 480, 282]
    return show

