Wellness-Oriented Nutrition Assistant
A Data Science & Machine Learning Based Personalized Nutrition System
<img src="https://img.icons8.com/color/452/healthy-food.png" width="120"/>
📊 Project Overview

The Wellness-Oriented Nutrition Assistant is a Data Science project that uses Machine Learning algorithms, nutritional calculations, and a Flask web interface to give personalized diet recommendations.
It offers meal plans based on user health parameters like age, gender, height, weight, activity level, medical history, and dietary preferences.

🏗️ System Architecture
<img src="IMAGE_LINK_HERE" alt="System Architecture" width="700"/>

(Replace IMAGE_LINK_HERE with your architecture diagram link)

🔬 Data Science Workflow
1️⃣ Data Collection & Cleaning

Structured dataset with nutritional parameters

Missing value handling

Feature encoding (gender, diet type, activity level)

Outlier removal

Feature engineering (BMR, TDEE, calorie category)

2️⃣ Model Development

Classification model using Random Forest

Compared with baseline Random Classifier

Performance metrics: Accuracy, Precision, Recall, F1 Score

Model stored using joblib

3️⃣ Web Integration (Flask)

Inputs collected through HTML form

Flask backend converts input → ML feature vector

Model predicts recommended diet plan

BMR & calories calculated using Mifflin-St Jeor formula

Calorie-wise Indian meal suggestions returned as JSON

💻 Tech Stack
<img src="https://skillicons.dev/icons?i=python,flask,html,css,bootstrap" width="400"/>

Python, NumPy, Pandas

Scikit-Learn

Flask

HTML / CSS / Bootstrap

Joblib

Jinja2 Templates

🧩 Key Features

✔ Personalized diet recommendation using ML
✔ Real-time BMR, TDEE & calorie calculation
✔ Supports medical conditions (Diabetes, Hypertension)
✔ Veg / Non-Veg smart meal plan choices
✔ Alternative Indian recipe suggestions
✔ User-friendly web interface built with Flask

🖥️ Screenshots
🔵 Input Page
<img src="SCREENSHOT_INPUT_LINK" alt="Input Page" width="700"/>
🟢 Output Page
<img src="SCREENSHOT_OUTPUT_LINK" alt="Result Page" width="700"/>

(Upload your screenshots to GitHub → right-click → Copy Image Address → replace links above.)

📂 Project Structure
Nutrition-App/
│── app.py
│── model/
│     ├── model.pkl
│     ├── target_encoder.pkl
│── templates/
│     ├── index.html
│     ├── result.html
│── static/
│     ├── style.css
│── README.md

🧠 How the Model Works
<img src="https://img.icons8.com/color/96/artificial-intelligence.png" width="120"/>

User inputs → encoded numerically

ML model predicts meal category

BMR & calorie needs calculated

Recipes mapped with calorie values

Output delivered via Flask web UI

📈 Use Case (Data Science Focus)

This project represents a complete end-to-end DS workflow:

Dataset creation

Preprocessing & feature engineering

Model training & evaluation

API deployment

Web UI integration

Result visualization

Perfect for Data Science portfolios, ML applications, and academic submissions.

🚀 Future Enhancements

✨ Deep learning–based personalized diet prediction
✨ Food recognition using computer vision
✨ Wearable device integration
✨ Chatbot assistant
✨ Multilingual UI
✨ User history + diet tracking system
