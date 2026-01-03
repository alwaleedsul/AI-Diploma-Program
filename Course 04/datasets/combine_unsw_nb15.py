"""
Combine UNSW-NB15 CSV files
Combines 4 parts into single CSV file

Usage:
    python combine_unsw_nb15.py
"""

import pandas as pd
from pathlib import Path
import os

# Paths
source_dir = Path("/Users/abdullah/Downloads/10140548")
output_dir = Path(__file__).parent.parent / "raw"
output_file = output_dir / "unsw_nb15.csv"

output_dir.mkdir(parents=True, exist_ok=True)

def combine_unsw_nb15():
    """Combine UNSW-NB15 CSV parts into single file"""
    print("=" * 60)
    print("Combining UNSW-NB15 Dataset Parts")
    print("=" * 60)
    
    if output_file.exists():
        print(f"\n✅ UNSW-NB15 already exists: {output_file}")
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"   Size: {size_mb:.1f} MB")
        return True
    
    # List of CSV files to combine (in order)
    csv_files = [
        source_dir / "UNSW-NB15_1.csv",
        source_dir / "UNSW-NB15_2.csv",
        source_dir / "UNSW-NB15_3.csv",
        source_dir / "UNSW-NB15_4.csv"
    ]
    
    # Check all files exist
    missing = [f for f in csv_files if not f.exists()]
    if missing:
        print(f"\n❌ Missing files:")
        for f in missing:
            print(f"   - {f}")
        return False
    
    print(f"\n📥 Found {len(csv_files)} CSV files to combine:")
    for f in csv_files:
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"   - {f.name} ({size_mb:.1f} MB)")
    
    try:
        print(f"\n📊 Reading and combining files...")
        print("   This may take a while (large files)...")
        
        # Read first file with header
        print(f"\n   1. Reading {csv_files[0].name}...")
        df_combined = pd.read_csv(csv_files[0])
        print(f"      Rows: {len(df_combined):,}")
        
        # Append remaining files (skip header for parts 2-4)
        for i, csv_file in enumerate(csv_files[1:], 2):
            print(f"\n   {i}. Reading {csv_file.name}...")
            df_part = pd.read_csv(csv_file)
            print(f"      Rows: {len(df_part):,)}")
            df_combined = pd.concat([df_combined, df_part], ignore_index=True)
            print(f"      Total so far: {len(df_combined):,} rows")
        
        print(f"\n✅ Combined successfully!")
        print(f"   Total rows: {len(df_combined):,}")
        print(f"   Total columns: {len(df_combined.columns)}")
        print(f"   Columns: {list(df_combined.columns)[:5]}...")
        
        # Save combined file
        print(f"\n💾 Saving to: {output_file}")
        df_combined.to_csv(output_file, index=False)
        
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"✅ Saved successfully!")
        print(f"   File: {output_file}")
        print(f"   Size: {size_mb:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error combining files: {e}")
        return False

if __name__ == "__main__":
    combine_unsw_nb15()

