#!/usr/bin/env python3
"""
Filter module for teaching data protection and logging.
"""

from typing import List
import re
import logging
from os import environ
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Redacts sensitive information in log messages.

    Args:
        fields: List of field names to redact.
        redaction: The string to replace sensitive data with.
        message: The original log message.
        separator: The separator used between fields in the message.

    Returns:
        The redacted message where sensitive fields are replaced with the redaction string.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """
    Formatter class that redacts sensitive information from log messages.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter.

        Args:
            fields: List of fields to redact in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats log records by redacting sensitive data.

        Args:
            record: The log record to format.

        Returns:
            A string representation of the log record with sensitive data redacted.
        """
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger object for logging user data.

    Returns:
        A Logger instance with a redacting formatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Establishes and returns a connection to a MySQL database.

    Returns:
        A MySQL database connection.
    """
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    cnx = mysql.connector.connect(user=username, password=password, host=host, database=db_name)
    return cnx


def main():
    """
    Main function to log user data from the database, applying redactions where necessary.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_names))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()

