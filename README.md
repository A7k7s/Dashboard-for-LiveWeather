🌦 Live Weather Dashboard

A real-time weather dashboard built with Python, Streamlit, Pandas, and Matplotlib, fetching data from the OpenWeatherMap API.
It displays current weather, 5-day daily averages, and a temperature trend chart in a user-friendly web interface.

🔹 Features

Fetches live weather data for any city worldwide.

Displays current weather:

Temperature 🌡

Feels Like 🌡

Humidity 💧

Wind Speed 💨

Weather description ☁

Shows 5-day forecast with daily averages only.

Visualizes temperature trend using a line chart.

Interactive web dashboard built with Streamlit.

Secure API key management using Streamlit Secrets / .env.

🔹 Tech Stack

Python 3

Streamlit – interactive web app

Pandas – data processing

Matplotlib – data visualization

Requests – API calls

Python-dotenv – environment variables (local testing)

OpenWeatherMap API – weather data

🔹 How to Run Locally

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Create and activate virtual environment:

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create a .env file in project root and add your API key:

OPENWEATHER_API_KEY=your_actual_api_key_here


Run the app:

streamlit run app.py

🔹 Live Demo

Access the live dashboard here:
🌐 https://dashboard-for-liveweather-kedhwvi8wwnt5kythx5uej.streamlit.app/

🔹 Future Enhancements

Add multiple city comparison.

Show weather icons/images dynamically.

Include additional metrics like precipitation, UV index, sunrise/sunset.

Improve UI/UX with custom styling.

🔹 Author

Akshayaa Panneerselvam

GitHub: A7k7s
