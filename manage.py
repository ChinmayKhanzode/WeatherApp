import requests

def get_city_coordinates(city_name):
    base_url = "https://geocoding-api.open-meteo.com/v1/search?name="+city_name+"&count=1&language=en&format=json"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        try:
            return(data['results'][0])
        except:
            return(None)
    else:
        print(f"${city_name} does not exist")

def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "forecast_days":"1",
        "latitude":latitude,
        "longitude":longitude,
        "timezone":"GMT",
        "current":"temperature_2m,relative_humidity_2m,is_day,precipitation,rain,showers,weather_code,wind_speed_10m"}
    
    response = requests.get(base_url,params=params)
    data = response.json()

    if response.status_code == 200:
        print(str(data['current']['temperature_2m'])+" °C")
        return(str(data['current']['temperature_2m'])+" °C")
    else:
        print(f"Error: {data['message']['temperature_2m']}")


def main(city_name):
    final_weather_detail = ""
    city_data = get_city_coordinates(city_name)
    if(city_data==None):
        final_weather_detail = (f"${city_name} city does not exist")
    else:
        final_weather_detail =  "Temprature in "+city_data["name"]+","+city_data["admin1"]+","+city_data["country"]+ " is : "
        final_weather_detail+=get_weather(city_data["latitude"],city_data["longitude"])
    return final_weather_detail

