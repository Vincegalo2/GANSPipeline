import json
import pandas as pd
import os
import sqlalchemy
import weather_functions

def lambda_handler(event, context):
    """
    AWS Lambda function to fetch weather data for a list of cities and store it in a database.
    
    Args:
    event (dict): Event data passed by the Lambda trigger.
    context (object): Runtime information provided by AWS Lambda.
    
    Returns:
    dict: Response object containing status code and a message.
    """
    
    # Fetch database connection string from environment variables
    con = os.environ["con"]
    
    # Read cities data from the database
    cities = pd.read_sql("cities", con=con, index_col="id")
    
    # Fetch weather data for the cities
    weather = weather_functions.get_weather(cities)
    
    # Append the fetched weather data to the weather table in the database
    weather.to_sql("weather", if_exists="append", con=con, index=False)
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }