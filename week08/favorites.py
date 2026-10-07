import json
import os


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            self.favorites = {}
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.favorites = data
            else:
                self.favorites = {}
        except (json.JSONDecodeError, OSError):
            self.favorites = {}

    def _save(self):
        with open(self.filename, "w") as file:
            json.dump(self.favorites, file, indent=4)

    def add(self, name, location):
        if name.lower() in {key.lower() for key in self.favorites}:
            return False

        self.favorites[name] = location
        self._save()
        return True

    def remove(self, name):
        for key in self.favorites:
            if key.lower() == name.lower():
                del self.favorites[key]
                self._save()
                return True

        return False

    def list_all(self):
        return self.favorites.copy()

    def get_location(self, name):
        for key, location in self.favorites.items():
            if key.lower() == name.lower():
                return location

        return None

