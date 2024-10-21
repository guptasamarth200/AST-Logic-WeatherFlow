import requests

# OpenWeatherMap API URL
API_KEY = '451e295e52e5ded690e0d5050a3a27e9' 
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to fetch weather data for a specific city
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Fetch temperature in Celsius
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'main': data['weather'][0]['main'],
            'dt': data['dt']  # Timestamp
        }
    else:
        print(f"Failed to fetch weather data for {city}: {response.status_code}")
        return None

# Example usage
if __name__ == '__main__':
    city = 'Delhi'
    weather = fetch_weather(city)
    if weather:
        print(weather)
