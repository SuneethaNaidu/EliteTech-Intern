import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Config
API_KEY = "9c034daa8cec67966dce937d5b1c4d8d"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch and validate data
try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    if data.get("cod") != "200":
        raise ValueError(data.get("message"))
except Exception as e:
    print("Error:", e)
    exit()

# Extract and process data
df = pd.DataFrame([{
    "datetime": datetime.fromtimestamp(item["dt"]),
    "temp": item["main"]["temp"],
    "humidity": item["main"]["humidity"]
} for item in data["list"]])

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="datetime", y="temp", label="Temperature (°C)", marker="o")
sns.lineplot(data=df, x="datetime", y="humidity", label="Humidity (%)", marker="x")
plt.title(f"5-Day Forecast: {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
