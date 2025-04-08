from flask import Flask, request, jsonify
from models.user import User
from models.role import Role
from services.authentication_service import AuthenticationService
from services.authorization_service import AuthorizationService
from services.logging_service import LoggingService

app = Flask(__name__)

@app.route('/admin/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role_id = data.get('role_id')

    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, 'create_user'):
        return jsonify({'error': 'Forbidden'}), 403

    # Create and save the user
    new_user = User(user_id=str(uuid.uuid4()), username=username, password=password, role=role_id)
    new_user.save_to_db()
    LoggingService.log_user_action(user_id, f'Created user {username}')
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/admin/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role_id = data.get('role_id')

    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'update_user'):
        return jsonify({'error': 'Forbidden'}), 403

    # Update the user
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.username = username or user.username
    user.password = password or user.password
    user.role = role_id or user.role
    user.save_to_db()
    LoggingService.log_user_action(current_user_id, f'Updated user {user_id}')
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/admin/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'delete_user'):
        return jsonify({'error': 'Forbidden'}), 403

    # Delete the user
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    del User._user_db[user_id]
    LoggingService.log_user_action(current_user_id, f'Deleted user {user_id}')
    return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/admin/create_role', methods=['POST'])
def create_role():
    data = request.json
    role_name = data.get('role_name')
    permissions = data.get('permissions', [])

    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, 'create_role'):
        return jsonify({'error': 'Forbidden'}), 403

    # Create and save the role
    new_role = Role(role_id=str(uuid.uuid4()), role_name=role_name, permissions=permissions)
    new_role.save_to_db()
    LoggingService.log_role_change(new_role.role_id, f'Created role {role_name}')
    return jsonify({'message': 'Role created successfully'}), 201

@app.route('/admin/update_role/<role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.json
    role_name = data.get('role_name')
    permissions = data.get('permissions')

    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'update_role'):
        return jsonify({'error': 'Forbidden'}), 403

    # Update the role
    role = Role.find_by_id(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404

    role.role_name = role_name or role.role_name
    role.permissions = permissions or role.permissions
    role.save_to_db()
    LoggingService.log_role_change(role_id, f'Updated role {role_id}')
    return jsonify({'message': 'Role updated successfully'}), 200

@app.route('/admin/delete_role/<role_id>', methods=['DELETE'])
def delete_role(role_id):
    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'delete_role'):
        return jsonify({'error': 'Forbidden'}), 403

    # Delete the role
    role = Role.find_by_id(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404

    del Role._role_db[role_id]
    LoggingService.log_role_change(role_id, f'Deleted role {role_id}')
    return jsonify({'message': 'Role deleted successfully'}), 200

@app.route('/admin/assign_role', methods=['POST'])
def assign_role():
    data = request.json
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    # Check if user is authenticated and has permission
    session_token = request.headers.get('Authorization')
    if not AuthenticationService.is_authenticated(session_token):
        return jsonify({'error': 'Unauthorized'}), 401

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'assign_role'):
        return jsonify({'error': 'Forbidden'}), 403

    # Assign role to user
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    role = Role.find_by_id(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404

    user.role = role_id
    user.save_to_db()
    LoggingService.log_user_action(current_user_id, f'Assigned role {role_id} to user {user_id}')
    return jsonify({'message': 'Role assigned successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)