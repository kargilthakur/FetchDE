# FetchDE

# ETL Data Processing Pipeline

## Overview

This repository contains an ETL (Extract, Transform, Load) data processing pipeline. The pipeline is designed to continuously extract data from an external source, apply data transformations, and load the transformed data into a PostgreSQL database.

## Usage

### Configuration

Before running the ETL pipeline, you must configure the `config/config.ini` file with the necessary settings. This configuration file allows you to specify AWS credentials, PostgreSQL database connection details, and other parameters required for the ETL process.

### Docker Setup

To run the ETL pipeline, you should set up the necessary Docker containers by running:

```bash
docker-compose up
```

This command starts the Docker containers defined in the docker-compose.yml file, which may be required for specific components of the ETL process.

### Dependencies

To install the required Python libraries, run the following command:

```bash
pip install -r requirements.txt
```

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

## Thought Process

* How will you read messages from the queue?
* What type of data structures should be used?
* How will you mask the PII data so that duplicate values can be identified?
* What will be your strategy for connecting and writing to Postgres?
* Where and how will your application run?

## Questions

* How would you deploy this application in production?
* What other components would you want to add to make this production-ready?
* How can this application scale with a growing dataset?
* How can PII be recovered later on?
* What are the assumptions you made?



## Future Steps

## Author

Kargil Thakur 
