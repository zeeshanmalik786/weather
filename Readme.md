<h2>Weather Data Daily Dump</h2>


<h2> Open Weather Map Data </h2>

We are providing highly recognisable weather products that make working with the weather data a way easier. We work with millions of developers around a clock and believe that these benefits might be suitable for most of applications, up to the complex enterprise systems.

A spectrum of ready-to-use weather products

Short-term and long-term forecasts, history and observation

Any location on the globe


Fields in API Response

coord
1. coord.lon 
   City geo location, longitude
2. coord.lat 
   City geo location, latitude

3. weather.id Weather condition id
4. weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
5. weather.description Weather condition within the group. You can get the output in your language. Learn more
6. weather.icon Weather icon id
base Internal parameter
main
7. main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
8. main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
9. main.humidity Humidity, %
10. main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
11. main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
12. main.sea_level Atmospheric pressure on the sea level, hPa
13. main.grnd_level Atmospheric pressure on the ground level, hPa
14. visibility Visibility, meter. The maximum value of the visibility is 10km
wind
15. wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
16. wind.deg Wind direction, degrees (meteorological)
17. wind.gust Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
clouds
18. clouds.all Cloudiness, %
rain
19. rain.1h (where available) Rain volume for the last 1 hour, mm
20. rain.3h (where available) Rain volume for the last 3 hours, mm
snow
21. snow.1h(where available) Snow volume for the last 1 hour, mm
22. snow.3h (where available)Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
23. sys.type Internal parameter
24. sys.id Internal parameter
25. sys.message Internal parameter
26. sys.country Country code (GB, JP etc.)
27. sys.sunrise Sunrise time, unix, UTC
28. sys.sunset Sunset time, unix, UTC


<h2> Sample API Response </h2>                          
<br>
{
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.48,
    "feels_like": 298.74,
    "temp_min": 297.56,
    "temp_max": 300.05,
    "pressure": 1015,
    "humidity": 64,
    "sea_level": 1015,
    "grnd_level": 933
  },
  "visibility": 10000,
  "wind": {
    "speed": 0.62,
    "deg": 349,
    "gust": 1.18
  },
  "rain": {
    "1h": 3.16
  },
  "clouds": {
    "all": 100
  },
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",
    "sunrise": 1661834187,
    "sunset": 1661882248
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
}                        

                        
