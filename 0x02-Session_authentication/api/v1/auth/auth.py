#!/usr/bin/python3
"""Auth module"""
from flask import request
from os import getenv

class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """Check if path requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None):
        """Get the current user from the request"""
        return None

    def session_cookie(self, request=None):
        """Get the session cookie from the request"""
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"))
