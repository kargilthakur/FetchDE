"""
ETL (Extract, Transform, Load) Data Processor

This script defines the DataProcessor class, which is responsible for continuously processing data
from an external source, transforming it, and loading it into a database. The ETL process is controlled
by a configuration file specified in the 'config/config.ini' file. The DataProcessor class reads
messages from an SQS queue, performs data transformations, and writes the data to a PostgreSQL database.

Usage:
- Make sure to configure the 'config/config.ini' file with the appropriate settings before running this script.
- Ensure that the required Python libraries are installed, and a PostgreSQL database is available.

Attributes:
    config (ConfigParser): A configuration parser object that reads settings from 'config/config.ini'.
    record_count (int): A counter to keep track of the number of records processed.

Methods:
    process_data():
    - The main data processing loop that continuously reads messages from the SQS queue, performs transformations,
      and stores the data in the database. It also prints a message every 10 records processed.

Example:
    To run the ETL pipeline, execute this script after configuring 'config/config.ini' appropriately.

Author:
    Kargil Thakur

Date:
    10/30/2023
"""
import time
from src.utils import read_data, write_data
from configparser import ConfigParser


class DataProcessor:
    def __init__(self, config):
        self.record_count = 0
        self.config = config

    def process_data(self):
        while True:
            message = read_data(self.config)

            if message is not None:
                print(message)
                write_data(message, self.config)
                self.record_count += 1

            if self.record_count % 10 == 0:
                print(f"{self.record_count} records added to the database")

            time.sleep(1)


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config/config.ini")
    data_processor = DataProcessor(config)
    data_processor.process_data()
