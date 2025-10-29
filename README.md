# Traffic Sign Recognition System

A web-based traffic sign recognition system using Convolutional Neural Networks (CNN) and Flask.

## Features

- **Real-time Traffic Sign Recognition**: Upload images and get instant predictions
- **43 Traffic Sign Classes**: Supports German Traffic Sign Recognition Benchmark dataset
- **Speed Unit Conversion**: Displays both km/h and mph for speed limit signs
- **Confidence Scoring**: Shows prediction confidence percentage
- **Responsive Web Interface**: Modern, user-friendly design
- **Secure File Upload**: Safe image processing and handling

## Technology Stack

### Backend
- **Python 3.8+**
- **Flask**: Web framework
- **TensorFlow/Keras**: Deep learning model
- **OpenCV**: Image processing
- **NumPy**: Numerical computations

### Frontend
- **HTML5/CSS3**: Structure and styling
- **JavaScript (jQuery)**: Interactive functionality
- **Bootstrap 4**: Responsive design framework

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bings8y/AI-Projects.git
cd AI-Projects
```

2. Install dependencies:
```bash
pip install flask tensorflow opencv-python numpy pillow
```

3. Add your trained model:
   - Place your `model.h5` file in the project root
   - The model should be trained on German Traffic Sign Recognition Benchmark

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5002`

## Usage

1. **Upload Image**: Click "Choose Image..." and select a traffic sign image
2. **Preview**: The selected image will be displayed
3. **Predict**: Click the "Predict!" button to classify the traffic sign
4. **Results**: View the prediction with confidence percentage

## Supported Traffic Signs

The system recognizes 43 different traffic sign categories including:

- **Speed Limits**: 20, 30, 50, 60, 70, 80, 100, 120 km/h
- **Prohibitory Signs**: Stop, Yield, No Entry, No Passing
- **Warning Signs**: General Caution, Curves, Road Work, Pedestrians
- **Mandatory Signs**: Turn Directions, Keep Right/Left, Roundabout

## Project Structure

```
AI-Projects/
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html         # HTML base template
│   └── index.html        # Main interface
├── static/
│   ├── css/main.css      # Custom styling
│   ├── js/main.js        # Frontend JavaScript
│   └── lib/              # Bootstrap & jQuery libraries
├── uploads/              # Temporary file storage
└── README.md            # Project documentation
```

## Model Architecture

- **Input**: 32x32 grayscale images
- **Architecture**: Convolutional Neural Network
- **Output**: 43 traffic sign classes
- **Preprocessing**: Grayscale conversion, histogram equalization, normalization

## Academic Project

This project was developed as part of a computer science curriculum to demonstrate:

- **Machine Learning**: CNN implementation and usage
- **Web Development**: Full-stack application development
- **Image Processing**: Computer vision techniques
- **Software Engineering**: Clean code structure and documentation

## License

This project is for educational purposes.

## Author

Developed by Joel Prasad as part of AI/ML coursework.