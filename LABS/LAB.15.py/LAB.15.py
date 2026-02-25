import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Load users from file and return a list of dictionaries."""
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            users = []
            for line in f:
                if line.strip():  # skip empty lines
                    users.append(json.loads(line))
            return users

    def save(self, users):
        """Save a list of user dictionaries to file as JSON lines."""
        with open(self.file_path, "w") as f:
            for user in users:
                f.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id):
        """Return the user dictionary with matching id, or None."""
        users = self.load()
        for user in users:
            if user.get("id") == user_id:
                return user
        return None

    def update_user(self, user_id, updated_data):
        """Update a user by ID. Returns True if successful, False otherwise."""
        users = self.load()
        for i, user in enumerate(users):
            if user.get("id") == user_id:
                users[i].update(updated_data)
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        """Delete a user by ID. Returns True if successful, False otherwise."""
        users = self.load()
        new_users = [user for user in users if user.get("id") != user_id]
        if len(new_users) == len(users):
            return False  # nothing was deleted
        self.save(new_users)
        return True


        from fastapi import FastAPI, HTTPException
from user_store import UserStore

app = FastAPI()
store = UserStore("users.txt")

@app.get("/users")
def get_users():
    return store.load()

@app.post("/users")
def create_user(user: dict):
    users = store.load()
    if any(u.get("id") == user.get("id") for u in users):
        raise HTTPException(status_code=400, detail="User ID already exists")
    users.append(user)
    store.save(users)
    return {"message": "User created successfully"}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_data: dict):
    success = store.update_user(user_id, updated_data)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}