from weather import Weather, Unit
import click


def weather_temperature_by_location(unit, city):
    weather, temperature_format_unit = weather_temperature_format(unit)
    city_weather_info = weather.lookup_by_location(city)
    forecasts = city_weather_info.forecast
    return forecasts, temperature_format_unit


def print_weather_today(city, condition, low_temperature, high_temperature, unit):
    print(f"The weather in {city} today is {condition} "
          f"with temperatures trailing from {low_temperature}-{high_temperature} "
          f"{unit}")


def print_weather_date(date, condition, low_temperature, high_temperature, unit):
    print(f"{date} {condition} with temperatures trailing "
          f"from {low_temperature}-{high_temperature} "
          f"{unit}")


def weather_forecast_for_next_days(forecast):
    forecast_format = forecast.split('+')
    if len(forecast_format) == 1:
        return 1
    number_of_days = int(forecast_format[1])+1
    if number_of_days > 10:
        print("Weather forecast is only for the next 9 days, Out of range")
        exit(1)
    return number_of_days


def weather_temperature_format(unit):
    if unit == "c":
        weather = Weather(unit=Unit.CELSIUS)
        temperature_format_unit = "Celsius"
    elif unit == "f":
        weather = Weather(unit=Unit.FAHRENHEIT)
        temperature_format_unit = "Fahrenheit"
    return weather, temperature_format_unit


@click.command()
@click.option('--city')
@click.option('-c', is_flag=True)
@click.option('-f', is_flag=True)
@click.option('--forecast')
def main(city, c, f, forecast):
    if c and f:
        print('Incorrect usage, use one of -c/-f.')
        exit(1)
    unit = 'c'
    if f:
        unit = 'f'
    number_of_days = weather_forecast_for_next_days(forecast)
    forecasts, temperature_unit = weather_temperature_by_location(unit, city)
    print_weather_today(city, forecasts[0].text, forecasts[0].low, forecasts[0].high, temperature_unit)
    if number_of_days > 1:
        print()
        print(f'Forecast for the next {number_of_days-1} days:')
        print()
        for forecast in forecasts[1:number_of_days]:
            print_weather_date(forecast.date, forecast.text, forecast.low, forecast.high, temperature_unit)



if __name__ == '__main__':
    main()


