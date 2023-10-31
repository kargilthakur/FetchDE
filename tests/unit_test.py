import unittest
import sys
sys.path.append("..") 
import psycopg2
from src.utils import pseudonymize, convert_version_to_integer, write_data, read_data


class TestYourFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        
    def test_read_data(self):

        message = read_data()
        self.assertIsNotNone(message)

    def test_pseudonymize(self):
        # Test your pseudonymize function here
        salt = "30"
        original_value = "127.0.0.1"
        hashed_value = pseudonymize(original_value, salt)
        hashed_value_1 = pseudonymize(original_value, salt)

        self.assertEqual(hashed_value, hashed_value_1)
        self.assertNotEqual(original_value, hashed_value)
        self.assertEqual(len(hashed_value), 64)

    def test_convert_version_to_integer(self):
        # Test your convert_version_to_integer function here
        version_string = "1.2.3"
        version_integer = convert_version_to_integer(version_string)

        self.assertEqual(version_integer, 123)
    
    def test_write_data(self):
        # Define a sample data dictionary with all required fields
        sample_data = {
            "user_id": "12345",
            "device_type": "mobile",
            "ip": "127.0.0.1",
            "device_id": "device123",
            "locale": "en-US",
            "app_version": "1.2.3",
        }
        
        self.assertIsNone(write_data({}))  
        self.assertIsNone(write_data({"user_id": "12345"}))  
        
        test_db_conn = psycopg2.connect("postgres://postgres:postgres@localhost:5432/postgres")
        cur = test_db_conn.cursor()
        try:
            cur.execute("SELECT count(*) from user_logins")
            count = cur.fetchone()[0]
        except:
            print("No records")

        from unittest.mock import patch
        with patch("datetime.datetime") as mock_datetime:
            sample_data['create_date'] = mock_datetime.today().strftime()
            write_data(sample_data)
        
        cur = test_db_conn.cursor()
        try:
            cur.execute("SELECT count(*) from user_logins")
            self.assertEqual(count+1,cur.fetchone()[0])
        except:
            print("Cannot Connect") 


if __name__ == "__main__":
    unittest.main()