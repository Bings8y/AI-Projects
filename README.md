# 🚦 Traffic Sign Recognition System

A modern web-based traffic sign recognition system using Convolutional Neural Networks (CNN) and Flask with real-time predictions and beautiful UI.

## ✨ Features

- **🔍 Real-time Recognition**: Upload images and get instant AI-powered predictions
- **🎯 43 Traffic Sign Classes**: Complete German Traffic Sign Recognition Benchmark support
- **🌍 Speed Unit Conversion**: Automatic km/h to mph conversion for international use
- **📊 Confidence Scoring**: Detailed prediction confidence percentages
- **📱 Responsive Design**: Beautiful, modern interface that works on all devices
- **🔒 Secure Upload**: Safe image processing with file validation
- **⌨️ Keyboard Shortcuts**: Press 'U' to upload, 'P' to predict
- **🖱️ Drag & Drop**: Simply drag images onto the upload area

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask 2.3+** - Lightweight web framework
- **TensorFlow 2.13+** - Deep learning and CNN model
- **OpenCV 4.8+** - Advanced image processing
- **NumPy 1.24+** - Numerical computations

### Frontend
- **HTML5/CSS3** - Modern web standards
- **JavaScript (jQuery 3.6)** - Interactive functionality
- **Bootstrap 4.6** - Responsive UI framework
- **Custom CSS** - Beautiful gradients and animations

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Clone the repository
git clone https://github.com/Bings8y/AI-Projects.git
cd AI-Projects

# Run automated setup
python setup_project.py
# Choose option 1 for full setup (downloads dataset + trains model)
# Choose option 2 for quick demo mode

# Start the application
python app.py
```

### Option 2: Manual Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download traffic sign dataset from Kaggle
python download_dataset.py

# 3. Train the CNN model (15-30 minutes)
python train_model.py

# 4. Run the web application
python app.py
```

### Option 3: Test System
```bash
# Test all components
python test_system.py
```

### 🌐 Access Your App
Navigate to `http://localhost:5002` and start recognizing traffic signs!

## 📋 Usage Guide

1. **📁 Upload**: Click "Choose Traffic Sign Image" or drag & drop
2. **👀 Preview**: Selected image appears with smooth animation
3. **🔍 Predict**: Click "Predict Traffic Sign!" button
4. **📊 Results**: View classification with confidence score
5. **🔄 Repeat**: Upload another image to test more signs

## 🎯 Supported Traffic Signs (43 Classes)

### Speed Limits
- 20 km/h (12 mph) - 120 km/h (75 mph)
- End of speed limit zones

### Prohibitory Signs
- 🛑 Stop signs
- ⚠️ Yield signs  
- 🚫 No entry
- 🚗 No passing
- 🚛 Vehicle restrictions

### Warning Signs
- ⚠️ General caution
- 🌊 Dangerous curves
- 🚧 Road work
- 🚶 Pedestrian crossings
- 👶 Children crossing
- 🚴 Bicycle crossings

### Mandatory Signs
- ➡️ Turn directions
- ⬆️ Straight ahead
- 🔄 Roundabout
- ↗️ Keep right/left

## 📁 Project Structure

```
Traffic-Sign-Recognition/
├── 🐍 app.py                    # Main Flask application
├── 📄 requirements.txt          # Python dependencies
├── 📋 model_info.txt           # Model requirements guide
├── 📂 templates/
│   ├── 🏠 base.html            # Base HTML template
│   └── 🎨 index.html           # Main user interface
├── 📂 static/
│   ├── 🎨 css/main.css         # Custom styling & animations
│   ├── ⚡ js/main.js           # Interactive JavaScript
│   └── 📚 lib/                 # Bootstrap & jQuery
├── 📂 uploads/                 # Temporary image storage
├── 🚫 .gitignore              # Git ignore rules
└── 📖 README.md               # This documentation
```

## 🧠 Model Architecture

```
Input (32×32×1) → Conv2D → MaxPool → Conv2D → MaxPool → Flatten → Dense → Output (43 classes)
```

### Preprocessing Pipeline
1. **Grayscale Conversion**: RGB → Grayscale
2. **Histogram Equalization**: Enhance contrast
3. **Normalization**: Scale pixels to [0,1]
4. **Reshape**: Format for CNN input

### Training Requirements
- **Dataset**: Kaggle Traffic Sign Dataset (`ahemateja19bec1025/traffic-sign-dataset-classification`)
- **Source**: German Traffic Sign Recognition Benchmark (GTSRB)
- **Training Images**: ~39,000 labeled samples across 43 classes
- **Validation**: ~12,000 test images
- **Augmentation**: Rotation, scaling, brightness adjustment, shear transformation

## 🎓 Educational Value

This project demonstrates key computer science concepts:

- **🤖 Machine Learning**: CNN architecture and training
- **🌐 Web Development**: Full-stack application development  
- **👁️ Computer Vision**: Image preprocessing and classification
- **🏗️ Software Engineering**: Clean architecture and documentation
- **🎨 UI/UX Design**: Modern, responsive interface design

## 🔧 Development Features

- **Hot Reload**: Debug mode for development
- **Error Handling**: Comprehensive error messages
- **File Validation**: Size and type checking
- **Responsive Design**: Mobile-friendly interface
- **Accessibility**: Keyboard navigation support

## 🚨 Troubleshooting

### Model Not Found
```
Warning: model.h5 not found. Please add your trained model file.
```
**Solution**: Add your trained model file as `model.h5` in the project root.

### Import Errors
```
ModuleNotFoundError: No module named 'tensorflow'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Port Already in Use
```
Address already in use
```
**Solution**: Change port in `app.py` or kill existing process.

## 📈 Performance Tips

- **Image Size**: Keep uploaded images under 5MB
- **Format**: Use JPG, JPEG, or PNG formats
- **Quality**: Clear, well-lit traffic signs work best
- **Angle**: Front-facing signs provide better accuracy

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork and experiment
- Add new features
- Improve the UI/UX
- Optimize the model
- Add more traffic sign classes

## 📄 License

Educational use only. Perfect for:
- Computer Science coursework
- AI/ML learning projects
- Portfolio demonstrations
- Academic presentations

## 👨‍💻 Author

**Joel Prasad**  
Computer Science Student  
AI/ML Enthusiast  

*Developed as part of AI/ML coursework to demonstrate practical application of deep learning in computer vision.*

---

⭐ **Star this repo if you found it helpful!** ⭐