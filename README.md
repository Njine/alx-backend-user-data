# Session Authentication System

## Description

This project implements a session-based authentication system using Flask, SQLAlchemy, and bcrypt. It covers user registration, login, session management, and password reset functionality.

## Files

- `user.py`: Defines the User model.
- `db.py`: Database management with methods to add, find, and update users.
- `auth.py`: Authentication class with methods for user registration, login, session creation, and password management.
- `app.py`: Flask application with endpoints for user registration, login, profile, and password reset.

## Setup

1. Install dependencies:
    ```bash
    pip install flask sqlalchemy bcrypt
    ```

2. Run the application:
    ```bash
    ./app.py
    ```

## Endpoints

- `POST /users`: Register a new user.
- `POST /sessions`: Log in and create a session.
- `DELETE /sessions`: Log out and destroy the session.
- `GET /profile`: Get the user profile.
- `POST /reset_password`: Request a password reset token.
- `PUT /reset_password`: Update the user's password using the reset token.

## License

This project is licensed under the MIT License.

