import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,timedelta




def api_inputs():
    try:
        latitude = float(input("What is the latitude?(00.00 format)  "))
        longitude = float(input("What is the longitude?(00.00 format) "))
        start_date = input("What is the start date?(YYYY-MM-DD format) ")
        end_date = input("What is the end date?(YYYY-MM-DD format) ")

    except ValueError:
        print("Please enter the co-ordinates in the correct float format.")
        return None

    try:
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")

    except ValueError:
        print("Please enter dates in the correct format.")
        return None

    if start_date_dt>end_date_dt:
        print("Please ensure your start date is before the end date.")
        return None

    return (latitude, longitude, start_date, end_date)


def api_call(latitude, longitude, start_date, end_date):
    url = (f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min")
    try:
        api_response = requests.get(url)
        api_response.raise_for_status()
        json_ = api_response.json()
        daily_data = json_["daily"]

    except requests.exceptions.ConnectionError:
        print("Connection Error, please try again later.")
        return None

    except requests.exceptions.HTTPError:
        print("HTTP Error, please recheck your date inputs.")
        return None

    except requests.exceptions.JSONDecodeError:
        print("Sorry, we didn't recieve a valid JSON response.")
        return None

    except KeyError:
        print("Sorry, we couldn't find a 'daily' key within the DataFrame.")
        return None

    return daily_data

def dataframe(daily_data):

    weather_df = pd.DataFrame({
        "date" : daily_data["time"],
        "max temperature" : daily_data["temperature_2m_max"],
        "min temperature" : daily_data["temperature_2m_min"]
    })
    weather_df["date"] = pd.to_datetime(weather_df["date"])
    return weather_df

def calculations(weather_df):
    max_temp = weather_df["max temperature"].max()
    min_temp = weather_df["min temperature"].min()
    avg_max_temp = weather_df["max temperature"].mean()
    avg_min_temp = weather_df["min temperature"].mean()
    daily_avg_temp = weather_df[["max temperature","min temperature"]].mean(axis=1)
    weather_df["daily_avg_temp"] = (daily_avg_temp)
    avg_temp = weather_df["daily_avg_temp"].mean()
    index_for_hottest = weather_df["max temperature"].idxmax()
    hottest_date = weather_df.loc[index_for_hottest, "date"]
    index_for_coldest = weather_df["min temperature"].idxmin()
    coldest_date = weather_df.loc[index_for_coldest, "date"]
    temp_range = weather_df["max temperature"] - weather_df["min temperature"]
    weather_df["Daily Temperature range"] = temp_range
    temp_range_avg = weather_df["Daily Temperature range"].mean()
    return max_temp, min_temp, avg_max_temp, avg_min_temp, avg_temp, hottest_date, coldest_date, temp_range_avg



def hot_and_cold_graph(weather_df):
    plt.figure(figsize = (15,10))
    plt.plot(weather_df["date"],weather_df["max temperature"], label = "max temp")
    plt.plot(weather_df["date"],weather_df["min temperature"], label = "min temp")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("max and min temp weather report")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/max_min_report.png")
    plt.show()
   

def daily_avg_graph(weather_df):
    plt.figure(figsize=(15,10))
    plt.plot(weather_df["date"],weather_df["daily_avg_temp"], label = "daily avg temp")
    plt.xlabel("Date")
    plt.ylabel("Avg Temperature (°C)")
    plt.title("daily average temperature")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/avg_daily_temp.png")
    plt.show()
   