# FetchDE

# ETL Data Processing Pipeline

## Overview

This repository contains an ETL (Extract, Transform, Load) data processing pipeline. The pipeline is designed to continuously extract data from an external source, apply data transformations, and load the transformed data into a PostgreSQL database.

## Thought Process


### How Messages Are Read from the Queue
To read messages from the queue, we utilize the boto3 library, which interfaces with Amazon Simple Queue Service (SQS). The `read_data` function in `utils.py` creates an SQS client with the specified queue URL, region name, endpoint, and user credentials. Subsequently, the `receive_message` function is employed to retrieve messages from the queue, which are then processed into individual JSON records.

### Data Structures Used
The primary data structures employed in the application are dictionaries and JSON data structures. Incoming messages from the SQS queue are typically in JSON format. The code operates on this data using Python dictionaries, making it easy to handle and manipulate the information.

### Masking PII Data for Identification of Duplicates
To safeguard Personally Identifiable Information (PII) data, we employ SHA-256 hashing with a unique salt. SHA-256 is a cryptographically secure one-way hash function. It obscures sensitive information by converting it into a fixed-size hash. Cracking a SHA-256 hash is computationally intensive and time-consuming, making it a robust choice for data protection. Additionally, SHA-256 consistently generates the same hash values for identical input data, allowing us to identify duplicate records.

### Strategy for Connecting and Writing to PostgreSQL
For connecting to and writing data to a PostgreSQL database, the code utilizes the psycopg2 library. It establishes a connection to the database and creates a cursor, which is employed to interact with the database. Data is inserted into the database using SQL statements, and the connection is committed. In case of an error, the code handles exceptions by rolling back the transaction.

### Where and How the Application Runs
The application can be executed on a suitable computing environment after configuring the PostgreSQL database details and AWS credentials in the `config.ini` file. To launch the application, simply run the `main.py` file. It will commence the data processing pipeline, extracting data from the AWS queue, securing PII data through SHA-256 hashing, and storing the anonymized data in the designated PostgreSQL database.

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
  
## Questions

### How would you deploy this application in production?

This application can be deployed in the production environment following these steps:

1. **Server Setup**: Configure the necessary servers or cloud instances.

2. **Database Management**: Utilize a robust database solution to store your data.

3. **Security Measures**: Implement stringent security protocols.

4. **Application Deployment**: Deploy your application code on servers or containers.

5. **Performance monitoring**: Ensure the system can adapt to varying workloads by monitoring performance metrics.

For a specific AWS example, deploy the application on Amazon EC2 instances, backed by Amazon RDS for PostgreSQL as the database. Set up Amazon SQS for message queuing and leverage Amazon CloudWatch for real-time monitoring. Use AWS IAM for granular security controls, while Amazon S3 serves for backups. 

### What other components would you want to add to make this production-ready?

Building upon the previously mentioned components, there are several key elements to consider for making this application production-ready:

1. **Containerize the Application**: Use Docker to containerize the application for consistent deployment.

2. **Implement Logging and Monitoring**: Set up a logging and monitoring system to track application performance.

3. **CI/CD Pipeline**: Establish a CI/CD pipeline for automated testing and deployment.

4. **High Availability Configuration**: Deploy the application in a high-availability configuration, distributing it across multiple servers or data centres.

5. **Comprehensive Documentation**: Develop detailed documentation for installation, configuration, and troubleshooting.

### How can this application scale with a growing dataset?

To ensure scalability with a growing dataset, the application should optimise resource usage and parallel processing. Horizontal scaling by distributing the application across multiple server instances allows for efficient handling of increasing data loads. It's essential to implement proper load-balancing mechanisms to distribute processing requests evenly.

Additionally, adopting cloud services, such as Amazon RDS, AWS Lambda, and S3, can provide the necessary elasticity to adapt to changing data volumes dynamically. Implementing data archiving and asynchronous processing can prevent performance degradation as the dataset grows. These strategies, coupled with well-designed database optimization, help the application remain responsive and scalable in the face of increasing data demands.

### How can PII be recovered later on?

In our case, where PII data is masked using SHA-256 hashing, recovery can be challenging due to the irreversible nature of the hashing process. SHA-256 is a one-way cryptographic hash function, which means there is no direct method to retrieve the original PII data from the hash value. 

### What are the assumptions you made?

1. AWS SQS is configured.
2. The PostgreSQL database is operational.
3. The config.ini file contains valid credentials.
4. Incoming data adheres to JSON format.
5. The application runs in a Python-supporting environment.

These assumptions are essential for the application's proper operation.

## Future Steps

If I had more time to design this application, I would have implemented the following enhancements to make it more production-ready and efficient:

1. Containerization: I would containerize the application using Docker to enhance portability, scalability, and deployment consistency.

2. Error Logging: Robust error logging and handling mechanisms would be a priority to diagnose and address issues quickly.

3. Monitoring: Continuous monitoring of the pipeline's performance, including key performance indicators, would be essential for optimization.

4. Parallel Processing: Implementing parallel processing and distributed computing techniques would improve data handling.

These enhancements would empower the application to handle growing datasets while maintaining high performance efficiently.

## Author

Kargil Thakur 
