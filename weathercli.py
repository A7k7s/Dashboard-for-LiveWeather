import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# Console for pretty CLI output
console = Console()

# Base URLs
current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

# Get city from user
city = input("Enter city name: ")

# Parameters
params = {"q": city, "appid": api_key, "units": "metric"}

# 1️⃣ Fetch current weather
response = requests.get(current_weather_url, params=params)

if response.status_code == 200:
    data = response.json()

    table = Table(title=f"Current Weather in {city.title()}")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Temperature", f"{data['main']['temp']}°C")
    table.add_row("Feels Like", f"{data['main']['feels_like']}°C")
    table.add_row("Weather", data['weather'][0]['description'].title())
    table.add_row("Humidity", f"{data['main']['humidity']}%")
    table.add_row("Wind Speed", f"{data['wind']['speed']} m/s")

    console.print(table)

else:
    console.print("[red]City not found. Please check the name and try again.[/red]")
    exit()

# 2️⃣ Fetch 5-day forecast
forecast_response = requests.get(forecast_url, params=params)

if forecast_response.status_code == 200:
    forecast_data = forecast_response.json()

    # Extract date/time, temperature, humidity
    records = []
    for item in forecast_data["list"]:
        records.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"]
        })

    # Convert to DataFrame
    df = pd.DataFrame(records)
# Convert datetime column to actual datetime objects
df["datetime"] = pd.to_datetime(df["datetime"])

# Extract only the date
df["date"] = df["datetime"].dt.date

# Group by date to get daily averages
daily_forecast = df.groupby("date").agg({
    "temp": "mean",
    "humidity": "mean"
}).reset_index()

# Show simplified forecast table
forecast_table = Table(title=f"5-Day Forecast (Daily Avg) for {city.title()}")
forecast_table.add_column("Date", style="green")
forecast_table.add_column("Avg Temp (°C)", style="yellow")
forecast_table.add_column("Avg Humidity (%)", style="blue")

for _, row in daily_forecast.iterrows():
    forecast_table.add_row(str(row["date"]), f"{row['temp']:.1f}°C", f"{row['humidity']:.1f}%")

console.print(forecast_table)

# Plot simplified daily temperature trend
plt.figure(figsize=(8, 4))
plt.plot(daily_forecast["date"], daily_forecast["temp"], marker="o", color="b", label="Avg Temp (°C)")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"5-Day Avg Temperature Trend in {city.title()}")
plt.legend()
plt.tight_layout()
plt.show()
