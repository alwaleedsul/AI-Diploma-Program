# Equipment and Workshop Setup Guide
## دليل المعدات وإعداد ورشة العمل

**AI Diploma Program - Tuwaiq Academy**  
**Last Updated:** January 7, 2026

---

## Overview

This guide provides comprehensive instructions for setting up the hardware, software, and workspace required for the AI Diploma program.

---

## 1. Hardware Requirements | متطلبات الأجهزة

### 1.1 Minimum System Requirements

**Computer Specifications:**
- **CPU:** Intel i5 (8th gen+) or AMD Ryzen 5 (3000 series+) or equivalent
- **RAM:** 8 GB minimum (16 GB recommended)
- **Storage:** 256 GB SSD minimum (512 GB recommended)
- **GPU:** Optional but recommended for deep learning courses
  - NVIDIA GPU with CUDA support (GTX 1060+ or RTX series)
  - 4 GB VRAM minimum (8 GB+ recommended)

**Peripherals:**
- Monitor (external monitor recommended for better productivity)
- Keyboard and mouse
- Webcam (for online sessions)
- Microphone and speakers/headphones

### 1.2 Recommended Setup

**For Deep Learning Courses (Courses 08-11):**
- **CPU:** Intel i7/i9 or AMD Ryzen 7/9
- **RAM:** 16-32 GB
- **GPU:** NVIDIA RTX 3060 or better (12 GB+ VRAM)
- **Storage:** 1 TB NVMe SSD

**For Cloud-Based Work:**
- Basic laptop/desktop (cloud resources handle computation)
- Stable internet connection (10 Mbps+ recommended)

---

## 2. Software Installation | تثبيت البرمجيات

### 2.1 Operating System

**Supported Operating Systems:**
- Windows 10/11 (64-bit)
- macOS 10.14+ (Intel or Apple Silicon)
- Linux (Ubuntu 18.04+, Debian, Fedora)

### 2.2 Python Installation

**Python Version:** Python 3.8+ (3.10 or 3.11 recommended)

**Installation Steps:**

**Windows:**
1. Download Python from python.org
2. Check "Add Python to PATH" during installation
3. Verify: `python --version` in Command Prompt

**macOS:**
1. Use Homebrew: `brew install python@3.11`
2. Or download from python.org
3. Verify: `python3 --version` in Terminal

**Linux:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

### 2.3 Package Management

**Virtual Environment (Recommended):**
```bash
# Create virtual environment
python -m venv ai_diploma_env

# Activate (Windows)
ai_diploma_env\Scripts\activate

# Activate (macOS/Linux)
source ai_diploma_env/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

**Conda (Alternative):**
```bash
# Create conda environment
conda create -n ai_diploma python=3.11
conda activate ai_diploma

# Install packages
conda install numpy pandas matplotlib scikit-learn
pip install -r requirements.txt
```

---

## 3. Development Tools | أدوات التطوير

### 3.1 Code Editor/IDE

**Recommended Options:**
- **VS Code:** Free, excellent Python support
- **PyCharm:** Professional IDE (free Community edition available)
- **JupyterLab:** Web-based IDE (included with Jupyter)
- **Spyder:** Scientific Python IDE

**VS Code Setup:**
1. Install VS Code from code.visualstudio.com
2. Install Python extension
3. Install Jupyter extension
4. Install Python extension pack

### 3.2 Jupyter Notebooks

**Installation:**
```bash
pip install jupyter jupyterlab notebook
```

**Launch:**
```bash
# Jupyter Notebook
jupyter notebook

# JupyterLab (recommended)
jupyterlab
```

**Access:** Opens in browser at `http://localhost:8888`

---

## 4. Cloud Resources | الموارد السحابية

### 4.1 Cloud Platforms

**For GPU Access (if local GPU unavailable):**

**Google Colab:**
- Free GPU access (limited)
- No setup required
- Access at colab.research.google.com

**Kaggle Notebooks:**
- Free GPU access
- Pre-installed libraries
- Access at kaggle.com

**AWS/GCP/Azure:**
- Paid cloud GPU instances
- More control and resources
- See Course 11 for deployment guides

### 4.2 Cloud Storage

**Recommended:**
- Google Drive (for Colab integration)
- Dropbox
- OneDrive
- GitHub (for code versioning)

---

## 5. Workspace Setup | إعداد مساحة العمل

### 5.1 Directory Structure

**Recommended Structure:**
```
AI_Diploma/
├── Course_01/
├── Course_02/
├── ...
├── Course_12/
├── Projects/
├── Datasets/
└── requirements.txt
```

**Setup:**
```bash
# Create main directory
mkdir AI_Diploma
cd AI_Diploma

# Clone or download course materials
# Organize by course
```

### 5.2 Environment Variables

**Python Path:**
- Ensure Python is in system PATH
- Verify with: `python --version`

