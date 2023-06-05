import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
import tensorflow as tf

def label_encoding(sex, age, birth_weight, birth_length, body_weight, body_length, asi_ekslusif):
    # Make dictionary for label encoding
    sex_encoding = {'M': 1, 'F': 0}
    asi_encoding = {'No': 0, 'Yes': 1}
    # Encode asi_ekslusif
    asi_encoded = asi_encoding.get(asi_ekslusif)
    # Encode sex
    sex_encoded = sex_encoding.get(sex)
    return sex_encoded, age, birth_weight, birth_length, body_weight, body_length, asi_encoded

def normalize_data(sex_encoded, age, birth_weight, birth_length, body_weight, body_length, asi_encoded):
    normalization_model = "normalization_model.joblib"
    # Load the saved scaler using joblib
    scaler = joblib.load(normalization_model)
    data = np.array([[sex_encoded, age, birth_weight, birth_length, body_weight, body_length, asi_encoded]])
    # Normalize the data using Joblib
    normalized_data = scaler.transform(data)
    return normalized_data

def predict_stunting(normalize_data):
    # Load the TensorFlow model
    model = "model.h5"
    model = tf.keras.models.load_model(model)
    predictions = model.predict(normalize_data)
    return predictions