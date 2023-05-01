from weather.weather import weather
from datetime import datetime


def main(cities, today):

    print("Current Date of Run", today)

    start = datetime.now()
    print("Weather start time", start)

    weath = weather()

    status =  weath.__weather__(today, cities)

    if status is True:
        print("Job 1 Done")
    else:
        print("Job 1 crashed")

    print("total time", datetime.now() - start)




def run(cities, today):

    main(cities, today)