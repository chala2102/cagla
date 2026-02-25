import json
from typing import List, Optional

class UserStore:
    def __init__(self, file_path: str):
        # Kullanıcı verilerini saklayacak dosya
        self.file_path = file_path

    def load(self) -> List[dict]:
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, users: List[dict]):
        with open(self.file_path, "w") as f:
            json.dump(users, f, indent=4)

    def find_by_id(self, user_id: int) -> Optional[dict]:
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    def get_next_id(self) -> int:
        users = self.load()
        return 1 if not users else max(user["id"] for user in users) + 1

    def update_user(self, user_id: int, updated_data: dict) -> bool:
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                users[i].update(updated_data)
                self.save(users)
                return True
        return False

    def delete_user(self, user_id: int) -> bool:
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                users.pop(i)
                self.save(users)
                return True
        return False