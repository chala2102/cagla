from fastapi import APIRouter, HTTPException
from schema import UserCreate
import json
import os

router = APIRouter()

FILE = "users.txt"


# -------------------------
# Helper Functions
# -------------------------

def read_users():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def write_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


# -------------------------
# POST /users
# Create new user
# -------------------------

@router.post("/")
def create_user(user: UserCreate):

    users = read_users()

    new_user = {
        "id": get_next_id(users),
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    write_users(users)

    return new_user


# -------------------------
# GET /users
# Get all users
# -------------------------

@router.get("/")
def get_users():

    return read_users()


# -------------------------
# GET /users/search?q=
# IMPORTANT: must be before /{id}
# -------------------------

@router.get("/search")
def search_users(q: str):

    users = read_users()

    results = [user for user in users if q.lower() in user["name"].lower()]

    return results


# -------------------------
# GET /users/{id}
# Get user by ID
# -------------------------

@router.get("/{id}")
def get_user(id: int):

    users = read_users()

    for user in users:

        if user["id"] == id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


# -------------------------
# PUT /users/{id}
# Update user
# -------------------------

@router.put("/{id}")
def update_user(id: int, updated_user: UserCreate):

    users = read_users()

    for user in users:

        if user["id"] == id:

            user["name"] = updated_user.name
            user["email"] = updated_user.email

            write_users(users)

            return user

    raise HTTPException(status_code=404, detail="User not found")


# -------------------------
# DELETE /users/{id}
# Delete user
# -------------------------

@router.delete("/{id}")
def delete_user(id: int):

    users = read_users()

    for user in users:

        if user["id"] == id:

            users.remove(user)

            write_users(users)

            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")