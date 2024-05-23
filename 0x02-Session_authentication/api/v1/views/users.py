#!/usr/bin/python3
"""Module of views for Users"""
from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Get all users"""
    all_users = [user.to_dict() for user in User.all()]
    return jsonify(all_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a single user"""
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    if 'password' not in data:
        return jsonify({"error": "Missing password"}), 400
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Update a user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200
