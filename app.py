import pickle
import threading
import json

from flask import Flask, request
from werkzeug import serving
import numpy as np

# path to the saved .pkl file
path = "lregression.pkl"

# loading the model file
lmodel = pickle.load(open(path, "rb"))

app = Flask(__name__)

# creating a preprocessing function to transform the input from json format
def preprocessing_function(request_data: str) -> np.array:
    """
    Converts the input format from json data to numpy array in order to use for the trained model later on

    Parameters:

    request_data (str): data in json format arriving with request made with json.dumps function

    Returns:

    list transformed into 2D numpy array
    """
    return np.asarray([json.loads(request.data)["inputs"]])

@app.route("/predict", methods=["POST"])
def predict() -> str:
    input_params = preprocessing_function(request.data)
    try:
        prediction = lmodel.predict(input_params)
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 400
    
    return json.dumps({"predicted price": int(prediction[0])})


app.run(debug=True)