import json
import pandas as pd
import requests
import os

def clean_weather_df(df):    
    """
    Cleans the weather DataFrame by converting specific columns to numeric and datetime types.
    
    Args:
    df (pd.DataFrame): DataFrame containing weather data.
    
    Returns:
    pd.DataFrame: Cleaned DataFrame.
    """
    numeric_columns = ['temp', 'rain_3_hours_past_mm', 'snow_3_hours_past_mm']
    datetime_columns = ['forecast_time', 'updated']

    # Convert specified columns to numeric type
    for measure in numeric_columns:
        df[measure] = pd.to_numeric(df[measure])
        
    # Convert specified columns to datetime type
    for dt in datetime_columns:
        df[dt] = pd.to_datetime(df[dt])
        
    print("The weather has been forecasted and cleaned!")
    return df
    
def get_weather(df):
    """
    Fetches weather forecast data for given locations in the DataFrame.
    
    Args:
    df (pd.DataFrame): DataFrame containing 'latitude' and 'longitude' columns for locations.
    
    Returns:
    pd.DataFrame: DataFrame containing weather forecast data for the specified locations.
    """
    key = os.environ["open_weather_API_key"]
    from datetime import datetime
    import pytz
    
    df_out = pd.DataFrame()  # Initialize an empty DataFrame to store the results

    # Iterate over each row in the input DataFrame
    for i, series in df.iterrows():
        parameters = {
            "lat": series["latitude"],
            "lon": series["longitude"],
            "appid": key,
            "units": "metric"
        }
        
        # API URL for fetching weather data
        url = f"https://api.openweathermap.org/data/2.5/forecast"
        weather = requests.get(url, params=parameters)
        
        # Check if the API request was successful
        if weather.status_code == 200:
            weather_json = weather.json()
            tz = pytz.timezone('Europe/Berlin')
            now = datetime.now().astimezone(tz)
            temp_dict = {}
            
            # Extract weather data for each forecast time
            temp_dict["city_id"] = [series.name for time in weather_json["list"]]
            temp_dict["forecast_time"] = [time.get("dt_txt") for time in weather_json["list"]]
            temp_dict["temp"] = [time["main"].get("temp") for time in weather_json["list"]]
            temp_dict["description"] = [time["weather"][0].get("description") for time in weather_json["list"]]
            temp_dict["rain_3_hours_past_mm"] = [time.get("rain", {'3h': 0.0})["3h"] for time in weather_json["list"]]
            temp_dict["snow_3_hours_past_mm"] = [time.get("snow", {'3h': 0.0})["3h"] for time in weather_json["list"]]
            temp_dict["updated"] = [now for time in weather_json["list"]]
            
            # Convert the dictionary to a DataFrame and clean it
            temp_df = pd.DataFrame(temp_dict).pipe(clean_weather_df)
            
            # Append the cleaned data to the output DataFrame
            df_out = pd.concat([df_out, temp_df])
        else:
            print(f"Error: no weather data for {series['city']}")
    
    return df_out