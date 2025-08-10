# 🎓 NextGrad — Graduate Admission Predictor

**Machine Learning-based Web App | DSBDA Mini Project (SPPU 2025)**  
Predict your chances of admission into graduate school using academic and research credentials.

---

## 🚀 Overview

**NextGrad** is a machine learning-powered web application that predicts a student’s **admission probability (%)** based on several academic and research-based parameters. Built as a mini project for the **Data Science and Business Data Analytics (DSBDA)** course, it aims to demonstrate real-world use of regression models in education analytics.

---

## 📌 Key Features

- 🎯 **Admission Chance Prediction** using:
  - GRE Score
  - TOEFL Score
  - University Rating
  - SOP Strength
  - LOR Strength
  - CGPA
  - Research Experience

- 🌲 **ML Model:** Random Forest Regressor  
- 📊 **Graphical Output:** Progress chart using Chart.js  
- 🖥️ **Responsive UI:** Clean frontend for input and output  
- 📦 **Trained model** loaded using `joblib` for fast predictions  

---

## 🛠️ Tech Stack

**Frontend**  
- HTML5  
- CSS3  
- JavaScript  
- Chart.js  

**Backend**  
- Python (Flask Framework)

**Machine Learning**  
- Random Forest Regressor  
- `pandas`, `numpy`, `scikit-learn`, `joblib`

**Deployment**  
- Localhost (Flask server)

---

## ⚙️ How It Works

1. 📥 User fills out a form with academic details.
2. 📡 Frontend sends a `POST` request to the Flask backend.
3. 🧠 Backend loads the trained ML model and predicts the admission chance.
4. 📈 The result is displayed as a percentage with a dynamic progress chart.

---

## 📊 Dataset

- **Source:** [Graduate Admissions Dataset – Kaggle](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions)  
- **Attributes:**  
  - GRE Score  
  - TOEFL Score  
  - SOP & LOR Ratings  
  - CGPA  
  - University Rating  
  - Research Experience  

---

## 🙌 Acknowledgements

- Developed as part of the 2025 **DSBDA Mini Project** under Savitribai Phule Pune University.
- Inspired by the increasing use of ML in student analytics and educational decision-making.

---

## 💡 Future Enhancements (Optional)

- Deploy on cloud using Render or Vercel  
- Store user data for comparison  
- Add more ML models for comparison  

---

## 👨‍💻 Author

**Aaryan Bairagi**  
GitHub: [@AaryanBairagi](https://github.com/AaryanBairagi)  

---

## 🌟 Thank You for Checking Out **NextGrad!**

