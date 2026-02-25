from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()

store = UserStore("users.db")


# -------------------------
# POST /users
# Create new user
# -------------------------

@router.post("/")
def create_user(user: UserCreate):

    users = store.load()

    new_user = {
        "id": store.get_next_id(),
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    store.save(users)

    return new_user


# -------------------------
# GET /users
# -------------------------

@router.get("/")
def get_users():

    return store.load()


# -------------------------
# GET /users/search
# -------------------------

@router.get("/search")
def search_users(q: str):

    users = store.load()

    return [user for user in users if q.lower() in user["name"].lower()]


# -------------------------
# GET /users/{id}
# -------------------------

@router.get("/{id}")
def get_user(id: int):

    user = store.find_by_id(id)

    if user:
        return user

    raise HTTPException(status_code=404, detail="User not found")


# -------------------------
# PUT /users/{id}
# -------------------------

@router.put("/{id}")
def update_user(id: int, updated_user: UserCreate):

    success = store.update_user(id, updated_user.dict())

    if success:
        return {"message": "User updated"}

    raise HTTPException(status_code=404, detail="User not found")


# -------------------------
# DELETE /users/{id}
# -------------------------

@router.delete("/{id}")
def delete_user(id: int):

    success = store.delete_user(id)

    if success:
        return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")