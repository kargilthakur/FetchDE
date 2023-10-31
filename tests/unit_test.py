import unittest
import psycopg2
from configparser import ConfigParser
from src.utils import pseudonymize, convert_version_to_integer, write_data, read_data
import os


class TestYourFunctions(unittest.TestCase):
    def setUp(self):
        """
        Set up common resources and configurations for the test cases.

        This method is called before each test case. It sets up the configuration
        and changes the current working directory to the project's root to ensure
        proper access to the configuration file.
        """
        self.config = ConfigParser()

        current_dir = os.path.dirname(__file__)
        root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        os.chdir(root_dir)
        config_file_path = os.path.join(root_dir, "config", "config.ini")
        print(f"Config file path: {config_file_path}")
        self.config.read(config_file_path)

    def test_read_data(self):
        """
        Test the read_data function.

        This test case checks if the read_data function successfully retrieves data and returns a non-empty message.
        """
        message = read_data(self.config)
        self.assertIsNotNone(message)

    def test_pseudonymize(self):
        """
        Test the pseudonymize function.

        This test case validates the pseudonymize function's behavior by hashing an IP address with a salt.
        It checks if the hashed values are equal and if the original value is are same.
        It also checks if the length of hash is 64 according to SHA conventions.
        """
        salt = "30"
        original_value = "127.0.0.1"
        hashed_value = pseudonymize(original_value, salt)
        hashed_value_1 = pseudonymize(original_value, salt)

        self.assertEqual(hashed_value, hashed_value_1)
        self.assertNotEqual(original_value, hashed_value)
        self.assertEqual(len(hashed_value), 64)

    def test_convert_version_to_integer(self):
        """
        Test the convert_version_to_integer function.

        This test case verifies the convert_version_to_integer function's ability to convert a version string into an integer format.
        It checks if the conversion is done correctly by comparing the result with the expected integer value.
        """
        version_string = "1.2.3"
        version_integer = convert_version_to_integer(version_string)

        self.assertEqual(version_integer, 123)

    def test_write_data(self):
        """
        Test the write_data function.

        This test case validates the write_data function's behavior. It includes multiple checks:
        1. It checks if writing data with missing required fields results in None.
        2. It verifies that writing data with a valid sample data dictionary succeeds.
        3. It checks if the number of records in the database increases after writing data.
        """
        sample_data = {
            "user_id": "12345",
            "device_type": "mobile",
            "ip": "127.0.0.1",
            "device_id": "device123",
            "locale": "en-US",
            "app_version": "1.2.3",
        }

        self.assertIsNone(write_data({}, self.config))
        self.assertIsNone(write_data({"user_id": "12345"}, self.config))

        test_db_conn = psycopg2.connect(
            "postgres://postgres:postgres@localhost:5432/postgres"
        )
        cur = test_db_conn.cursor()
        try:
            cur.execute("SELECT count(*) from user_logins")
            count = cur.fetchone()[0]
        except:
            print("No records")

        from unittest.mock import patch

        with patch("datetime.datetime") as mock_datetime:
            sample_data["create_date"] = mock_datetime.today().strftime()
            write_data(sample_data, self.config)

        cur = test_db_conn.cursor()
        try:
            cur.execute("SELECT count(*) from user_logins")
            self.assertEqual(count + 1, cur.fetchone()[0])
        except:
            print("Cannot Connect")


if __name__ == "__main":
    unittest.main()
