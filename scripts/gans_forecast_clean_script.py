import pandas as pd
import requests
from keys import API_key_openweather

# Database connection details for local and AWS
schema = "gans"
host = "localhost"
user = "root"
password = "mySQL_pass"
port = 3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

# AWS RDS MySQL connection details
host = 'wbs-project4-db.c1iajchyyr27.eu-north-1.rds.amazonaws.com'
username = 'admin'
password = 'aws_pass' # add your personal password
con = f'mysql+pymysql://{username}:{password}@{host}:{port}/{schema}'

# List of cities to fetch data for
cities = ['Berlin', 'Munich', 'Frankfurt', 'London', 'Copenhagen']

# Lists to store city data
name = []
latitude = []
longitude = []
country = []

# Fetch geographical data for each city
for city in cities:
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_key_openweather}')
    city_data = response.json()[0]
    name.append(city_data['name'])
    latitude.append(city_data['lat'])
    longitude.append(city_data['lon'])
    country.append(city_data['country'])

# Create DataFrame for city location data
location_data_per_city = pd.DataFrame(list(zip(name, country, latitude, longitude)), columns=['city_name', 'country_code', 'latitude', 'longitude'])

# Save city location data to the database
location_data_per_city.to_sql("cities", if_exists="append", con=con, index=False)

# Read city data from the database
cities = pd.read_sql("cities", con=con)

def forecast(cities):
    """
    Fetches 5-day weather forecast for given cities.
    
    Args:
    cities (pd.DataFrame): DataFrame containing city data with latitude and longitude.
    
    Returns:
    pd.DataFrame: DataFrame containing weather forecast information.
    """
    city_id = []
    temp = []
    temp_min = []
    temp_max = []
    humidity = []
    main_weather = []
    description = []
    wind_speed = []
    visibility = []
    datetime = []

    # Fetch weather forecast for each city
    for i, row in cities.iterrows():
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={row["latitude"]}&lon={row["longitude"]}&appid={API_key_openweather}')
        weather_data = response.json()

        for time in weather_data['list'][:8]:  # Limit to the first 8 timestamps (next 24 hours)
            city_id.append(row['city_id'])
            temp.append(time['main']['temp'])
            temp_min.append(time['main']['temp_min'])
            temp_max.append(time['main']['temp_max'])
            humidity.append(time['main']['humidity'])
            main_weather.append(time['weather'][0]['main'])
            description.append(time['weather'][0]['description'])
            wind_speed.append(time['wind']['speed'])
            visibility.append(time['visibility'])
            datetime.append(time['dt_txt'])

    # Create DataFrame from collected forecast data
    return pd.DataFrame(list(zip(city_id, temp, temp_min, temp_max, humidity, main_weather, description, wind_speed, visibility, datetime)),
                        columns=['city_id', 'temperature', 'min', 'max', 'humidity', 'weather', 'description', 'wind_speed', 'visibility', 'forecast_time'])

# Fetch and save forecast data
forecast_data = forecast(cities)
forecast_data.to_sql('forecast', if_exists='append', con=con, index=False)