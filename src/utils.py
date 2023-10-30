import json
import boto3
import psycopg2
from configparser import ConfigParser
import hashlib
from datetime import datetime

config = ConfigParser()
config.read("config/config.ini")


def read_data():
    aws_config = config["aws"]

    sqs = boto3.client(
        "sqs",
        endpoint_url="{}".format(aws_config["aws_endpoint_url"]),
        region_name="{}".format(aws_config["aws_region_name"]),
        aws_access_key_id=aws_config["aws_access_key_id"],
        aws_secret_access_key=aws_config["aws_secret_access_key"],
    )

    queue_url = "{}".format(aws_config["aws_queue_url"])

    response = sqs.receive_message(QueueUrl=queue_url)
    if "Messages" in response:
        for message in response["Messages"]:
            message_body = json.loads(message["Body"])
            return message_body
    else:
        print("No messages in the queue")
        return None


def pseudonymize(value, salt):
    value = value + salt
    hashed = hashlib.sha256(value.encode()).hexdigest()
    return hashed


def convert_version_to_integer(version):
    version_parts = version.split(".")
    version_as_int = int("".join(version_parts))
    return version_as_int


def write_data(data):
    required_fields = [
        "user_id",
        "device_type",
        "ip",
        "device_id",
        "locale",
        "app_version",
    ]

    if not all(field in data for field in required_fields):
        print("Received message does not contain all required fields. Skipping.")
        return

    db_config = config["postgres"]

    conn = psycopg2.connect(db_config["db_conn_string"])
    cur = conn.cursor()

    data["create_date"] = datetime.today().strftime("%Y-%m-%d")

    data["app_version"] = convert_version_to_integer(data["app_version"])

    sha_config = config["sha"]
    data["ip"] = pseudonymize(data["ip"], sha_config["salt_ip"])
    data["device_id"] = pseudonymize(data["device_id"], sha_config["salt_device_id"])

    try:
        cur.execute(
            "INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                data["user_id"],
                data["device_type"],
                data["ip"],
                data["device_id"],
                data["locale"],
                int(data["app_version"]),
                data["create_date"],
            ),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Failed to write data to the database: {e}")
    finally:
        cur.close()
        conn.close()
