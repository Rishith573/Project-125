from flask import Flask, jsonify, request
from Classifier import data_prediction

app = Flask(__name__)

@app.route("/predict-alphabet", methods = ["POST"])

def predict_data():
    image = request.files('alphabet')
    prediction = data_prediction(image)
    return jsonify({
        "prediction": prediction
    }), 200

if __name__ == '__main__':
    app.run(debug = True)