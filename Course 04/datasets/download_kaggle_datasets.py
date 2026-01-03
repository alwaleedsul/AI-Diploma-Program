"""
Kaggle Dataset Download Script
Automates downloading of Kaggle datasets for Course 04

Prerequisites:
1. Kaggle account: https://www.kaggle.com/account/register
2. Kaggle API credentials: https://www.kaggle.com/settings → API → Create New Token
3. Install: pip install kaggle

Usage:
    python download_kaggle_datasets.py
"""

import os
import subprocess
import sys
from pathlib import Path

# Setup directories
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def check_kaggle_installed():
    """Check if Kaggle API is installed"""
    try:
        result = subprocess.run(['kaggle', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_kaggle_credentials():
    """Check if Kaggle credentials are set up"""
    kaggle_dir = Path.home() / ".kaggle"
    kaggle_json = kaggle_dir / "kaggle.json"
    
    if kaggle_json.exists():
        # Check permissions
        stat = os.stat(kaggle_json)
        mode = stat.st_mode
        # Check if permissions are secure (readable only by owner)
        if (mode & 0o077) == 0:
            return True
    
    return False

def download_dataset(dataset_id, output_filename, description):
    """Download a Kaggle dataset"""
    print(f"\n📥 Downloading {description}...")
    print(f"   Dataset: {dataset_id}")
    print(f"   Output: {output_filename}")
    
    # Check if already exists
    output_path = RAW_DIR / output_filename
    if output_path.exists():
        print(f"   ✅ Already exists: {output_filename}")
        return True
    
    try:
        # Download to raw directory
        cmd = ['kaggle', 'datasets', 'download', '-d', dataset_id, '-p', str(RAW_DIR)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Extract ZIP file
        zip_file = RAW_DIR / f"{dataset_id.split('/')[-1]}.zip"
        if zip_file.exists():
            print(f"   📦 Extracting {zip_file.name}...")
            import zipfile
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(RAW_DIR)
            zip_file.unlink()  # Delete ZIP after extraction
            print(f"   ✅ Extracted successfully")
        
        # Find the CSV file and rename if needed
        csv_files = list(RAW_DIR.glob("*.csv"))
        if csv_files:
            # If multiple CSV files, use the largest one (main dataset)
            if len(csv_files) > 1:
                csv_file = max(csv_files, key=lambda p: p.stat().st_size)
            else:
                csv_file = csv_files[0]
            
            # Rename to desired filename
            if csv_file.name != output_filename:
                csv_file.rename(output_path)
                print(f"   ✅ Renamed to: {output_filename}")
            else:
                print(f"   ✅ Saved as: {output_filename}")
        
        # Check file size
        if output_path.exists():
            size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"   📊 File size: {size_mb:.1f} MB")
            return True
        else:
            print(f"   ⚠️  Downloaded but CSV file not found")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error downloading: {e.stderr}")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Kaggle Dataset Download Script for Course 04")
    print("=" * 60)
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    
    if not check_kaggle_installed():
        print("\n❌ Kaggle API not installed!")
        print("\n📋 Installation instructions:")
        print("   1. Install: pip install kaggle")
        print("   2. Get credentials: https://www.kaggle.com/settings → API → Create New Token")
        print("   3. Save kaggle.json to ~/.kaggle/ (Linux/Mac) or C:\\Users\\<User>\\.kaggle\\ (Windows)")
        print("   4. Set permissions: chmod 600 ~/.kaggle/kaggle.json")
        print("\n   Or use manual download: See KAGGLE_DOWNLOAD_GUIDE.md")
        sys.exit(1)
    
    print("   ✅ Kaggle API installed")
    
    if not check_kaggle_credentials():
        print("\n⚠️  Kaggle credentials not found or insecure!")
        print("\n📋 Setup instructions:")
        print("   1. Go to: https://www.kaggle.com/settings")
        print("   2. Scroll to 'API' section")
        print("   3. Click 'Create New Token'")
        print("   4. Save kaggle.json to ~/.kaggle/ (Linux/Mac)")
        print("   5. Set permissions: chmod 600 ~/.kaggle/kaggle.json")
        print("\n   Or use manual download: See KAGGLE_DOWNLOAD_GUIDE.md")
        sys.exit(1)
    
    print("   ✅ Kaggle credentials found")
    
    # Define datasets to download
    datasets = [
        {
            'id': 'mlg-ulb/creditcardfraud',
            'filename': 'creditcard_fraud.csv',
            'description': 'Credit Card Fraud Detection (European Data)'
        },
        {
            'id': 'sobhanmoosavi/us-accidents',
            'filename': 'us_accidents.csv',
            'description': 'US-Accidents Dataset (Traffic Management)'
        }
    ]
    
    # Download datasets
    print("\n" + "=" * 60)
    print("📥 Downloading Kaggle Datasets")
    print("=" * 60)
    
    downloaded = []
    failed = []
    
    for dataset in datasets:
        success = download_dataset(
            dataset['id'],
            dataset['filename'],
            dataset['description']
        )
        
        if success:
            downloaded.append(dataset['filename'])
        else:
            failed.append(dataset['description'])
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Download Summary")
    print("=" * 60)
    
    print(f"\n✅ Successfully downloaded: {len(downloaded)}")
    for filename in downloaded:
        print(f"   - {filename}")
    
    if failed:
        print(f"\n❌ Failed downloads: {len(failed)}")
        for desc in failed:
            print(f"   - {desc}")
        print("\n💡 Troubleshooting:")
        print("   - Check internet connection")
        print("   - Verify Kaggle account is logged in")
        print("   - Accept dataset terms on Kaggle website")
        print("   - See KAGGLE_DOWNLOAD_GUIDE.md for manual download")
    
    print(f"\n📁 Files location: {RAW_DIR}")
    print("\n✅ Script completed!")

if __name__ == "__main__":
    main()

