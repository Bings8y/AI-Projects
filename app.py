from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = 'model.h5'

# Load the trained model (you'll need to add your model.h5 file)
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully!")
except:
    print("Warning: model.h5 not found. Please add your trained model file.")
    model = None

def grayscale(img):
    """Convert image to grayscale"""
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    """Enhance image contrast using histogram equalization"""
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    """Complete image preprocessing pipeline"""
    img = grayscale(img)      # Convert to grayscale
    img = equalize(img)       # Enhance contrast
    img = img/255            # Normalize pixel values (0-1)
    return img

def getClassName(classNo):
    """Map class numbers to traffic sign names with speed conversions"""
    if classNo == 0: return 'Speed limit (20km/h / 12mph)'
    elif classNo == 1: return 'Speed limit (30km/h / 19mph)'
    elif classNo == 2: return 'Speed limit (50km/h / 31mph)'
    elif classNo == 3: return 'Speed limit (60km/h / 37mph)'
    elif classNo == 4: return 'Speed limit (70km/h / 43mph)'
    elif classNo == 5: return 'Speed limit (80km/h / 50mph)'
    elif classNo == 6: return 'End of speed limit (80km/h / 50mph)'
    elif classNo == 7: return 'Speed limit (100km/h / 62mph)'
    elif classNo == 8: return 'Speed limit (120km/h / 75mph)'
    elif classNo == 9: return 'No passing'
    elif classNo == 10: return 'No passing for vehicles over 3.5 metric tons'
    elif classNo == 11: return 'Right-of-way at the next intersection'
    elif classNo == 12: return 'Priority road'
    elif classNo == 13: return 'Yield'
    elif classNo == 14: return 'Stop'
    elif classNo == 15: return 'No vehicles'
    elif classNo == 16: return 'Vehicles over 3.5 metric tons prohibited'
    elif classNo == 17: return 'No entry'
    elif classNo == 18: return 'General caution'
    elif classNo == 19: return 'Dangerous curve to the left'
    elif classNo == 20: return 'Dangerous curve to the right'
    elif classNo == 21: return 'Double curve'
    elif classNo == 22: return 'Bumpy road'
    elif classNo == 23: return 'Slippery road'
    elif classNo == 24: return 'Road narrows on the right'
    elif classNo == 25: return 'Road work'
    elif classNo == 26: return 'Traffic signals'
    elif classNo == 27: return 'Pedestrians'
    elif classNo == 28: return 'Children crossing'
    elif classNo == 29: return 'Bicycles crossing'  
    elif classNo == 30: return 'Beware of ice/snow'
    elif classNo == 31: return 'Wild animals crossing'
    elif classNo == 32: return 'End of all speed and passing limits'
    elif classNo == 33: return 'Turn right ahead'
    elif classNo == 34: return 'Turn left ahead'
    elif classNo == 35: return 'Ahead only'
    elif classNo == 36: return 'Go straight or right'
    elif classNo == 37: return 'Go straight or left'
    elif classNo == 38: return 'Keep right'
    elif classNo == 39: return 'Keep left'
    elif classNo == 40: return 'Roundabout mandatory'
    elif classNo == 41: return 'End of no passing'
    elif classNo == 42: return 'End of no passing by vehicles over 3.5 metric tons'
    elif classNo == 43: return 'Turn left ahead'
    elif classNo == 44: return 'Turn right ahead'
    elif classNo == 45: return 'Ahead only'
    elif classNo == 46: return 'Go straight or left'
    elif classNo == 47: return 'Go straight or right'
    elif classNo == 48: return 'Keep right'
    elif classNo == 49: return 'Keep left'
    elif classNo == 50: return 'Roundabout mandatory'
    elif classNo == 51: return 'End of no passing'
    elif classNo == 52: return 'End of no passing by vehicles over 3.5 metric tons'
    elif classNo == 53: return 'Priority road'
    elif classNo == 54: return 'Yield'
    elif classNo == 55: return 'Stop'
    elif classNo == 56: return 'No vehicles'
    elif classNo == 57: return 'Vehicles over 3.5 metric tons prohibited'
    else: return 'Unknown traffic sign'

def model_predict(img_path, model):
    """Process image and predict traffic sign class"""
    if model is None:
        return "Model not loaded. Please add model.h5 file.", 0.0
    
    print(f"Processing image: {img_path}")
    
    # Load and resize image
    img = image.load_img(img_path, target_size=(224, 224))
    img = np.asarray(img)
    img = cv2.resize(img, (32, 32))
    
    # Apply preprocessing
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)  # Reshape for CNN input
    
    # Make prediction
    prediction = model.predict(img)
    classIndex = np.argmax(prediction, axis=1)
    probabilityValue = np.amax(prediction)
    
    # Get class name and return results
    preds = getClassName(int(classIndex[0]))
    return preds, float(probabilityValue)

@app.route('/', methods=['GET'])
def index():
    """Main page route"""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    """Handle image upload and return prediction"""
    if request.method == 'POST':
        try:
            # Get uploaded file
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            
            # Make prediction
            preds, probabilityValue = model_predict(file_path, model)
            confidence = round(probabilityValue * 100, 2)
            
            # Return formatted result
            result = f"{preds} (Confidence: {confidence}%)"
            return result
        except Exception as e:
            return f"Error processing image: {str(e)}"
    return None

if __name__ == '__main__':
    app.run(port=5002, debug=True)