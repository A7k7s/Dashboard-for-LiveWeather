import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# API URLs
current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

st.title("🌦 Live Weather Dashboard")

# Input city
city = st.text_input("Enter city name:", "London")

if st.button("Get Weather"):
    params = {"q": city, "appid": api_key, "units": "metric"}

    # Current weather
    response = requests.get(current_weather_url, params=params)
    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Current Weather in {city.title()}")
        st.write(f"🌡 Temperature: {data['main']['temp']}°C")
        st.write(f"🤔 Feels Like: {data['main']['feels_like']}°C")
        st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")

    # Forecast
    forecast_response = requests.get(forecast_url, params=params)
    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()

        # Extract forecast
        records = []
        for item in forecast_data["list"]:
            records.append({
                "datetime": item["dt_txt"],
                "temp": item["main"]["temp"],
                "humidity": item["main"]["humidity"]
            })

        df = pd.DataFrame(records)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.date

        # Daily averages
        daily_forecast = df.groupby("date").agg({
            "temp": "mean",
            "humidity": "mean"
        }).reset_index()

        st.subheader(f"📅 5-Day Forecast for {city.title()}")
        st.dataframe(daily_forecast)

        # Chart
        fig, ax = plt.subplots()
        ax.plot(daily_forecast["date"], daily_forecast["temp"], marker="o", color="b", label="Avg Temp (°C)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        ax.set_title(f"5-Day Avg Temperature Trend in {city.title()}")
        ax.legend()
        st.pyplot(fig)
