# AURA-AI-NEURAL-STYLIST

# AURA AI – Neural Stylist

## Overview

AURA AI is an AI-powered fashion recommendation system that analyzes a user’s facial skin tone using computer vision and provides personalized fashion color recommendations.

The project combines:

* MediaPipe Face Detection
* OpenCV Skin Segmentation
* Streamlit Interactive UI
* AI-Based Fashion Suggestions

Users can capture their image directly from the webcam, and the system detects:

* Face region
* Skin tone
* Complexion category
* Undertone
* Suitable fashion colors

The application also generates:

* Fashion shopping links
* Downloadable AI report

---

# Features

## AI Face Detection

Uses MediaPipe Face Detection to accurately detect the face region in real time.

## Skin Tone Detection

Uses OpenCV HSV color segmentation to identify skin pixels.

## Complexion Classification

Classifies users into categories such as:

* Fair / Light
* Medium / Olive
* Tan / Mid-Dark
* Deep Dark

## Undertone Detection

Predicts basic undertones:

* Cool
* Warm
* Neutral
* Bold

## Fashion Recommendation Engine

Suggests color palettes that match the detected skin tone.

## Amazon Fashion Links

Generates direct Amazon search links for:

* Shirts
* Blazers
* Kurtas
* Sneakers

## Downloadable Report

Allows users to download the AI-generated style analysis report.

## Futuristic UI

Modern cyberpunk-inspired interface built with custom Streamlit CSS.

---

# Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| Streamlit  | Frontend Web Application  |
| OpenCV     | Image Processing          |
| MediaPipe  | Face Detection            |
| NumPy      | Numerical Computation     |
| Pillow     | Image Handling            |

---

# Project Architecture

```text
User Camera Input
        ↓
MediaPipe Face Detection
        ↓
Face Cropping
        ↓
OpenCV Skin Segmentation
        ↓
HSV Skin Pixel Analysis
        ↓
Complexion Classification
        ↓
Undertone Prediction
        ↓
Fashion Recommendation Engine
        ↓
AI Dashboard Output
```

---

# Installation Guide

## Step 1 – Clone Repository

```bash
git clone https://github.com/AdityaCypherX/AURA-AI-NEURAL-STYLIST.git
```

---

## Step 2 – Open Project Folder

```bash
cd AURA-AI-NEURAL-STYLIST
```

---

## Step 3 – Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Step 4 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 – Run Streamlit App

```bash
streamlit run app.py
```

---

# How It Works

## 1. Camera Capture

The user captures an image using Streamlit camera input.

---

## 2. Face Detection

MediaPipe detects the face bounding box.

```python
face_detector = mp_face.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.5
)
```

---

## 3. Skin Segmentation

The face region is converted into HSV color space.

```python
hsv = cv2.cvtColor(face, cv2.COLOR_BGR2HSV)
```

Skin mask is created using HSV thresholds.

```python
lower_skin = np.array([0, 30, 60], dtype=np.uint8)
upper_skin = np.array([25, 255, 255], dtype=np.uint8)
```

---

## 4. Average Skin Intensity

The system calculates average brightness values from skin pixels.

```python
avg_skin = np.mean(skin_pixels)
```

---

## 5. AI Classification

The system predicts:

* Complexion
* Undertone
* Recommended colors

Based on predefined intensity thresholds.

---

# Fashion Recommendation Logic

| Skin Tone      | Undertone | Recommended Colors                 |
| -------------- | --------- | ---------------------------------- |
| Fair / Light   | Cool      | Emerald Green, Navy Blue, Lavender |
| Medium / Olive | Warm      | Mustard, Teal, Earthy Browns       |
| Tan / Mid-Dark | Neutral   | White, Sky Blue, Royal Purple      |
| Deep Dark      | Bold      | Bright Red, Cobalt Blue, Gold      |

---

# Folder Structure

```text
AURA-AI-NEURAL-STYLIST/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# UI Highlights

## Sidebar Features

* Camera input
* Analyze button
* Project description
* User instructions

## Dashboard Features

* Face detection preview
* Skin region visualization
* AI analysis card
* Shopping recommendations
* Report download button

---

# Sample Output

## AI Analysis Result

```text
Detected Complexion: Medium / Olive
Undertone: Warm
Recommended Palette: Mustard, Teal, Earthy Browns
```

---

# Future Enhancements

The project can be expanded using:

* Deep Learning Skin Analysis
* Emotion Detection
* Gender Detection
* Age Prediction
* AI Outfit Recommendation
* Real-Time Webcam Video Analysis
* Seasonal Fashion Recommendations
* Celebrity Style Matching
* Virtual Try-On System
* MongoDB User Profiles
* Cloud Deployment

---

# Deployment Options

The project can be deployed on:

* Streamlit Cloud
* Render
* Railway
* Hugging Face Spaces
* AWS EC2
* Azure App Service

---

# Challenges Faced

* Accurate skin segmentation under different lighting conditions
* False detections in low-light environments
* HSV threshold tuning
* Real-time processing optimization

---

# Learning Outcomes

This project demonstrates:

* Computer Vision fundamentals
* AI-based recommendation systems
* Image preprocessing
* Face detection techniques
* Streamlit frontend integration
* Real-time AI application development

---

# Applications

AURA AI can be used in:

* Fashion Industry
* E-Commerce
* Personal Styling Platforms
* Beauty Recommendation Systems
* Smart Retail Applications
* AI Shopping Assistants

---

# Screenshots

<img width="602" height="488" alt="Screenshot 2026-05-14 170350" src="https://github.com/user-attachments/assets/742628cc-1d21-4c6b-a498-b795bf103784" />
<img width="567" height="564" alt="Screenshot 2026-05-14 170332" src="https://github.com/user-attachments/assets/3b2034df-2220-49b7-b637-0e3c91b525ce" />
<img width="1527" height="608" alt="Screenshot 2026-05-14 170302" src="https://github.com/user-attachments/assets/b4da6dfc-af80-48c5-b94f-2d611e4bc35e" />

```

---

# Author

## Aditya

AI/ML & Data Scientist Enthusiast

GitHub:

[https://github.com/AdityaCypherX](https://github.com/AdityaCypherX)

---

---

# Acknowledgements

Special thanks to:

* Streamlit
* OpenCV
* MediaPipe
* Python Community

for providing powerful open-source tools.

---

# Conclusion

AURA AI demonstrates how Artificial Intelligence and Computer Vision can be integrated into the fashion industry to provide personalized styling experiences.

The project combines real-time image analysis with AI-powered recommendations to create a smart fashion assistant capable of enhancing user appearance through data-driven color suggestions.
