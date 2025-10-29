#!/usr/bin/env python3
"""
System Test Script
Tests all components of the traffic sign recognition system
"""

import os
import sys
import importlib
import subprocess

def test_imports():
    """Test if all required packages are installed"""
    print("🧪 Testing Python package imports...")
    
    required_packages = [
        ('flask', 'Flask'),
        ('tensorflow', 'TensorFlow'),
        ('cv2', 'OpenCV'),
        ('numpy', 'NumPy'),
        ('PIL', 'Pillow'),
        ('sklearn', 'Scikit-learn'),
        ('matplotlib', 'Matplotlib'),
        ('pandas', 'Pandas')
    ]
    
    failed_imports = []
    
    for package, name in required_packages:
        try:
            importlib.import_module(package)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} - Not installed")
            failed_imports.append(name)
    
    if failed_imports:
        print(f"\n❌ Missing packages: {', '.join(failed_imports)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All packages installed correctly!")
        return True

def test_file_structure():
    """Test if all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'download_dataset.py',
        'train_model.py',
        'setup_project.py',
        'templates/base.html',
        'templates/index.html',
        'static/css/main.css',
        'static/js/main.js',
        'static/lib/jquery.min.js',
        'static/lib/bootstrap.min.css',
        'static/lib/bootstrap.min.js'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - Missing")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files present!")
        return True

def test_directories():
    """Test if required directories exist"""
    print("\n📂 Testing directories...")
    
    required_dirs = ['uploads', 'templates', 'static', 'static/css', 'static/js', 'static/lib']
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"   ✅ {directory}/")
        else:
            print(f"   ❌ {directory}/ - Missing")
            os.makedirs(directory, exist_ok=True)
            print(f"   🔧 Created {directory}/")
    
    print("✅ All directories ready!")
    return True

def test_flask_app():
    """Test if Flask app can be imported"""
    print("\n🌐 Testing Flask application...")
    
    try:
        sys.path.insert(0, os.getcwd())
        from app import app
        print("   ✅ Flask app imports successfully")
        
        # Test if model loading works (even if model doesn't exist)
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("   ✅ Main page loads successfully")
            else:
                print(f"   ❌ Main page error: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"   ❌ Flask app error: {e}")
        return False
    
    print("✅ Flask application working!")
    return True

def test_model_status():
    """Check model file status"""
    print("\n🧠 Testing model status...")
    
    if os.path.exists('model.h5'):
        file_size = os.path.getsize('model.h5') / (1024 * 1024)  # MB
        print(f"   ✅ Model file exists ({file_size:.1f} MB)")
        return True
    else:
        print("   ⚠️  Model file not found")
        print("   💡 Run 'python train_model.py' to create the model")
        print("   💡 Or run 'python setup_project.py' for full setup")
        return False

def test_dataset_status():
    """Check dataset status"""
    print("\n📊 Testing dataset status...")
    
    if os.path.exists('Dataset'):
        class_dirs = [d for d in os.listdir('Dataset') 
                     if os.path.isdir(os.path.join('Dataset', d)) and d.isdigit()]
        
        if len(class_dirs) >= 43:
            print(f"   ✅ Dataset exists with {len(class_dirs)} classes")
            
            # Count total images
            total_images = 0
            for class_dir in class_dirs[:5]:  # Check first 5 classes
                class_path = os.path.join('Dataset', class_dir)
                images = [f for f in os.listdir(class_path) 
                         if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                total_images += len(images)
            
            print(f"   📷 Sample: {total_images} images in first 5 classes")
            return True
        else:
            print(f"   ⚠️  Dataset incomplete ({len(class_dirs)} classes found)")
            return False
    else:
        print("   ⚠️  Dataset not found")
        print("   💡 Run 'python download_dataset.py' to download")
        return False

def run_full_test():
    """Run all tests"""
    print("🚦 Traffic Sign Recognition System Test")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("File Structure", test_file_structure),
        ("Directories", test_directories),
        ("Flask Application", test_flask_app),
        ("Dataset Status", test_dataset_status),
        ("Model Status", test_model_status)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"   ❌ {test_name} failed with error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is ready to use.")
        print("🚀 Run 'python app.py' to start the web application")
    elif passed >= total - 2:
        print("⚠️  System mostly ready. Check warnings above.")
        print("🚀 You can still run 'python app.py' for demo mode")
    else:
        print("❌ System needs setup. Run 'python setup_project.py'")
    
    return passed == total

if __name__ == "__main__":
    run_full_test()