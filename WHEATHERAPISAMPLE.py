import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "SAMPLE_API_KEY"  


def get_weather_data(date):
    url = f"{API_BASE_URL}?q={date}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "list" in data and data["list"]:
            temperature = data["list"][0]["main"]["temp"]
            return temperature
        else:
            print(f"Temperature data not found for {date}.")
            return None
    else:
        print("Failed to fetch weather data.")
        return None


def get_wind_speed_data(date):
    url = f"{API_BASE_URL}?q={date}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "list" in data and data["list"]:
            wind_speed = data["list"][0]["wind"]["speed"]
            return wind_speed
        else:
            print(f"Wind speed data not found for {date}.")
            return None
    else:
        print("Failed to fetch wind speed data.")
        return None


def get_pressure_data(date):
    url = f"{API_BASE_URL}?q={date}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "list" in data and data["list"]:
            pressure = data["list"][0]["main"]["pressure"]
            return pressure
        else:
            print(f"Pressure data not found for {date}.")
            return None
    else:
        print("Failed to fetch pressure data.")
        return None


def main():
    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            city_name = input("Enter the city name: ")
            temperature = get_weather_data(city_name)
            if temperature is not None:
                print(f"Temperature on {date} in {city_name}: {temperature}°C")

        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            city_name = input("Enter the city name: ")
            wind_speed = get_wind_speed_data(city_name)
            if wind_speed is not None:
                print(f"Wind Speed on {date} in {city_name}: {wind_speed} m/s")

        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            city_name = input("Enter the city name: ")
            pressure = get_pressure_data(city_name)
            if pressure is not None:
                print(f"Pressure on {date} in {city_name}: {pressure} hPa")

        elif option == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
