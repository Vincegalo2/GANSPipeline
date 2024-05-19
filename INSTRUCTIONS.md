# GANSPipeline - Detailed Instructions

## Directory Structure

```plaintext
GANSPipeline/
├── notebooks/                    # Jupyter notebooks
│   ├── gans_flights.ipynb        # Notebook for flight data extraction and processing
│   ├── gans_forecast.ipynb       # Notebook for weather forecast data extraction and processing
├── scripts/                      # Python scripts
│   ├── gans_flights_clean_script.py  # Script for extracting and processing flight data
│   ├── gans_forecast_clean_script.py # Script for extracting and processing weather forecast data
│   ├── lambda_function.py            # AWS Lambda function for automation
│   ├── weather_functions.py          # Additional weather-related functions
├── sql/                          # SQL files
│   ├── gans_project.sql          # SQL script to create and populate database
├── diagram/                      # Directory for project diagrams
│   └── gans_diagram.png          # Database schema diagram
├── .gitignore                    # Git ignore file
├── README.md                     # Project overview
├── images/                       # Various pictures
└── requirements.txt              # Project dependencies

### Installations

1. Clone or download the repository from GitHub.
2. Set up your environment and install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your API keys and database credentials as environment variables:
   ```bash
   export OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   export AERODATABOX_API_KEY=your_aerodatabox_api_key
   export MYSQL_USER=your_mysql_user
   export MYSQL_PASSWORD=your_mysql_password
   export MYSQL_HOST=your_mysql_host
   export MYSQL_DB=your_mysql_database
   ```
4. Run the data extraction scripts:
   ```bash
   python scripts/gans_flights_clean_script.py
   python scripts/gans_forecast_clean_script.py
   ````

### Usage

1.	Set up your MySQL database using the script in the sql/ directory:
   ```sql
   -- Run this command in your MySQL Workbench
   SOURCE /path/to/sql/gans_project.sql;
   ````
2. Configure AWS Lambda functions and schedule them using AWS Eventbridge for real-time data updates (details to be added later).

### Contributing

Feel free to open issues or submit pull requests for improvements and new features.

### License

This project is licensed under the MIT License.

