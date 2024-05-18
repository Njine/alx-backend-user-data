#!/usr/bin/env python3
"""A module for handling password encryption."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against a hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
