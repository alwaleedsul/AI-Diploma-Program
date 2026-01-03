"""
Dataset Download Script
Downloads all datasets required for Course 04 notebooks

Usage:
    python download_datasets.py
"""

import os
import urllib.request
import zipfile
import shutil
from pathlib import Path

# Setup directories
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url, filename, description):
    """Download a file from URL"""
    filepath = RAW_DIR / filename
    if filepath.exists():
        print(f"✅ {description}: Already exists ({filename})")
        return True
    
    try:
        print(f"📥 Downloading {description}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"   ✅ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"   ❌ Error downloading {description}: {e}")
        return False

def main():
    print("=" * 60)
    print("Dataset Download Script for Course 04")
    print("=" * 60)
    
    # Direct URL downloads
    print("\n📥 Downloading datasets with direct URLs...")
    print("-" * 60)
    
    datasets = [
        {
            'url': 'https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv',
            'filename': 'crime_statistics.csv',
            'description': 'Crime Statistics - USArrests (Internal Intelligence)'
        },
        {
            'url': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
            'filename': 'titanic.csv',
            'description': 'Titanic Dataset (Evidence Gathering, Airport Security)'
        }
    ]
    
    downloaded = []
    for dataset in datasets:
        if download_file(dataset['url'], dataset['filename'], dataset['description']):
            downloaded.append(dataset['filename'])
    
    # Manual download instructions
    print("\n" + "=" * 60)
    print("📋 Manual Download Required")
    print("=" * 60)
    print("\nThe following datasets require manual download:")
    print("\n1. Credit Card Fraud Detection (Kaggle)")
    print("   URL: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n2. US-Accidents Dataset (Kaggle)")
    print("   URL: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n3. Global Terrorism Database (GTD)")
    print("   URL: https://www.start.umd.edu/gtd/")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n4. UNSW-NB15 (Cybersecurity - Australia)")
    print("   URL: https://research.unsw.edu.au/projects/unsw-nb15-dataset")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n5. CICIDS2017 (Cybersecurity - Canada)")
    print("   URL: https://www.unb.ca/cic/datasets/ids-2017.html")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n6. 911 Calls (data.gov)")
    print("   URL: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    print("\n7. BTS/CBP Border Data (data.gov)")
    print("   URL: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    print("   Instructions: See datasets/DOWNLOAD_INSTRUCTIONS.md")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Download Summary")
    print("=" * 60)
    print(f"\n✅ Direct downloads completed: {len(downloaded)}")
    print(f"   Files: {', '.join(downloaded)}")
    print(f"\n⚠️  Manual downloads required: 7 datasets")
    print(f"   See: {BASE_DIR / 'DOWNLOAD_INSTRUCTIONS.md'}")
    print(f"\n📁 Download location: {RAW_DIR}")
    print("\n✅ Script completed!")

if __name__ == "__main__":
    main()

