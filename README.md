# GANSPipeline

This repository contains the code for a comprehensive data engineering project named GANSPipeline. The project aims to create a robust data pipeline that extracts, processes, and stores real-time flight and weather information into a MySQL database on the cloud. The pipeline leverages multiple technologies, including Python, SQL, and AWS, to ensure data flow automation and real-time availability for analysis.

![Pipeline Overview](images/pipeline_overview.png)

### Key Features

- **Real-time Data Extraction**: Utilizes APIs to fetch real-time weather and flight data.
- **Automated Data Storage**: Stores extracted data in a cloud-based MySQL database.
- **Serverless Pipeline Automation**: Employs AWS Lambda and Eventbridge for automated data flow.

### Technologies Used

- **Python**: For scripting and data processing.
- **MySQL**: For database storage.
- **AWS Lambda and Eventbridge**: For serverless pipeline automation.
- **APIs**: For accessing weather (OpenWeatherMap) and flight data (Aerodatabox).

### How It Works

1. **Extract Data**: Scripts fetch real-time data from weather and flight APIs.
2. **Process Data**: Data is processed and cleaned using Python scripts.
3. **Store Data**: Processed data is stored in a MySQL database.
4. **Automate Pipeline**: AWS Lambda functions are used to automate the data pipeline, scheduled by AWS Eventbridge.

### Setup Instructions

For detailed installation instructions, directory structure, and usage, please refer to the [INSTRUCTIONS.md](INSTRUCTIONS.md).


### Read More

For an in-depth story about the journey and technical insights, check out my Medium article: [From Lost Octopus to Data Pipeline Success: Navigating Amazon RDS]([https://medium.com/@vincegalodk/from-lost-octopus-to-data-pipeline-success-navigating-amazon-rds-37412eedc7bd]).

Feel free to contribute and enhance this data pipeline project!
