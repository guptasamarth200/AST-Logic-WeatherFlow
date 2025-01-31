# Zeotap Intern Assignment
🌟 Overview

Welcome to the Zeotap Rule Engine & Weather Monitoring System – a powerful yet simple solution designed to:

Rule Engine with AST – Dynamically evaluate user eligibility with customizable rules using an Abstract Syntax Tree (AST).

Real-Time Weather Monitoring System – Fetch, analyze, and alert weather conditions with smart rollups and aggregates.

🔥 Key Features

🛠 Rule Engine with AST

✅ Define rules using an Abstract Syntax Tree (AST).
✅ Create, modify, and combine rules dynamically.
✅ Evaluate user eligibility with structured conditions.
✅ Store and manage rules efficiently in a database.
✅ Error handling for incorrect inputs to keep things smooth.

🌤 Real-Time Weather Monitoring System

✅ Fetches live weather data from OpenWeatherMap API at your chosen intervals.
✅ Converts temperature seamlessly from Kelvin to Celsius.
✅ Aggregates daily weather stats (average, max, min, dominant condition).
✅ Custom alerts for extreme conditions – no more weather surprises!
✅ Visualize weather trends with engaging charts.

🚀 API Endpoints

📌 Rule Engine API

🔹 POST /create_rule – Convert rule string into an AST.
🔹 POST /combine_rules – Merge multiple AST-based rules into one.
🔹 POST /evaluate_rule – Check user eligibility against a rule AST.

📌 Weather Monitoring API

🔹 GET /fetch_weather – Fetches current weather data.
🔹 GET /daily_summary – Provides summarized daily weather insights.
🔹 POST /set_alert – Set alerts for extreme weather conditions.

💡 Tech Stack

🔹 Backend: Python (Flask/FastAPI)
🔹 Database: PostgreSQL / SQLite
🔹 Data Processing: Pandas, NumPy
🔹 API Calls: Requests
🔹 Visualization: Matplotlib / Dash / Streamlit

This repository contains two independent projects as part of the Zeotap Intern Assignment:

1. **[Rule Engine with AST](https://github.com/guptasamarth200/zeotap-intern-assignment/tree/rule-engine)**: A rule engine that dynamically creates, combines, and evaluates rules using an Abstract Syntax Tree (AST).
2. **[Weather Data Processing System](https://github.com/guptasamarth200/zeotap-intern-assignment/tree/weather-processing)**: A real-time weather monitoring system that fetches and processes data from OpenWeatherMap.

- **Rule Engine**: The Rule Engine allows users to create custom eligibility rules and combine them using logical operations (`AND`, `OR`). The engine processes these rules based on input data, evaluating whether users meet the specified conditions. It's powered by an Abstract Syntax Tree (AST) to parse and execute complex rule structures.

- **Weather Processing System**: The Weather Data Processing System retrieves real-time weather data from the OpenWeatherMap API and processes it to generate daily summaries. It also triggers alerts if weather conditions, such as temperature thresholds, exceed predefined limits.

## Project 1: Rule Engine with AST
🎯 Installation & Setup  
### Setup Instructions

1. Clone the repository and navigate to the `rule-engine` branch:
    ```bash
    git clone https://github.com/guptasamarth200/zeotap-intern-assignment.git
    cd zeotap-intern-assignment
    git checkout rule-engine
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the necessary dependencies:
    ```bash
    pip install Flask
    ```

4. Run the Flask server:
    ```bash
    python app.py
    ```

5. Open `index.html` in your browser to interact with the Rule Engine.

---

## Project 2: Weather Data Processing System
🎯 Installation & Setup

### Setup Instructions

1. Navigate to the `weather-processing` branch:
    ```bash
    git checkout weather-processing
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the necessary dependencies:
    ```bash
    pip install Flask requests
    ```

4. Obtain an API key from OpenWeatherMap, and add it to the `weather_data.py` file:
    ```python
    API_KEY = 'your_openweather_api_key_here'
    ```

5. Run the Flask server:
    ```bash
    python main.py
    ```

6. Open `weather.html` in your browser to view real-time weather summaries and alerts.

---

## Dependencies

- **Python 3.x**
- **Flask** for creating web servers.
- **Requests** for API calls (used in the weather processing system).
- **OpenWeatherMap API** for real-time weather data.

---

## Testing

### Rule Engine:
- Test the rule creation using the `create_rule` API.
- Test rule combinations using the `combine_rules` API.
- Evaluate rules with test user data using the `evaluate_rule` API.

### Weather Processing:
- Test real-time weather data fetching.
- Simulate multiple weather data updates to generate daily summaries.
- Verify that weather alerts trigger when thresholds are exceeded.

---
Made with ❤️ for innovation and problem-solving. Let’s build something amazing! 🚀

