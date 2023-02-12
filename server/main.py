from datetime import datetime
from time import time
import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import numpy as np

from typing import Optional

from server.database import LocalDatabase
from original_files.main import load_model, MODEL_NAME
from server.helpers import generate_ocean_proximity_list

app = FastAPI()

templates = Jinja2Templates(directory="server/templates")
model = load_model(os.path.join("original_files", MODEL_NAME))
local_database = LocalDatabase()


@app.post('/get_form_params', response_class=HTMLResponse)
async def get_form_params(
    _request: Request,
    longitude: Optional[float] = Form(None),
    latitude: Optional[float] = Form(None),
    housing_median_age: Optional[float] = Form(None),
    total_rooms: Optional[int] = Form(None),
    total_bedrooms: Optional[int] = Form(None),
    population: Optional[int] = Form(None),
    households: Optional[int] = Form(None),
    median_income: Optional[float] = Form(None),
    ocean_proximity: Optional[str] = Form(None),
):
    if None in (longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                median_income, ocean_proximity):
        local_database.unsuccessful_prediction()
        return

    ocean_proximity_list = generate_ocean_proximity_list(ocean_proximity)
    data = np.array((longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                     median_income, *ocean_proximity_list))
    data = data.reshape(1, -1)

    predicted_price = model.predict(data)

    timestamp = datetime.fromtimestamp(time())
    str_timestamp = timestamp.strftime("%d-%m-%Y, %H:%M:%S")

    local_database.insert({
            "timestamp": str_timestamp,
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity,
            "predicted_price": predicted_price[0],
        }
    )


@app.get("/update_table", response_class=HTMLResponse)
async def display_last_prediction(request: Request):
    return templates.TemplateResponse(
        "table.html",
        {"request": request,
         "last_prediction": local_database.get_last_predicted_price(),
         "previous_predictions": local_database.get_all_values(),
         }
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    previous_predictions = local_database.get_all_values()
    local_database.reset_last()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "previous_predictions": previous_predictions}
    )
