# 🤖 AI Resume Classification System

This project is a Machine Learning + NLP based web application that automatically classifies resumes into different job categories using text analysis techniques.

---

## 📌 Why Resume Screening?

- Companies receive thousands of resumes for each job role  
- Manual screening is time-consuming and inefficient  
- Automating this process helps reduce effort and improves accuracy  

👉 This system helps classify resumes in seconds instead of hours.

---

## ⚙️ Working Pipeline

1. Text Preprocessing (cleaning, stopword removal)
2. Feature Extraction using TF-IDF
3. Model Training using KNN Classifier
4. Resume Classification
5. Prediction via Flask Web Interface

---

## 🚀 Features

- Resume classification using Machine Learning  
- NLP-based text preprocessing  
- TF-IDF vectorization  
- Flask-based web interface  
- Real-time prediction  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- Flask  
- NumPy, Pandas  
- NLTK  
- Matplotlib, Seaborn  

---

## 📊 Model

- Algorithm: K-Nearest Neighbors (KNN)  
- Accuracy: ~82% on test dataset  

---

## 🖥️ Application UI

Below is the working interface of the Resume Classification System:

<img width="1196" height="631" alt="image" src="https://github.com/user-attachments/assets/14670776-677b-46a3-9179-20cb6956dd37" />
<img width="1056" height="626" alt="image" src="https://github.com/user-attachments/assets/2c14146e-95a8-4e7d-b9a5-48e61809643e" />
<img width="1187" height="240" alt="image" src="https://github.com/user-attachments/assets/d08d8dc8-a263-42ec-8338-25bd045d6b59" />




## ⚡ Installation

git clone https://github.com/AyushiSaxena03/AI-Resume-Classifier.git

cd AI-Resume-Classifier

pip install -r requirements.txt

python app.py

## Usage
Run the Flask app
Open browser at http://127.0.0.1:5000/
Paste resume text
Click Predict Category
View result
📂 Dataset
Resume dataset containing multiple job categories
Preprocessed using NLP techniques
📈 Results
Achieved ~82% accuracy
Tested across multiple domains (Data Science, Web Dev, HR, etc.)

## 🔮 Future Improvements
Use advanced models (SVM, Logistic Regression)

Improve dataset quality

Deploy on cloud

Add PDF resume upload & parsing

## 💡 Key Learning
NLP preprocessing

Feature engineering using TF-IDF

Model training & evaluation

Building ML-powered web apps using Flask
