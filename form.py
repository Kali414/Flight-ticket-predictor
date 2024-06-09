import pandas as pd
from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    IntegerField,
    SubmitField,
    TimeField,
    DateField,
    SelectField
)

from wtforms.validators import(
    DataRequired
)

#getting the data for creating the drop-down-list
train=pd.read_csv("data/train.csv")
val=pd.read_csv("data/val.csv")

X_data=pd.concat([train,val],axis=0).drop(columns="price")

#Creating the form
class Inputform(FlaskForm):
    airline=SelectField(
        "Airline",
        choices=X_data["airline"].unique(),
        validators=[DataRequired()]
    )

    date_of_journey=DateField(
        "Date of journey",
        validators=[DataRequired()]
    )

    source=SelectField(
        "Source",
        choices=X_data["source"].unique(),
        validators=[DataRequired()]
    )

    destination=SelectField(
        "Destination",
        choices=X_data["destination"].unique(),
        validators=[DataRequired()]
    )

    dep_time=TimeField(
        "Departure Time",
        validators=[DataRequired()]
    )

    arrival_time=TimeField(
        "Arrival Time",
        validators=[DataRequired()]
    )

    duration=IntegerField(
        "Duration",
        validators=[DataRequired()]
    )

    total_stops=IntegerField(
        "Total stops",
        validators=[DataRequired()]
    )

    additional_info=SelectField(
        "Additional Info",
        choices=X_data["additional_info"].unique(),
        validators=[DataRequired()]
    )

    submit=SubmitField(
        "Predict"
    )