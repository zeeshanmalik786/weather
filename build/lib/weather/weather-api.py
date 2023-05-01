import python_weather

class weather:

    async def __getweather__(self, city, date):

        async with python_weather.Client(format=python_weather.IMPERIAL) as client:
            weather = await client.get(city)
        return {"Date":date,
                "Temperature in Celsius":round((weather.current.temperature - 32) * 5/9,2),
                "Temperature in Fahrenheit":weather.current.temperature,
                "City Name":city}
