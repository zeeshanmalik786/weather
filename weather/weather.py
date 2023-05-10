from pyspark.sql.types import StringType, StructType, StructField, FloatType, DoubleType
import requests
import pandas as pd
from weather.config import config


class weather:
    def __init__(self):

        self.con = config()
        self.spark = self.con.spark

        self.column = [
            "City",
            "Longitude",
            "Latitude",
            "Temperature in Fahrenheit",
            "Temperature in Celsius",
            "precipitation",
            "Pressure",
            "Humidity",
            "Visibility",
            "Speed",
            "Date"]


    def __weather__(self, date, cities, type):
        result = pd.DataFrame(columns=self.column)
        for index, city in enumerate(cities):
            try:
                print(city)
                api_url = "https://api.openweathermap.org/data/2.5/weather?" + "q=" + str(city) + str(self.con.key)
                response = requests.get(api_url)
                output = response.json()
                result = result.append({"City": city,
                                        "Longitude": output['coord']['lon'],
                                        "Latitude": output['coord']['lat'],
                                        "Temperature in Fahrenheit": round((output['main']['temp'] - 273.15) * 9 / 5 + 32, 2),
                                        "Temperature in Celsius": round((output['main']['temp'] - 273.15), 2),
                                        "precipitation": output['weather'][0]['description'],
                                        "Pressure": output['main']['pressure'],
                                        "Humidity": output['main']['humidity'],
                                        "Visibility": output['visibility'],
                                        "Speed": output['wind']['speed'],
                                        "Date": str(date)}, ignore_index=True)
                print("Record: ", index)
            except:
                pass
        output = self.spark.createDataFrame(result, self.con.schema)
        self.spark.sql("DROP TABLE IF EXISTS default.weather")
        output.write.format("delta").saveAsTable("default.weather")
        if type=="daily":
            self.spark.sql("INSERT INTO cable_access_networks_performance.weather SELECT * from default.weather")
        else:
            self.spark.sql("INSERT INTO cable_access_networks_performance.weather_hourly SELECT * from default.weather")

        return True








