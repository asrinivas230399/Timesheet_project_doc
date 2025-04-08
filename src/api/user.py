from flask import Blueprint, request, jsonify
from models.user import User
from services.authentication_service import AuthenticationService
from services.authorization_service import AuthorizationService
from services.logging_service import LoggingService

user_api = Blueprint('user_api', __name__)

@user_api.route('/user/view', methods=['GET'])
def view_user():
    # Check if user is authenticated
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'user_id': user.user_id,
        'username': user.username,
        'role': user.role
    }), 200

@user_api.route('/user/update', methods=['PUT'])
def update_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user is authenticated
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Update user information
    user.username = username or user.username
    user.password = password or user.password
    user.save_to_db()
    LoggingService.log_user_action(user_id, 'Updated their information')
    return jsonify({'message': 'User updated successfully'}), 200

@user_api.route('/user/perform_action', methods=['POST'])
def perform_action():
    data = request.json
    action = data.get('action')

    # Check if user is authenticated
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, action):
        return jsonify({'error': 'Forbidden'}), 403

    # Log the action
    LoggingService.log_user_action(user_id, f'Performed action: {action}')
    return jsonify({'message': f'Action {action} performed successfully'}), 200
