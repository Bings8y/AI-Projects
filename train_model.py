#!/usr/bin/env python3
"""
Traffic Sign Recognition Model Training Script
Trains a CNN model on the downloaded traffic sign dataset
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import warnings
warnings.filterwarnings('ignore')

class TrafficSignTrainer:
    def __init__(self, dataset_path="Dataset/traffic_Data/DATA", img_size=32):
        self.dataset_path = dataset_path
        self.img_size = img_size
        self.num_classes = 58  # Updated to match the actual dataset
        self.model = None
        
    def load_and_preprocess_data(self):
        """Load and preprocess the traffic sign dataset"""
        print("📊 Loading and preprocessing dataset...")
        
        images = []
        labels = []
        
        # Check if dataset exists
        if not os.path.exists(self.dataset_path):
            print(f"❌ Dataset not found at {self.dataset_path}")
            print("🔄 Run 'python download_dataset.py' first to download the dataset")
            return None, None
        
        # Load images from each class directory
        class_dirs = [d for d in os.listdir(self.dataset_path) 
                     if os.path.isdir(os.path.join(self.dataset_path, d)) and d.isdigit()]
        class_dirs.sort(key=int)
        
        print(f"📁 Found {len(class_dirs)} classes")
        
        for class_dir in class_dirs:
            class_path = os.path.join(self.dataset_path, class_dir)
            class_label = int(class_dir)
            
            image_files = [f for f in os.listdir(class_path) 
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            print(f"📷 Class {class_label}: {len(image_files)} images")
            
            for img_file in image_files:
                img_path = os.path.join(class_path, img_file)
                
                try:
                    # Load and preprocess image
                    img = cv2.imread(img_path)
                    if img is not None:
                        # Resize image
                        img = cv2.resize(img, (self.img_size, self.img_size))
                        
                        # Convert to grayscale
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        
                        # Histogram equalization
                        img = cv2.equalizeHist(img)
                        
                        # Normalize
                        img = img / 255.0
                        
                        images.append(img)
                        labels.append(class_label)
                        
                except Exception as e:
                    print(f"⚠️  Error processing {img_path}: {e}")
                    continue
        
        # Convert to numpy arrays
        X = np.array(images)
        y = np.array(labels)
        
        # Reshape for CNN (add channel dimension)
        X = X.reshape(-1, self.img_size, self.img_size, 1)
        
        print(f"✅ Loaded {len(X)} images")
        print(f"📊 Data shape: {X.shape}")
        print(f"🎯 Labels shape: {y.shape}")
        print(f"🔢 Number of classes: {len(np.unique(y))}")
        
        return X, y
    
    def create_model(self):
        """Create CNN model architecture"""
        print("🏗️  Building CNN model...")
        
        model = Sequential([
            # First Convolutional Block
            Conv2D(32, (3, 3), activation='relu', input_shape=(self.img_size, self.img_size, 1)),
            BatchNormalization(),
            Conv2D(32, (3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),
            
            # Second Convolutional Block
            Conv2D(64, (3, 3), activation='relu'),
            BatchNormalization(),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),
            
            # Third Convolutional Block
            Conv2D(128, (3, 3), activation='relu'),
            BatchNormalization(),
            Dropout(0.25),
            
            # Fully Connected Layers
            Flatten(),
            Dense(512, activation='relu'),
            BatchNormalization(),
            Dropout(0.5),
            Dense(256, activation='relu'),
            Dropout(0.5),
            Dense(self.num_classes, activation='softmax')
        ])
        
        # Compile model
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        self.model = model
        
        print("✅ Model created successfully!")
        print(f"📊 Model parameters: {model.count_params():,}")
        
        return model
    
    def train_model(self, X, y, epochs=50, batch_size=32, validation_split=0.2):
        """Train the CNN model"""
        print("🚀 Starting model training...")
        
        # Split data
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=validation_split, random_state=42, stratify=y
        )
        
        print(f"📊 Training samples: {len(X_train)}")
        print(f"📊 Validation samples: {len(X_val)}")
        
        # Data augmentation
        datagen = ImageDataGenerator(
            rotation_range=10,
            zoom_range=0.1,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.1,
            fill_mode='nearest'
        )
        
        # Callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_accuracy',
                patience=10,
                restore_best_weights=True,
                verbose=1
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=1e-7,
                verbose=1
            ),
            ModelCheckpoint(
                'best_model.h5',
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1
            )
        ]
        
        # Train model
        history = self.model.fit(
            datagen.flow(X_train, y_train, batch_size=batch_size),
            steps_per_epoch=len(X_train) // batch_size,
            epochs=epochs,
            validation_data=(X_val, y_val),
            callbacks=callbacks,
            verbose=1
        )
        
        # Evaluate model
        val_loss, val_accuracy = self.model.evaluate(X_val, y_val, verbose=0)
        print(f"\n✅ Training completed!")
        print(f"📊 Final validation accuracy: {val_accuracy:.4f}")
        print(f"📊 Final validation loss: {val_loss:.4f}")
        
        return history
    
    def save_model(self, filename="model.h5"):
        """Save the trained model"""
        if self.model is not None:
            self.model.save(filename)
            print(f"💾 Model saved as {filename}")
        else:
            print("❌ No model to save!")
    
    def plot_training_history(self, history):
        """Plot training history"""
        print("📈 Generating training plots...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # Accuracy plot
        ax1.plot(history.history['accuracy'], label='Training Accuracy')
        ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
        ax1.set_title('Model Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Accuracy')
        ax1.legend()
        ax1.grid(True)
        
        # Loss plot
        ax2.plot(history.history['loss'], label='Training Loss')
        ax2.plot(history.history['val_loss'], label='Validation Loss')
        ax2.set_title('Model Loss')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Loss')
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        plt.savefig('training_history.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📊 Training plots saved as 'training_history.png'")

def main():
    """Main training function"""
    print("🚦 Traffic Sign Recognition Model Training")
    print("=" * 50)
    
    # Initialize trainer
    trainer = TrafficSignTrainer()
    
    # Load data
    X, y = trainer.load_and_preprocess_data()
    if X is None:
        return
    
    # Create model
    model = trainer.create_model()
    
    # Print model summary
    print("\n🏗️  Model Architecture:")
    model.summary()
    
    # Train model
    print(f"\n🚀 Starting training with {len(X)} samples...")
    history = trainer.train_model(X, y, epochs=50, batch_size=32)
    
    # Save model
    trainer.save_model("model.h5")
    
    # Plot results
    trainer.plot_training_history(history)
    
    print("\n🎉 Training completed successfully!")
    print("✅ Your model is ready to use with the web application!")
    print("🚀 Run 'python app.py' to start the web interface")

if __name__ == "__main__":
    main()