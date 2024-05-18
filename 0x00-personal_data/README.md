# Backend User Data

This project contains modules for handling personal user data, including log filtering, password encryption, and database interaction.

## Files

### `filtered_logger.py`
- **filter_datum**: Filters specific fields in a log message using regex.
- **get_logger**: Creates a logger configured to handle and filter personal information.
- **get_db**: Connects to a MySQL database using credentials from environment variables.
- **RedactingFormatter**: Custom logging formatter that redacts sensitive fields.

### `encrypt_password.py`
- **hash_password**: Hashes a password using bcrypt.
- **is_valid**: Validates a password against a hashed password.

### `main.py`
- Tests the functionality of the modules in `filtered_logger.py` and `encrypt_password.py`.

## Usage

### Running the main file
```bash
./main.py
