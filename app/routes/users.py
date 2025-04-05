from app.main import app
from app.schemas.user import UserSignup , UserLogin

@app.post("/users/signup")
async def create_user(request : UserSignup):
    return {"message" : "User created successfully", "user" : request}

@app.post("users/login")
async def login_user(request : UserLogin):
    return {"message" : "Login successful", "user" : request}