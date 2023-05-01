<h2>Weather Data Daily Dump</h2>


<h2> Open Weather Map Data </h2>

We are providing highly recognisable weather products that make working with the weather data a way easier. We work with millions of developers around a clock and believe that these benefits might be suitable for most of applications, up to the complex enterprise systems.

A spectrum of ready-to-use weather products

Short-term and long-term forecasts, history and observation

Any location on the globe


Fields in API Response

<b>coord</b>
1. <b>coord.lon</b> 
   City geo location, longitude
2. <b>coord.lat</b> 
   City geo location, latitude

3. <b>weather.id</b> Weather condition id
4. <b>weather.main</b> Group of weather parameters (Rain, Snow, Extreme etc.)
5. <b>weather.description</b> Weather condition within the group. You can get the output in your language. Learn more
6. <b>weather.icon</b> Weather icon id
base Internal parameter
main
7. <b>main.temp</b> Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
8. <b>main.pressure</b> Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
9. <b>main.humidity</b> Humidity, %
10. <b>main.temp_min</b> Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
11. <b>main.temp_max</b> Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
12. <b>main.sea_level</b> Atmospheric pressure on the sea level, hPa
13. <b>main.grnd_level</b> Atmospheric pressure on the ground level, hPa
14. <b>visibility Visibility</b>, meter. The maximum value of the visibility is 10km
wind
15. <b>wind.speed</b> Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
16. <b>wind.deg</b> Wind direction, degrees (meteorological)
17. <b>wind.gust</b> Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
clouds
18. <b>clouds.all</b> Cloudiness, %
rain
19. <b>rain.1h</b> (where available) Rain volume for the last 1 hour, mm
20. <b>rain.3h</b> (where available) Rain volume for the last 3 hours, mm
snow
21. <b>snow.1h</b>(where available) Snow volume for the last 1 hour, mm
22. <b>snow.3h</b> (where available)Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
23. <b>sys.type</b> Internal parameter
24. <b>sys.id</b> Internal parameter
25. <b>sys.message</b> Internal parameter
26. <b>sys.country</b> Country code (GB, JP etc.)
27. <b>sys.sunrise</b> Sunrise time, unix, UTC
28. <b>sys.sunset</b> Sunset time, unix, UTC


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

                        
