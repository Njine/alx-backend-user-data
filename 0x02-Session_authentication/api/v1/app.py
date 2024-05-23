#!/usr/bin/python3
"""App module for Session Authentication"""
from flask import Flask, jsonify, request, abort
from os import getenv
from api.v1.views import app_views
from models import storage
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)

auth = None
if getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()
elif getenv('AUTH_TYPE') == 'session_auth':
    auth = SessionAuth()

@app.before_request
def before_request_func():
    """Filter each request before it's handled"""
    if auth:
        excluded_paths = ['/api/v1/status/',
                          '/api/v1/unauthorized/', '/api/v1/forbidden/',
                          '/api/v1/auth_session/login/']
        if not auth.require_auth(request.path, excluded_paths):
            return
        if not auth.authorization_header(request) and \
           not auth.session_cookie(request):
            abort(401)
        request.current_user = auth.current_user(request)
        if request.current_user is None:
            abort(403)

@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    """Handler for 401 errors"""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """Handler for 403 errors"""
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
