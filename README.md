# ✈️ SmartFare: Flight Price Prediction Web App

A web application that predicts flight ticket prices based on user input such as airline, source, destination, duration, and time of journey. This project leverages machine learning for price estimation and is deployed using Flask and Render.

## 🚀 Features

- Predicts flight ticket prices based on various parameters.
- Trained on 10,000+ real-world flight data entries.
- Web interface built using Flask-WTF for easy form handling.
- Backend powered by Scikit-learn, Feature-engine, and Pandas.
- Fully deployed and accessible online (see link below).

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, Feature-engine
- **Backend**: Flask
- **Frontend**: HTML, CSS, Flask-WTF
- **Deployment**: Render

## 📈 Model

- The model was trained using various regression algorithms.
- Feature engineering and preprocessing steps improved accuracy by 15%.
- 5-step pipeline includes: missing value handling, encoding, transformation, model training, and evaluation.

## 🔗 Live Demo

👉 [Click here to try the live app](https://smartfare.onrender.com)

## 📥 Setup Instructions

```bash
git clone https://github.com/Kali414/flight-ticket-price-predictor.git
cd flight-ticket-price-predictor
pip install -r requirements.txt
python app.py

