"""
Combine CICIDS2017 CSV files
Combines 8 parts (by day/attack type) into single CSV file

Usage:
    python combine_cicids2017.py
"""

import pandas as pd
from pathlib import Path
import os

# Paths
source_dir = Path("/Users/abdullah/Downloads/archive (5)")
output_dir = Path(__file__).parent.parent / "raw"
output_file = output_dir / "cicids2017.csv"

output_dir.mkdir(parents=True, exist_ok=True)

def combine_cicids2017():
    """Combine CICIDS2017 CSV parts into single file"""
    print("=" * 60)
    print("Combining CICIDS2017 Dataset Parts")
    print("=" * 60)
    
    if output_file.exists():
        print(f"\n✅ CICIDS2017 already exists: {output_file}")
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"   Size: {size_mb:.1f} MB")
        return True
    
    # List of CSV files to combine (in order - all have headers)
    csv_files = [
        source_dir / "Monday-WorkingHours.pcap_ISCX.csv",
        source_dir / "Tuesday-WorkingHours.pcap_ISCX.csv",
        source_dir / "Wednesday-workingHours.pcap_ISCX.csv",
        source_dir / "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
        source_dir / "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
        source_dir / "Friday-WorkingHours-Morning.pcap_ISCX.csv",
        source_dir / "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        source_dir / "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
    ]
    
    # Check all files exist
    missing = [f for f in csv_files if not f.exists()]
    if missing:
        print(f"\n❌ Missing files:")
        for f in missing:
            print(f"   - {f}")
        return False
    
    print(f"\n📥 Found {len(csv_files)} CSV files to combine:")
    total_size = 0
    for f in csv_files:
        size_mb = f.stat().st_size / (1024 * 1024)
        total_size += size_mb
        print(f"   - {f.name} ({size_mb:.1f} MB)")
    print(f"   Total size: {total_size:.1f} MB")
    
    try:
        print(f"\n📊 Reading and combining files...")
        print("   This may take a while (large files, ~844 MB total)...")
        
        # Read first file with header
        print(f"\n   1. Reading {csv_files[0].name}...")
        df_combined = pd.read_csv(csv_files[0])
        print(f"      Rows: {len(df_combined):,}, Columns: {len(df_combined.columns)}")
        
        # Append remaining files (all have headers, so we'll read them and concat)
        for i, csv_file in enumerate(csv_files[1:], 2):
            print(f"\n   {i}. Reading {csv_file.name}...")
            df_part = pd.read_csv(csv_file)
            print(f"      Rows: {len(df_part):,}, Columns: {len(df_part.columns)}")
            df_combined = pd.concat([df_combined, df_part], ignore_index=True)
            print(f"      Total so far: {len(df_combined):,} rows")
        
        print(f"\n✅ Combined successfully!")
        print(f"   Total rows: {len(df_combined):,}")
        print(f"   Total columns: {len(df_combined.columns)}")
        print(f"   Columns: {list(df_combined.columns)[:5]}...")
        
        # Save combined file
        print(f"\n💾 Saving to: {output_file}")
        print("   This may take a while (large file)...")
        df_combined.to_csv(output_file, index=False)
        
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"✅ Saved successfully!")
        print(f"   File: {output_file}")
        print(f"   Size: {size_mb:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error combining files: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    combine_cicids2017()

