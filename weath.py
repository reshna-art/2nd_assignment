import requests

def fetch_weather_data(city, api_key):
    """
    Fetch weather data for a given city from the OpenWeatherMap API and display the temperature.

    Args:
        city (str): The name of the city to fetch weather data for.
        api_key (str): Your API key for the OpenWeatherMap API.
    """
    # Base URL for the OpenWeatherMap API
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Get temperature in Celsius
    }

    try:
        # Send the GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the JSON response
        data = response.json()

        # Extract and display the temperature
        temperature = data["main"]["temp"]
        print(f"The current temperature in {city} is {temperature}°C.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
    except KeyError:
        print("Error: Unable to fetch temperature data. Please check the city name and API key.")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
    fetch_weather_data("London", "your_api_key_here")
    
