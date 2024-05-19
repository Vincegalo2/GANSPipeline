import pandas as pd
import requests   
from con_aws_to_sql import aws_pass # personal password!
from datetime import datetime, date, timedelta
from pytz import timezone, utc
from keys import API_key_aerodata, mySQL_pass # personal passwords!

# Database connection details for local and AWS
schema = "gans"
host = "localhost"
user = "root"
password = mySQL_pass
port = 3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

# AWS RDS MySQL connection details
host = 'wbs-project4-db.c1iajchyyr27.eu-north-1.rds.amazonaws.com'
username = 'admin'
password = aws_pass
con = f'mysql+pymysql://{username}:{password}@{host}:{port}/{schema}'

# Read airport ICAOs from the database
airport_icaos = pd.read_sql("cities_airports", con=con)
list_icao = airport_icaos['airport_icao'].tolist()

def flights(list_icao):
    """
    Fetches flight information for a list of airport ICAOs.
    
    Args:
    list_icao (list): List of airport ICAO codes.
    
    Returns:
    pd.DataFrame: DataFrame containing flight information.
    """
    today = datetime.now().astimezone(timezone('Europe/Berlin')).date()
    tomorrow = today + timedelta(days=1)
    
    # Initialize lists to store flight information
    arr_airport_icao = []
    dep_airport_icao = []
    dep_airport_name = []
    arr_flight_schtime = []
    arr_flight_revtime = []
    arr_flight_number = []
    arr_flight_status = []
    arr_flight_model = []
    arr_flight_name = []

    # Iterate over each ICAO code to fetch flight data
    for icao in list_icao:
        url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T08:00/{tomorrow}T19:59"
        querystring = {
            "withLeg": "false",
            "direction": "Arrival",
            "withCancelled": "false",
            "withCargo": "true",
            "withPrivate": "true",
            "withLocation": "false"
        }
        headers = {
            "X-RapidAPI-Key": API_key_aerodata,
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            flight_info = response.json()
            for i in range(len(flight_info['arrivals'])):
                try:
                    aircraft = flight_info['arrivals'][i]['aircraft']['model']
                    arr_flight_model.append(aircraft)
                except KeyError:
                    arr_flight_model.append(None)
                try:
                    arrival_icao = flight_info['arrivals'][i]['movement']['airport']['icao']
                    dep_airport_icao.append(arrival_icao)
                except KeyError:
                    dep_airport_icao.append(None)
                arr_airport_icao.append(icao)
                dep_airport_name.append(flight_info['arrivals'][i]['movement']['airport']['name'])
                scheduled_time_local = flight_info['arrivals'][i]['movement']['scheduledTime']['local']
                scheduled_time = datetime.strptime(scheduled_time_local, '%Y-%m-%d %H:%M%z')
                scheduled_time_utc = scheduled_time.astimezone(utc).replace(tzinfo=None)
                arr_flight_schtime.append(scheduled_time_utc)
                arr_flight_number.append(flight_info['arrivals'][i]['number'])
                arr_flight_status.append(flight_info['arrivals'][i]['status'])
                arr_flight_name.append(flight_info['arrivals'][i]['airline']['name'])
        else:
            print(f'No arrivals found for ICAO: {icao}')
    
    # Create DataFrame from collected flight data
    arr_columns = [
        'airport_icao',
        'departure_airport_icao',
        'departure_airport_name',
        'scheduled_time',
        'revised_time',
        'flight_number',
        'flight_status',
        'aircraft_used',
        'airline_name'
    ]
    return pd.DataFrame(list(zip(
        arr_airport_icao,
        dep_airport_icao,
        dep_airport_name,
        arr_flight_schtime,
        arr_flight_revtime,
        arr_flight_number,
        arr_flight_status,
        arr_flight_model,
        arr_flight_name
    )), columns=arr_columns)

# Fetch flight data for the list of ICAO codes
flights(list_icao)