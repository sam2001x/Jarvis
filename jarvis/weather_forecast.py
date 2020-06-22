import requests,json

def weather():
    api_key = # enter your api key here.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "udaipur"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temp = y["temp"]
        # Converting kelvin into degree celcius
        C = current_temp - 273.15
        curremt_pres = y["pressure"]
        current_humidity = y["humidity"]

        return(f"temperature  is {C:.2f} °C\natmospheric tempersture (in hPa unit) = {str(curremt_pres)}\nhumidty = {str(current_humidity)} %")

    else:
        return("city not found")
