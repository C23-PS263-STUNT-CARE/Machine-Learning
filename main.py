from flask import Flask, request, jsonify
import tensorflow as tf
from preprocess import preprocess_data

app = Flask(__name__)

def predict_stunting(normalized_data):
    # Load the TensorFlow model
    model = "./model/model.h5"
    model = tf.keras.models.load_model(model)
    predictions = model.predict(normalized_data)
    return predictions

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sex = data['sex']
    age = data['age']
    birth_weight = data['birth_weight']
    birth_length = data['birth_length']
    body_weight = data['body_weight']
    body_length = data['body_length']
    asi_ekslusif = data['asi_ekslusif']

    normalized_data = preprocess_data(sex, age, birth_weight, birth_length, body_weight, body_length, asi_ekslusif)
    predictions = predict_stunting(normalized_data)
    prediction_value = round(predictions[0][0].item(), 2)

    result = {
        'prediction': prediction_value
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
