#!/usr/bin/env python3
"""
Traffic Sign Dataset Download Script
Downloads the traffic sign dataset from Kaggle using kagglehub
"""

import kagglehub
import os
import shutil

def download_traffic_sign_dataset():
    """Download and organize the traffic sign dataset"""
    
    print("🚀 Starting Traffic Sign Dataset Download...")
    print("=" * 50)
    
    try:
        # Download latest version of the dataset
        print("📥 Downloading dataset from Kaggle...")
        path = kagglehub.dataset_download("ahemateja19bec1025/traffic-sign-dataset-classification")
        print(f"✅ Dataset downloaded to: {path}")
        
        # Create organized directory structure
        project_root = os.getcwd()
        dataset_dir = os.path.join(project_root, "Dataset")
        
        print(f"📁 Organizing dataset in: {dataset_dir}")
        
        # Copy dataset to project directory if not already there
        if path != dataset_dir:
            if os.path.exists(dataset_dir):
                print("🗑️  Removing existing dataset directory...")
                shutil.rmtree(dataset_dir)
            
            print("📋 Copying dataset to project directory...")
            shutil.copytree(path, dataset_dir)
            print("✅ Dataset copied successfully!")
        
        # List dataset contents
        print("\n📊 Dataset Structure:")
        print("-" * 30)
        
        for root, dirs, files in os.walk(dataset_dir):
            level = root.replace(dataset_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            
            # Show first few files in each directory
            subindent = ' ' * 2 * (level + 1)
            for i, file in enumerate(files[:3]):
                print(f"{subindent}{file}")
            if len(files) > 3:
                print(f"{subindent}... and {len(files) - 3} more files")
        
        print(f"\n🎯 Total directories: {len([d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))])}")
        
        # Count total images
        total_images = 0
        for root, dirs, files in os.walk(dataset_dir):
            total_images += len([f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        print(f"🖼️  Total images: {total_images}")
        
        print("\n✅ Dataset download and organization complete!")
        print("🚀 You can now run 'python train_model.py' to train your model")
        
        return dataset_dir
        
    except Exception as e:
        print(f"❌ Error downloading dataset: {str(e)}")
        print("💡 Make sure you have:")
        print("   1. Installed kagglehub: pip install kagglehub")
        print("   2. Kaggle API credentials configured")
        print("   3. Internet connection")
        return None

if __name__ == "__main__":
    download_traffic_sign_dataset()