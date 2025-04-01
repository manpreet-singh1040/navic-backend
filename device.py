import requests
import time

# Define the device ID and the URL of the update endpoint
device_id = "NAV-001"
url = f"http://localhost:8080/api/devices/{device_id}/location"

# Starting location (somewhere in India)
start_location = {
    "lat": 28.6139,  # Latitude for New Delhi
    "lng": 77.2090   # Longitude for New Delhi
}

# Function to simulate walking by updating the location in small increments
def simulate_walking(location, step_size=0.0001):
    # Update latitude and longitude by a small step size
    location["lat"] += step_size
    location["lng"] += step_size
    return location

# Continuously update the location every second
current_location = start_location
while True:
    current_location = simulate_walking(current_location)
    response = requests.put(url, json=current_location)

    if response.status_code == 200:
        print(f"Location updated successfully: {current_location}")
    else:
        print(f"Failed to update location: {response.status_code} - {response.text}")

    time.sleep(1)
