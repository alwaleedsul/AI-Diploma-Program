# Google Colab Setup Guide for Generative AI | دليل إعداد Google Colab للذكاء الاصطناعي التوليدي
## Using GPU-Accelerated Notebooks on Google Colab

**For students without NVIDIA GPU:** Use Google Colab for free GPU access!

**⚠️ IMPORTANT:** Generative AI models (GANs, VAEs, Stable Diffusion) are **VERY slow on CPU**. GPU is **strongly recommended**!

---

## 🚀 Quick Start | البدء السريع

### Step 1: Open Notebook in Colab

1. **Go to Google Colab:** https://colab.research.google.com/
2. **Upload notebook:**
   - Click "File" → "Upload notebook"
   - Select the notebook file (e.g., `02_image_generation_advanced.ipynb`)
   - Or use "File" → "Open notebook" → "GitHub" and paste repository URL

### Step 2: Enable GPU

1. **Click:** "Runtime" → "Change runtime type"
2. **Set:**
   - Hardware accelerator: **GPU** (T4 or better, A100 preferred for large models)
   - Runtime type: **Python 3**
3. **Click:** "Save"

### Step 3: Install Generative AI Libraries

**Add this cell at the beginning of your notebook (or run the Colab setup cell):**

```python
# Install generative AI libraries
!pip install -q diffusers transformers accelerate torch torchvision
```

**The setup cell will:**
- Detect Colab environment
- Install diffusers, transformers, accelerate
- Verify GPU access

### Step 4: Verify GPU Access

```python
# Verify GPU is available
import torch

if torch.cuda.is_available():
    print(f"✅ GPU Available: {torch.cuda.get_device_name(0)}")
    print(f"   GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("⚠️  GPU not available. Make sure you selected GPU in runtime settings.")
    print("   ⚠️  WARNING: Generative AI training will be VERY slow on CPU!")
```

---

## 📚 Notebooks That Require GPU

These notebooks **strongly require** GPU:

1. **`02_image_generation_advanced.ipynb`** - Stable Diffusion (requires GPU)
2. **GAN notebooks** - GAN training (very slow on CPU)
3. **VAE notebooks** - VAE training (benefits greatly from GPU)
4. **Text generation notebooks** - Large language models (require GPU)

---

## 💡 Tips | نصائح

### Free GPU Limits
- **Free tier:** ~12 hours/day of GPU usage
- **Colab Pro:** More GPU hours, better GPUs (T4, V100, A100)
- **Solution:** Save your work frequently!

### Best Practices
1. **Enable GPU before installing libraries** - Saves time
2. **Use smaller models for testing** - Faster iteration
3. **Save generated outputs** - Download images/texts locally
4. **Monitor GPU memory** - Use `nvidia-smi` or `torch.cuda.memory_allocated()`
5. **Save model checkpoints** - Don't lose training progress

### Memory Management
- **Stable Diffusion:** Requires ~8GB+ GPU memory
- **GANs:** Require 4-8GB GPU memory
- **VAEs:** Require 2-4GB GPU memory
- **If out of memory:** Use smaller batch sizes, lower resolution, or smaller models

### Troubleshooting

**Problem:** "CUDA out of memory"
- **Solution:** Reduce batch size, use lower resolution, or use smaller models

**Problem:** "Training is extremely slow"
- **Solution:** Check that GPU is enabled (Runtime → Change runtime type → GPU)

**Problem:** "Model generation fails"
- **Solution:** Ensure GPU is enabled and has enough memory (8GB+ recommended)

---

## 🔗 Alternative: Kaggle Notebooks

**Kaggle also provides free GPU:**
1. Go to: https://www.kaggle.com/
2. Create new notebook
3. Enable GPU: Settings → Accelerator → GPU
4. Install libraries: `!pip install diffusers transformers accelerate`

---

## ⚠️ Important Notes

1. **CPU is NOT recommended** for generative AI - training can take days/weeks
2. **GPU is essential** for reasonable training times (hours instead of days)
3. **Colab free tier** is perfect for learning and small experiments
4. **For production:** Consider Colab Pro or cloud GPU instances

---

## ✅ Quick Checklist

- [ ] Opened notebook in Google Colab
- [ ] Enabled GPU (Runtime → Change runtime type → GPU)
- [ ] Ran Colab setup cell
- [ ] Installed generative AI libraries
- [ ] Restarted runtime
- [ ] Verified GPU access
- [ ] Ready to generate AI content!

---

**Last Updated:** January 2025  
**Status:** Ready for use
