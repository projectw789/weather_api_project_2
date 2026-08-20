import requests
import pandas as pd
# import matplotlib as mpl
# from datetime import datetime, timedelta

# my bae in ilford  51.5577 &  0.0728

latitude = float(input("whats the latitude?(00.00 format)  "))
longitude = float(input("whats the longitude?(00.00 format) "))
start_date = input("Whats the start date?(YYYY-MM-DD format) ")
end_date = input("Whats the end date?(YYYY-MM-DD format) ")

url = (f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min")

api_response = requests.get(url)

json_string = api_response.json()

daily_data = json_string["daily"]

# print(daily_data)

# print()

weather_df = pd.DataFrame({
    "date" : daily_data["time"],
    "max temperature" : daily_data["temperature_2m_max"],
    "min temperature" : daily_data["temperature_2m_min"]
})

weather_df["date"] = pd.to_datetime(weather_df["date"])

print(weather_df)