from datetime import datetime

# A simple structure to store weather data throughout the day
daily_weather_data = []

# Function to add weather data to daily records
def add_weather_data(weather):
    daily_weather_data.append(weather)

# Function to calculate daily weather summary
def calculate_daily_summary():
    if not daily_weather_data:
        return None
    
    temperatures = [entry['temperature'] for entry in daily_weather_data]
    conditions = [entry['main'] for entry in daily_weather_data]
    
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    dominant_condition = max(set(conditions), key=conditions.count)
    
    return {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'average_temperature': avg_temp,
        'max_temperature': max_temp,
        'min_temperature': min_temp,
        'dominant_condition': dominant_condition
    }

# Example usage
if __name__ == '__main__':
    # Simulate adding weather data throughout the day
    add_weather_data({'temperature': 25, 'main': 'Clear'})
    add_weather_data({'temperature': 27, 'main': 'Clear'})
    add_weather_data({'temperature': 22, 'main': 'Rain'})
    
    summary = calculate_daily_summary()
    if summary:
        print(summary)
