from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from services.authentication_service import AuthenticationService
from services.authorization_service import AuthorizationService
from services.logging_service import LoggingService

user_router = APIRouter()

@user_router.get("/view")
async def view_user(session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    user = User.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role
    }

@user_router.put("/update")
async def update_user(username: str, password: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    user = User.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = username or user.username
    user.password = password or user.password
    user.save_to_db()
    LoggingService.log_user_action(user_id, 'Updated their information')
    return {"message": "User updated successfully"}

@user_router.post("/perform_action")
async def perform_action(action: str, session_token: str = Depends(AuthenticationService.get_session_token)):
    if not AuthenticationService.is_authenticated(session_token):
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = AuthenticationService.get_user_id_from_session(session_token)
    if not AuthorizationService.user_has_permission(user_id, action):
        raise HTTPException(status_code=403, detail="Forbidden")

    LoggingService.log_user_action(user_id, f'Performed action: {action}')
    return {"message": f'Action {action} performed successfully'}