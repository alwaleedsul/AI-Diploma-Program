"""
Download Cybersecurity Datasets
Downloads UNSW-NB15 and CICIDS2017 datasets using Hugging Face datasets library

Prerequisites:
    pip install datasets huggingface_hub

Usage:
    python download_cybersecurity_datasets.py
"""

import os
from pathlib import Path
import pandas as pd

# Setup directories
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def download_cicids2017():
    """Download CICIDS2017 dataset from Hugging Face"""
    print("\n" + "=" * 60)
    print("📥 Downloading CICIDS2017 Dataset...")
    print("=" * 60)
    
    output_file = RAW_DIR / "cicids2017.csv"
    
    if output_file.exists():
        print(f"✅ CICIDS2017 already exists: {output_file}")
        return True
    
    try:
        from datasets import load_dataset
        
        print("\n📥 Loading dataset from Hugging Face...")
        print("   Dataset: c01dsnap/CIC-IDS2017")
        print("   This may take a while (large dataset)...")
        
        # Load dataset from Hugging Face
        ds = load_dataset("c01dsnap/CIC-IDS2017")
        
        print(f"\n✅ Dataset loaded successfully!")
        print(f"   Split: {list(ds.keys())}")
        
        # Convert to pandas DataFrame
        # Usually the dataset has 'train' split, but check what's available
        if 'train' in ds:
            df = ds['train'].to_pandas()
        elif 'default' in ds:
            df = ds['default'].to_pandas()
        else:
            # Get first available split
            first_split = list(ds.keys())[0]
            print(f"   Using split: {first_split}")
            df = ds[first_split].to_pandas()
        
        print(f"\n📊 Dataset info:")
        print(f"   Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"   Columns: {list(df.columns)[:5]}...")
        
        # Save to CSV
        print(f"\n💾 Saving to CSV...")
        df.to_csv(output_file, index=False)
        
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"✅ Saved successfully!")
        print(f"   File: {output_file}")
        print(f"   Size: {size_mb:.1f} MB")
        
        return True
        
    except ImportError:
        print("\n❌ Error: 'datasets' library not installed")
        print("\n📋 Installation instructions:")
        print("   pip install datasets huggingface_hub")
        return False
    except Exception as e:
        print(f"\n❌ Error downloading CICIDS2017: {e}")
        print("\n💡 Alternative: Download manually from:")
        print("   https://huggingface.co/datasets/c01dsnap/CIC-IDS2017")
        return False

def download_unsw_nb15():
    """Download UNSW-NB15 dataset (manual instructions - not on Hugging Face)"""
    print("\n" + "=" * 60)
    print("📥 UNSW-NB15 Dataset")
    print("=" * 60)
    
    output_file = RAW_DIR / "unsw_nb15.csv"
    
    if output_file.exists():
        print(f"✅ UNSW-NB15 already exists: {output_file}")
        return True
    
    print("\n⚠️  UNSW-NB15 is NOT available on Hugging Face")
    print("   Need to download manually from Zenodo or UNSW")
    print("\n📋 Manual Download Instructions:")
    print("   1. Go to: https://zenodo.org/doi/10.5281/zenodo.10140548")
    print("   2. Download CSV files")
    print("   3. Combine parts if multiple files")
    print("   4. Save as: datasets/raw/unsw_nb15.csv")
    print("\n   Alternative (Official UNSW):")
    print("   https://research.unsw.edu.au/projects/unsw-nb15-dataset")
    
    return False

def main():
    print("=" * 60)
    print("Cybersecurity Datasets Download Script")
    print("=" * 60)
    
    print("\n📋 This script downloads:")
    print("   1. CICIDS2017 (from Hugging Face)")
    print("   2. UNSW-NB15 (manual download - instructions provided)")
    
    # Download CICIDS2017
    cicids_success = download_cicids2017()
    
    # UNSW-NB15 instructions
    unsw_success = download_unsw_nb15()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Download Summary")
    print("=" * 60)
    
    print(f"\n✅ CICIDS2017: {'Downloaded' if cicids_success else 'Failed/Need Manual Download'}")
    print(f"⚠️  UNSW-NB15: Manual download required (instructions above)")
    
    print(f"\n📁 Files location: {RAW_DIR}")
    print("\n✅ Script completed!")

if __name__ == "__main__":
    main()

