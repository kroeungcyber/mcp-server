from typing import Dict, Any

class UserProfile:
    def __init__(self):
        self.profiles: Dict[str, Dict[str, Any]] = {}

    def get_profile(self, user_id: str) -> Dict[str, Any]:
        return self.profiles.get(user_id, {})

    def update_profile(self, user_id: str, updates: Dict[str, Any]):
        if user_id not in self.profiles:
            self.profiles[user_id] = {}
        self.profiles[user_id].update(updates)