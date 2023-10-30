from src.utils import read_data, write_data

record_count = 0  # Initialize a record count

while True:
    message = read_data()

    if message is not None:
        print(message)
        write_data(message)
        record_count += 1  # Increment the record count

    if record_count % 10 == 0:  # Print a message every 10 records (adjust as needed)
        print(f"{record_count} records added to the database")

    # Optionally, you can add a sleep interval to control the rate of processing
    # time.sleep(1)  # Sleep for 1 second
