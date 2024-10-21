from flask import Flask, jsonify
from weather_data import fetch_weather
from weather_aggregator import add_weather_data, calculate_daily_summary
from alert_system import check_for_alert
from time import sleep

app = Flask(__name__)

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
TEMP_THRESHOLD = 35  # Set the threshold for triggering alerts

# Endpoint to return the daily weather summary
@app.route('/daily_summary', methods=['GET'])
def daily_summary():
    summary = calculate_daily_summary()
    if summary:
        return jsonify(summary)
    return jsonify({"error": "No data available for today."}), 404

# Function to fetch weather data, process it, and trigger alerts
def fetch_and_process_weather():
    while True:
        for city in CITIES:
            weather = fetch_weather(city)
            if weather:
                # Add weather data to the daily aggregator
                add_weather_data(weather)

                # Check if the temperature exceeds the threshold
                alert = check_for_alert(weather, TEMP_THRESHOLD)
                if alert:
                    print(alert)

        # Sleep for 5 minutes before fetching again
        sleep(300)

if __name__ == '__main__':
    fetch_and_process_weather()  # Start fetching and processing weather data
    app.run(debug=True)  # Run the Flask server
