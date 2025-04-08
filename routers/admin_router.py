from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from models.role import Role
from services.authentication_service import AuthenticationService
from services.authorization_service import AuthorizationService
from services.logging_service import LoggingService
import uuid

admin_router = APIRouter()

@admin_router.post("/create_user")
async def create_user(username: str, password: str, role_id: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, 'create_user'):
        raise HTTPException(status_code=403, detail="Forbidden")

    new_user = User(user_id=str(uuid.uuid4()), username=username, password=password, role=role_id)
    new_user.save_to_db()
    LoggingService.log_user_action(user_id, f'Created user {username}')
    return {"message": "User created successfully"}

@admin_router.put("/update_user/{user_id}")
async def update_user(user_id: str, username: str, password: str, role_id: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'update_user'):
        raise HTTPException(status_code=403, detail="Forbidden")

    user = User.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = username or user.username
    user.password = password or user.password
    user.role = role_id or user.role
    user.save_to_db()
    LoggingService.log_user_action(current_user_id, f'Updated user {user_id}')
    return {"message": "User updated successfully"}

@admin_router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'delete_user'):
        raise HTTPException(status_code=403, detail="Forbidden")

    user = User.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    del User._user_db[user_id]
    LoggingService.log_user_action(current_user_id, f'Deleted user {user_id}')
    return {"message": "User deleted successfully"}

@admin_router.post("/create_role")
async def create_role(role_name: str, permissions: list, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, 'create_role'):
        raise HTTPException(status_code=403, detail="Forbidden")

    new_role = Role(role_id=str(uuid.uuid4()), role_name=role_name, permissions=permissions)
    new_role.save_to_db()
    LoggingService.log_role_change(new_role.role_id, f'Created role {role_name}')
    return {"message": "Role created successfully"}

@admin_router.put("/update_role/{role_id}")
async def update_role(role_id: str, role_name: str, permissions: list, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'update_role'):
        raise HTTPException(status_code=403, detail="Forbidden")

    role = Role.find_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    role.role_name = role_name or role.role_name
    role.permissions = permissions or role.permissions
    role.save_to_db()
    LoggingService.log_role_change(role_id, f'Updated role {role_id}')
    return {"message": "Role updated successfully"}

@admin_router.delete("/delete_role/{role_id}")
async def delete_role(role_id: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'delete_role'):
        raise HTTPException(status_code=403, detail="Forbidden")

    role = Role.find_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    del Role._role_db[role_id]
    LoggingService.log_role_change(role_id, f'Deleted role {role_id}')
    return {"message": "Role deleted successfully"}

@admin_router.post("/assign_role")
async def assign_role(user_id: str, role_id: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(current_user_id, 'assign_role'):
        raise HTTPException(status_code=403, detail="Forbidden")

    user = User.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role = Role.find_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    user.role = role_id
    user.save_to_db()
    LoggingService.log_user_action(current_user_id, f'Assigned role {role_id} to user {user_id}')
    return {"message": "Role assigned successfully"}