**CUDA (if using GPU):**
- Install CUDA toolkit (NVIDIA)
- Install cuDNN
- Verify: `nvidia-smi` (should show GPU info)

---

## 6. Network Requirements | متطلبات الشبكة

### 6.1 Internet Connection

**Minimum:**
- 5 Mbps download
- 2 Mbps upload

**Recommended:**
- 25+ Mbps download
- 10+ Mbps upload
- Stable connection (low latency)

**For:**
- Downloading datasets
- Installing packages
- Cloud-based work
- Online sessions

### 6.2 Firewall and Ports

**Required Ports:**
- Port 8888: Jupyter Notebooks
- Port 5000: Flask applications (if developing APIs)
- Port 8000: Alternative web services

**Firewall Configuration:**
- Allow Python/Jupyter through firewall
- Configure router if needed

---

## 7. Dataset Storage | تخزين البيانات

### 7.1 Local Storage

**Recommended:**
- Dedicated folder for datasets
- Organize by course/topic
- Keep original and processed versions separate

**Structure:**
```
Datasets/
├── raw/          # Original datasets
├── processed/     # Cleaned/processed data
└── external/      # External data sources
```

### 7.2 Cloud Storage

**For Large Datasets:**
- Google Drive (15 GB free)
- AWS S3
- Azure Blob Storage
- Kaggle Datasets

---

## 8. GPU Setup (Optional) | إعداد GPU (اختياري)

### 8.1 NVIDIA GPU Setup

**Windows:**
1. Install NVIDIA drivers
2. Install CUDA toolkit
3. Install cuDNN
4. Install PyTorch/TensorFlow with CUDA support

**macOS:**
- Limited GPU support (Apple Silicon has Metal support)
- Use cloud resources for GPU work

**Linux:**
```bash
# Install NVIDIA drivers
sudo apt install nvidia-driver-XXX

# Install CUDA
# Follow NVIDIA CUDA installation guide

# Verify
nvidia-smi
```

### 8.2 GPU Libraries

**PyTorch (CUDA):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**TensorFlow (GPU):**
```bash
pip install tensorflow[and-cuda]
```

---

## 9. Troubleshooting | حل المشاكل

### 9.1 Common Issues

**Python Not Found:**
- Check PATH environment variable
- Reinstall Python with "Add to PATH" option
- Use `python3` instead of `python` on macOS/Linux

**Package Installation Fails:**
- Upgrade pip: `pip install --upgrade pip`
- Use `pip3` if `pip` doesn't work
- Check internet connection
- Try: `pip install --user package_name`

**Jupyter Won't Start:**
- Check if port 8888 is available
- Try: `jupyter notebook --port 8889`
- Reinstall: `pip install --upgrade jupyter`

**GPU Not Detected:**
- Check drivers: `nvidia-smi`
- Verify CUDA installation
- Check PyTorch/TensorFlow GPU support

### 9.2 Getting Help

**Resources:**
- Course instructor
- Program coordinator
- IT support
- Online forums (Stack Overflow, etc.)

---

## 10. Verification Checklist | قائمة التحقق

### Before Starting

- [ ] Python 3.8+ installed and working
- [ ] Virtual environment created
- [ ] Required packages installed
- [ ] Jupyter Notebooks working
- [ ] Code editor/IDE configured
- [ ] Internet connection stable
- [ ] Workspace organized
- [ ] Backup system in place

### For GPU Work

- [ ] GPU drivers installed
- [ ] CUDA toolkit installed (if NVIDIA)
- [ ] GPU detected by system
- [ ] PyTorch/TensorFlow GPU support verified

---

## 11. Course-Specific Requirements | متطلبات خاصة بالدورة

### Course 02 (Python):
- Python 3.8+
- Basic text editor

### Course 03 (Mathematics):
- NumPy, SciPy, SymPy
- Jupyter Notebooks

### Course 04 (Machine Learning):
- scikit-learn
- pandas, matplotlib

### Course 07 (NLP):
- NLTK, spaCy
- Hugging Face Transformers

### Course 08 (Deep Learning):
- PyTorch or TensorFlow
- GPU recommended

### Course 09 (Reinforcement Learning):
- OpenAI Gym
- Stable-Baselines3

### Course 10 (Generative AI):
- PyTorch/TensorFlow
- GPU highly recommended

### Course 11 (Deployment):
- Docker
- Cloud account (AWS/GCP/Azure)

---

## Additional Resources

- **Python Installation:** https://www.python.org/downloads/
- **VS Code:** https://code.visualstudio.com/
- **Jupyter:** https://jupyter.org/
- **CUDA:** https://developer.nvidia.com/cuda-downloads
- **Docker:** https://www.docker.com/

---

**Remember: Proper setup saves time and prevents issues later. Take time to set up correctly!**

**تذكر: الإعداد الصحيح يوفر الوقت ويمنع المشاكل لاحقاً. خذ الوقت للإعداد بشكل صحيح!**

