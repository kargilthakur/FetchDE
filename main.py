import time
from src.utils import read_data, write_data


class DataProcessor:
    def __init__(self):
        self.record_count = 0

    def process_data(self):
        while True:
            message = read_data()

            if message is not None:
                print(message)
                write_data(message)
                self.record_count += 1

            if self.record_count % 10 == 0:
                print(f"{self.record_count} records added to the database")

            time.sleep(1)


if __name__ == "__main__":
    data_processor = DataProcessor()
    data_processor.process_data()
