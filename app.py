from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from io import BytesIO

app = Flask(__name__, static_url_path='/static')

# Load the model
model = load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        # Convert the FileStorage object to a BytesIO object
        file_stream = BytesIO(file.read())
        # Load the image from the BytesIO object
        img = image.load_img(file_stream, target_size=(224, 224))
        # Convert the image to a numpy array
        image_array = image.img_to_array(img)
        # Expand dimensions to match the model's expected input shape
        image_array = np.expand_dims(image_array, axis=0)
        # Make the prediction
        prediction = model.predict(image_array)
        # Convert prediction to label
        # Reverse the logic here: if prediction[0][0] is higher, it's Healthy, else Pneumonia
        label = 'Healthy' if prediction[0][0] > prediction[0][1] else 'Pneumonia'
        # Calculate the confidence score
        confidence_score = max(prediction[0])
        # Return the label and confidence score
        return jsonify({'prediction': label, 'confidence_score': float(confidence_score)})

if __name__ == '__main__':
    app.run(debug=True)
