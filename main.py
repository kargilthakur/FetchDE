import time
from src.utils import read_data, write_data
from configparser import ConfigParser


class DataProcessor:
    def __init__(self,config):
        self.record_count = 0
        self.config = config
    def process_data(self):
        while True:
            message = read_data(self.config)

            if message is not None:
                print(message)
                write_data(message,self.config)
                self.record_count += 1

            if self.record_count % 10 == 0:
                print(f"{self.record_count} records added to the database")

            time.sleep(1)


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config/config.ini")
    data_processor = DataProcessor(config)
    data_processor.process_data()
