import python_weather
import asyncio
import os
import pandas as pd
from datetime import date
import requests


def getweather():
    try:
        cities_df = pd.read_excel('canadacities.xlsx')
        cities = cities_df["city"]
        current_date = date.today()
        column=[
            "City",
            "Longitude",
            "Latitude",
            "Temperature in Fahrenheit",
            "Temperature in Celsius",
            "Description",
            "Pressure",
            "Humidity",
            "Visibility",
            "Speed",
            "Date"]
        result = pd.DataFrame(columns=column)
        for index,city in enumerate(cities):
            print(city)
            api_url = "https://api.openweathermap.org/data/2.5/weather?" + "q=" + str(city) + ",CA&APPID=2a2f1e754c02588897a5b262265e9353"
            response=requests.get(api_url)
            output=response.json()
            result = result.append({"City": city,
                                "Longitude":output['coord']['lon'],
                                "Latitude":output['coord']['lat'],
                                "Temperature in Fahrenheit": round((output['main']['temp'] - 273.15) * 9 / 5 + 32, 2),
                                "Temperature in Celsius": round((output['main']['temp'] - 273.15), 2),
                                "Description":output['weather'][0]['description'],
                                "Pressure":output['main']['pressure'],
                                "Humidity":output['main']['humidity'],
                                "Visibility":output['visibility'],
                                "Speed":output['wind']['speed'],
                                "Date": current_date}, ignore_index=True)

            print("Record: ",index)
            print(result.head())
    except:
        pass

# async def getweather():
#     # declare the client. format defaults to the metric system (celcius, km/h, etc.)
#     cities_df = pd.read_excel('canadacities.xlsx')
#     cities = cities_df["city"]
#     column=["Date","Temperature in Celsius","Temperature in Fahrenheit", "City Name"]
#     today = date.today()
#     result = pd.DataFrame(columns=column)
#
#     for index,city in enumerate(cities):
#
#         async with python_weather.Client(format=python_weather.IMPERIAL) as client:
#
#             # fetch a weather forecast from a city
#             weather = await client.get(city)
#             result = result.append({"Date":today,
#                                     "Temperature in Celsius":round((weather.current.temperature - 32) * 5/9,2),
#                                     "Temperature in Fahrenheit":weather.current.temperature,
#                                     "City Name":city}, ignore_index=True)
#             print("Record:",index)
#     print(result.head())



    #
    #     # # get the weather forecast for a few days
    #     for forecast in weather.forecasts:
    #         print(forecast.date, forecast.astronomy, forecast.temperature)
    #     #
    #     #     # hourly forecasts
    #     #     for hourly in forecast.hourly:
    #     #         print(f' --> {hourly!r}')


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    getweather()
    # if os.name == "nt":
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #
    # asyncio.run(getweather())