# FetchDE

# ETL Data Processing Pipeline

## Directory Structure

```
├── README.md
├── config
│   └── config.ini
├── docker-compose.yml
├── main.py
├── requirements.txt
├── src
│   └── utils.py
├── test.ipynb
└── tests
    └── unit_test.py
```

## Overview

This repository contains an ETL (Extract, Transform, Load) data processing pipeline. The pipeline is designed to continuously extract data from an external source, apply data transformations, and load the transformed data into a PostgreSQL database.

## Usage

### Configuration

Before running the ETL pipeline, you need to configure the `config/config.ini` file with the necessary settings. This configuration file allows you to specify AWS credentials, PostgreSQL database connection details, and other parameters required for the ETL process.

### Dependencies

Ensure that you have the required Python libraries installed. These libraries include `psycopg2`, `boto3`, and `datetime`. Additionally, you should have access to a PostgreSQL database for data storage.

### Running the ETL Pipeline

To start the ETL data processing pipeline, run the following command:

```bash
python main.py
```

This command initiates the ETL pipeline, which continually reads data from an SQS queue, performs data transformations, and stores the transformed data in the designated PostgreSQL database.

### Unit Tests

To validate the functionality of the utility functions used in the ETL pipeline, you can execute unit tests by running:

```bash
python -m unittest tests.unit_test
```

## Author

Kargil Thakur 
