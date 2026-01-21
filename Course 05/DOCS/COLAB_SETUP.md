# Google Colab Setup Guide | دليل إعداد Google Colab
## Using GPU-Accelerated Notebooks on Google Colab

**For students without NVIDIA GPU:** Use Google Colab for free GPU access!

---

## 🚀 Quick Start | البدء السريع

### Step 1: Open Notebook in Colab

1. **Go to Google Colab:** https://colab.research.google.com/
2. **Upload notebook:**
   - Click "File" → "Upload notebook"
   - Select the notebook file (e.g., `03_cudf_introduction.ipynb`)
   - Or use "File" → "Open notebook" → "GitHub" and paste repository URL

### Step 2: Enable GPU

1. **Click:** "Runtime" → "Change runtime type"
2. **Set:**
   - Hardware accelerator: **GPU** (T4 or better)
   - Runtime type: **Python 3**
3. **Click:** "Save"

### Step 3: Install RAPIDS (GPU Libraries)

**Add this cell at the beginning of your notebook:**

```python
# Install RAPIDS for GPU acceleration (Colab)
import subprocess
import sys

def install_rapids():
    """Install RAPIDS on Google Colab"""
    print("🚀 Installing RAPIDS for GPU acceleration...")
    print("⏳ This may take 5-10 minutes...")
    
    # Install RAPIDS
    subprocess.run([
        sys.executable, "-m", "pip", "install", 
        "--upgrade", "pip"
    ], check=True)
    
    subprocess.run([
        sys.executable, "-m", "pip", "install", 
        "cudf-cu11", "cuml-cu11", "cugraph-cu11", 
        "cuspatial-cu11", "cuproj-cu11", "nvtx-cu11",
        "rmm-cu11", "--extra-index-url=https://pypi.nvidia.com"
    ], check=True)
    
    print("✅ RAPIDS installed successfully!")
    print("🔄 Please restart runtime: Runtime → Restart runtime")

# Run installation
install_rapids()
```

**After installation:**
- Click "Runtime" → "Restart runtime"
- Run the cell again to verify installation

### Step 4: Verify GPU Access

```python
# Verify GPU is available
import torch

if torch.cuda.is_available():
    print(f"✅ GPU Available: {torch.cuda.get_device_name(0)}")
    print(f"   GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("⚠️  GPU not available. Make sure you selected GPU in runtime settings.")
```

---

## 📚 Notebooks That Benefit from GPU

These notebooks work better with GPU:

1. **`03_cudf_introduction.ipynb`** - cuDF (GPU DataFrames)
2. **`07_cudf_import_export_gpu.ipynb`** - cuDF import/export
3. **`13_cpu_vs_gpu_ml.ipynb`** - GPU machine learning
4. **`16_rapids_workflows.ipynb`** - RAPIDS workflows
5. **`08_numba_jit_compilation.ipynb`** - Numba (works on CPU too, but faster with GPU)

---

## 💡 Tips | نصائح

### Free GPU Limits
- **Free tier:** ~12 hours/day of GPU usage
- **Colab Pro:** More GPU hours, better GPUs
- **Solution:** Save your work frequently!

### Best Practices
1. **Enable GPU before installing libraries** - Saves time
2. **Restart runtime after installation** - Ensures libraries load correctly
3. **Save notebooks to Google Drive** - Don't lose your work
4. **Download outputs** - Save generated files locally

### Troubleshooting

**Problem:** "CUDA out of memory"
- **Solution:** Use smaller datasets or restart runtime

**Problem:** "RAPIDS installation fails"
- **Solution:** Make sure GPU is enabled, then restart runtime and try again

**Problem:** "Notebook runs slowly"
- **Solution:** Check that GPU is enabled (Runtime → Change runtime type → GPU)

---

## 🔗 Alternative: Kaggle Notebooks

**Kaggle also provides free GPU:**
1. Go to: https://www.kaggle.com/
2. Create new notebook
3. Enable GPU: Settings → Accelerator → GPU
4. Install RAPIDS using same commands

---

## ✅ Quick Checklist

- [ ] Opened notebook in Google Colab
- [ ] Enabled GPU (Runtime → Change runtime type → GPU)
- [ ] Installed RAPIDS (run installation cell)
- [ ] Restarted runtime
- [ ] Verified GPU access
- [ ] Ready to run GPU-accelerated notebooks!

---

**Last Updated:** January 2025  
**Status:** Ready for use
