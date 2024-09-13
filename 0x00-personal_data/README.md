# Overview

This project focuses on managing personal data securely, with a particular emphasis on protecting Personally Identifiable Information (PII) and ensuring secure authentication practices. The tasks include creating loggers to filter sensitive information, encrypting passwords, and connecting to a secure database using environment variables.

## Files

### `filtered_logger.py`
This file handles logging and data filtering. Key functionalities include:
- **`filter_datum`**: Obfuscates sensitive fields in log messages using regular expressions.
- **`RedactingFormatter`**: Custom log formatter that filters PII fields before logging.
- **`get_logger`**: Creates and configures a logger to safely log user data, ensuring sensitive fields are obfuscated.
- **`get_db`**: Connects to a secure MySQL database using environment variables for credentials.

### `encrypt_password.py`
This file manages password encryption and validation. Key functionalities include:
- **`hash_password`**: Encrypts a given password using `bcrypt`.
- **`is_valid`**: Verifies if a plain-text password matches the stored encrypted version.

This project emphasizes secure logging, password protection, and safe database connections using environment variables.
