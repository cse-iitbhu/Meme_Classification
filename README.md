# 🧠 BiasBreakers – Multilingual Meme Classification

🚀 Official implementation of the BiasBreakers framework
📚 Developed for the LT-EDI 2026 Shared Task on Homophobic and Transphobic Meme Detection

This repository contains the implementation of BiasBreakers, a multimodal meme classification framework designed to detect homophobic and transphobic content across English, Hindi, and Chinese memes.

The system integrates OCR extraction, Vision-Language Models (VLMs), CLIP-based multimodal embeddings, and transformer classifiers to effectively capture the interaction between visual and textual cues in memes.
📬 Contact

For questions, additional code, or dataset access:

Nilendu Adhikary
IIT (BHU), Varanasi
nilendu.adhikary.cd.cse23@iitbhu.ac.in
suplife24@gamil.com
---

## 📌 Project Overview

Memes are inherently multimodal, combining images, embedded text, sarcasm, and contextual signals. Detecting harmful intent in memes is challenging because the hate may arise from the interaction between visual content and textual components.

To address this challenge, our system combines:

🖼 Visual Understanding using pretrained vision encoders

📝 OCR-based Text Extraction from meme images

🤖 Vision-Language Models for semantic understanding

🔗 Multimodal Feature Fusion

🌍 Multilingual Processing for English, Hindi, and Chinese

This allows the framework to perform robust harmful meme detection across multiple languages.

---

## 🗂 Repository Structure
## BiasBreakers
│
## ├── code
## │ ├── chinese_final
## │ ├── english_final
## │ ├── hindi_final
## │ └── qwen_vlm
## │
## └── selected_data



### Folder Description

| Folder | Description |
|------|------|
| `english_final` | Meme classification pipeline for English |
| `hindi_final` | Meme classification pipeline for Hindi |
| `chinese_final` | Meme classification pipeline for Chinese |
| `qwen_vlm` | Vision-Language processing using Qwen models |
| `selected_data` | Sample dataset for testing and demonstration |

---

## ⚙️ Pipeline Architecture

The framework follows a **multimodal classification pipeline**:

1️⃣ **OCR Extraction**  
Text is extracted from meme images using OCR.

2️⃣ **Vision-Language Processing**  
Images and extracted text are processed using **Qwen-VL models**.

3️⃣ **Multimodal Feature Fusion**  
Visual and textual features are combined.

4️⃣ **Meme Classification**  
Final classification is performed on fused representations.

---

## 🚀 Tech Stack

### Languages

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)

### Libraries & Frameworks

![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Transformers](https://img.shields.io/badge/-HuggingFace-FCC624?style=flat&logo=huggingface&logoColor=black)
![SentenceTransformers](https://img.shields.io/badge/-SentenceTransformers-4B8BBE?style=flat)
![EasyOCR](https://img.shields.io/badge/-EasyOCR-2C3E50?style=flat)
![FAISS](https://img.shields.io/badge/-FAISS-0099cc?style=flat)

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/BiasBreakers.git
cd BiasBreakers




Install dependencies

pip install torch
pip install transformers
pip install sentence-transformers
pip install pandas
pip install numpy
pip install easyocr



▶️ Running the Pipeline

Example execution for English:

cd code/english_final
python main.py

You can similarly run pipelines from:

code/hindi_final
code/chinese_final
🧪 Dataset

The repository contains sample data located in:

selected_data/

⚠️ Due to dataset constraints, the complete dataset and intermediate preprocessing scripts are not included in this release.

If you require additional components or clarification regarding the implementation, please contact us.
```



⭐ If you find this repository useful, please consider starring the repo!

