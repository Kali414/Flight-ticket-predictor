from flask import Flask, render_template, redirect, url_for
from form import Inputform
import joblib
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "This is a secret key"

model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template("home.html", Title="Home")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    form = Inputform()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            airline=[form.airline.data],
            date_of_journey=[form.date_of_journey.data.strftime("%Y-%m-%d")],  # Converting datetime to string
            source=[form.source.data],
            destination=[form.destination.data],
            dep_time=[form.dep_time.data.strftime("%H:%M:%S")],
            arrival_time=[form.arrival_time.data.strftime("%H:%M:%S")],
            duration=[form.duration.data],
            total_stops=[form.total_stops.data],
            additional_info=[form.additional_info.data]
        ))

        # Debug: Print the input DataFrame and its columns
        print("Input DataFrame:")
        print(x_new)
        print("Columns in input DataFrame:", x_new.columns)

        try:
            prediction = model.predict(x_new)[0]
            message = f"The predicted price is {prediction:,.0f} INR!"
        except KeyError as e:
            # Capture and print the KeyError
            print("KeyError:", e)
            message = f"An error occurred: {e}"
    else:
        message = "Please provide valid input details!"

    return render_template("prediction.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
