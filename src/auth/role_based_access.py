from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

# Simulated user database
users_db = {
    "alice": {"username": "alice", "role": "admin"},
    "bob": {"username": "bob", "role": "user"}
}

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Role-based access control
roles_permissions = {
    "admin": ["add_project", "edit_project"],
    "user": ["view_project"]
}

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = users_db.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user

def check_permission(user: dict, permission: str):
    role = user.get("role")
    if permission not in roles_permissions.get(role, []):
        raise HTTPException(status_code=403, detail="Operation not permitted")

# Dependency to check if the user has permission to add a project
def can_add_project(user: dict = Depends(get_current_user)):
    check_permission(user, "add_project")

# Dependency to check if the user has permission to edit a project
def can_edit_project(user: dict = Depends(get_current_user)):
    check_permission(user, "edit_project")