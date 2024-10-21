# Function to check if an alert should be triggered based on thresholds
def check_for_alert(weather, temp_threshold):
    if weather['temperature'] > temp_threshold:
        return f"ALERT: Temperature in {weather['city']} exceeded {temp_threshold}°C"
    return None

# Example usage
if __name__ == '__main__':
    temp_threshold = 35  # Example threshold
    weather = {'city': 'Delhi', 'temperature': 36, 'main': 'Clear'}
    
    alert = check_for_alert(weather, temp_threshold)
    if alert:
        print(alert)
