from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('./model/model.h5')

# Load the dataset
dataset = pd.read_excel('./dataset/stunting_dataset.xlsx')

# Mapping values for categorical columns
sex_mapping = {'F': 0, 'M': 1}
asi_mapping = {'No': 0, 'Yes': 1}

# API endpoint for stunting detection
@app.route('/predict', methods=['POST'])
def predict_stunting():
    # Get data from request
    data = request.json

    # Preprocess the input data
    sex = sex_mapping[data['Sex']]
    age = float(data['Age'])
    birth_weight = float(data['Birth Weight'])
    birth_length = float(data['Birth Length'])
    body_weight = float(data['Body Weight'])
    body_length = float(data['Body Length'])
    asi_eksklusif = asi_mapping[data['ASI Eksklusif']]

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Sex': [sex],
        'Age': [age],
        'Birth Weight': [birth_weight],
        'Birth Length': [birth_length],
        'Body Weight': [body_weight],
        'Body Length': [body_length],
        'ASI Eksklusif': [asi_eksklusif]
    })

    # Perform prediction
    prediction = model.predict(input_data)
    stunting = 'Yes' if prediction[0][0] > 0 else 'No'

    # Return the prediction as JSON response
    response = {'Stunting': stunting}
    return jsonify(response)

if (__name__ == "__main__"):
     app.run(host="0.0.0.0", port = 5000, debug=False)
