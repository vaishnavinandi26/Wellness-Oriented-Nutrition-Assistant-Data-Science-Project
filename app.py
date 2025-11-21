from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import json

# Initialize Flask app
app = Flask(__name__)

# Load trained ML model and target encoder
model = joblib.load("model/model.pkl")  
target_encoder = joblib.load("model/target_encoder.pkl") 

# Activity level mapping
activity_map = {
    "Sedentary": 1,
    "Lightly active": 2,
    "Moderately active": 3,
    "Very active": 4,
    "Extra active": 5
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Extract input values
        age = data["age"]
        height = data["height"]
        weight = data["weight"]
        gender = 1 if data["gender"] == "Male" else 0
        diabetes = data["diabetes"]
        hypertension = data["hypertension"]
        diet_preference = data["diet_preference"]
        activity_level = activity_map.get(data["activity_level"])
        goal = data["goal"]

        if activity_level is None:
            return jsonify({"error": "Invalid activity level"}), 400

        # Prepare input array
        input_data = np.array([[age, height, weight, gender,
                                diabetes, hypertension,
                                1 if diet_preference == "Veg" else 0,
                                activity_level]])

        # Make prediction
        prediction = model.predict(input_data)[0]
        recommended_diet = target_encoder.inverse_transform([prediction])[0]

        # Calories estimation
        bmi = weight / ((height / 100) ** 2)
        base_calories = 1500 + (activity_level * 100)
        if goal == "Weight Loss":
            recommended_calories = base_calories - 200
        elif goal == "Weight Gain":
            recommended_calories = base_calories + 200
        else:
            recommended_calories = base_calories

        # Diet plan suggestions
        diet_plans = {
            "High Protein Veg": ["Paneer Tikka", "Soya Chunks", "Moong Dal"],
            "High Protein Non-Veg": ["Grilled Chicken", "Boiled Eggs", "Fish Fry"],
            "Balanced Veg": ["Dal, Roti, Rice", "Vegetable Pulao", "Salad"],
            "Balanced Non-Veg": ["Egg Curry", "Chicken Rice Bowl", "Fish Curry"],
            "Low Carb Diet": ["Sprouts Bowl", "Boiled Eggs", "Grilled Fish"],
        }

        return jsonify({
            "recommended_diet": recommended_diet,
            "recommended_calories": recommended_calories,
            "bmi": round(bmi, 2),
            "recipes": diet_plans.get(recommended_diet, ["No recipes available"])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
