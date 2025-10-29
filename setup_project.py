#!/usr/bin/env python3
"""
Traffic Sign Recognition Project Setup Script
Automates the complete setup process
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"   {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("   Please use Python 3.8 or higher")
        return False

def setup_project():
    """Complete project setup"""
    print("🚦 Traffic Sign Recognition Project Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    print("\n📦 Installing Python packages...")
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print("💡 Try: pip install --upgrade pip")
        print("💡 Or: python -m pip install -r requirements.txt")
        return False
    
    # Create necessary directories
    print("\n📁 Creating project directories...")
    directories = ["uploads", "Dataset", "models"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"   ✅ Created {directory}/")
    
    # Download dataset
    print("\n📥 Downloading traffic sign dataset...")
    if not run_command("python download_dataset.py", "Downloading dataset"):
        print("💡 Make sure you have Kaggle API credentials configured")
        print("💡 Visit: https://www.kaggle.com/docs/api")
        return False
    
    # Train model
    print("\n🧠 Training the CNN model...")
    print("⏰ This may take 15-30 minutes depending on your hardware...")
    if not run_command("python train_model.py", "Training model"):
        print("💡 Training failed. Check the error messages above.")
        return False
    
    # Test the web application
    print("\n🌐 Testing web application...")
    print("✅ Setup completed successfully!")
    print("\n🚀 To start the application:")
    print("   python app.py")
    print("\n🌐 Then open: http://localhost:5002")
    
    return True

def quick_setup():
    """Quick setup without training (for demo)"""
    print("🚦 Quick Setup (Demo Mode)")
    print("=" * 30)
    
    # Install requirements only
    if run_command("pip install -r requirements.txt", "Installing requirements"):
        print("\n✅ Quick setup completed!")
        print("🚀 Run: python app.py")
        print("📝 Note: Add your model.h5 file to enable predictions")
        return True
    return False

def main():
    """Main setup function"""
    print("Choose setup option:")
    print("1. Full setup (download dataset + train model)")
    print("2. Quick setup (demo mode only)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        setup_project()
    elif choice == "2":
        quick_setup()
    else:
        print("❌ Invalid choice. Please run again and select 1 or 2.")

if __name__ == "__main__":
    main()