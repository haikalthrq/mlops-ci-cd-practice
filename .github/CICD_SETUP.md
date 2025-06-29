# 🚀 GitHub Actions CI/CD Setup Guide

## 📋 Overview
Project ini menggunakan dua GitHub Actions workflows untuk automasi CI/CD:

1. **Continuous Integration (CI)** - `.github/workflows/ci.yml`
2. **Continuous Deployment (CD)** - `.github/workflows/cd.yml`

## 🔐 Required Secrets Setup

Sebelum workflows dapat berjalan dengan baik, Anda perlu mengatur secrets di GitHub repository:

### 1. Hugging Face Token (`HF`)
1. Buka [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Klik "New Token" 
3. Pilih scope **"Write"** 
4. Copy token yang dihasilkan
5. Di GitHub repository, buka **Settings > Secrets and variables > Actions**
6. Klik **"New repository secret"**
7. Name: `HF` (bukan HF_TOKEN)
8. Value: Paste token dari Hugging Face

### 2. Hugging Face Space Setup
1. Buka [Hugging Face Spaces](https://huggingface.co/spaces)
2. Klik **"Create new Space"**
3. Space name: `mlops-ci-cd-practice` (sesuai dengan nama di file `cd.yml`)
4. License: Pilih yang sesuai (recommend: MIT)
5. Space SDK: **"Gradio"** 
6. Python version: **3.10**

## 🔄 Workflows Explanation

### 🎯 CI Workflow (`ci.yml`) - Now Makefile-based
**Triggers:**
- Push ke branch `main`
- Pull Request ke `main` 
- Manual dispatch

**Steps:**
1. ✅ Checkout Repository
2.  Install Packages (`make install`)
3. 🔍 Format Code (`make format`) 
4. 🧪 Run Tests (`make test`)
5. 🏋️ Train Model (`make train`)
6. 📊 Evaluate Model (`make eval`)
7. ⚙️ Update Branch configuration

### 🚀 CD Workflow (`cd.yml`) - Simplified
**Triggers:**
- When CI workflow completes successfully
- Manual dispatch

**Steps:**
1. ✅ Checkout repository
2. � Deploy to Hugging Face (`make deploy`)

## 🗂️ Project Structure Requirements

```
mlops-ci-cd-practice/
├── app/                    # ✅ Required - Main application code
│   └── app.py             # ✅ Required - Main app file
├── requirements.txt        # ✅ Required - Python dependencies
├── README.md              # ✅ Required - Project documentation
├── tests/                 # ⚠️ Optional - Unit tests
├── train.py              # ⚠️ Optional - Model training script
├── eval.py               # ⚠️ Optional - Model evaluation script
├── model/                # ⚠️ Optional - Saved models
└── results/              # ⚠️ Optional - Training results
```

## 🔧 Customization

### Change Hugging Face Space Name
Edit file `.github/workflows/cd.yml` line ~87:
```bash
SPACE_URL="https://haikalthrq:${HF_TOKEN}@huggingface.co/spaces/haikalthrq/mlops-ci-cd-practice"
```
**Note**: Ganti `haikalthrq` dengan username GitHub Anda yang sebenarnya.

### Add More Linting Rules
Edit file `.github/workflows/ci.yml` di bagian flake8:
```bash
flake8 app/ --count --select=E9,F63,F7,F82,W503 --show-source --statistics
```

### Add More Test Coverage
Jika Anda memiliki folder `tests/`, workflows akan otomatis menjalankan pytest.

## 🐛 Troubleshooting

### Common Issues:

1. **HF_TOKEN tidak valid**
   - Pastikan token memiliki permission "Write"
   - Regenerate token jika diperlukan

2. **Space tidak ditemukan**
   - Pastikan Space sudah dibuat di Hugging Face
   - Periksa nama space di workflow file

3. **"src refspec main does not match any" error**
   - Fixed: Workflow sekarang menggunakan `git init -b main` untuk default branch
   - Fallback: Jika git versi lama, akan otomatis checkout ke branch main

4. **File terlalu besar**
   - Workflows sudah dikonfigurasi dengan Git LFS
   - File .pkl, .joblib, .h5, .bin, .safetensors akan otomatis menggunakan LFS

5. **Dependencies error**
   - Pastikan `requirements.txt` mencantumkan semua dependencies
   - Periksa compatibility antar package

## ✨ Best Practices

1. **Always test locally** before pushing
2. **Keep requirements.txt updated**
3. **Use semantic commit messages**
4. **Add unit tests** for critical functions
5. **Monitor workflow runs** di GitHub Actions tab

## 📞 Support

Jika ada masalah, periksa:
1. GitHub Actions logs untuk error details
2. Hugging Face Space logs 
3. Requirements.txt untuk missing dependencies

---
**Happy Coding! 🎉**
