import json
import os
from typing import Any, Dict, List
from models.book import Book

USERS_FILE = "users.json"
BOOKS_FILE = "books.json"
ORDERS_FILE = "orders.json"

DEFAULT_USERS = {"admin": {"password": "987654321", "blocked": False}}
DEFAULT_BOOKS = [{}]
DEFAULT_ORDERS = []


def load_json(path: str, default: Any):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f)

    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default


def save_json(path: str, data: Any):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


class DataManager:

    def __init__(self):

        self.users = load_json(USERS_FILE, DEFAULT_USERS)

        raw_books = load_json(BOOKS_FILE, DEFAULT_BOOKS)
        self.books = [Book.from_dict(b) for b in raw_books]

        self.orders = load_json(ORDERS_FILE, DEFAULT_ORDERS)

    def validate_login(self, username, password):

        user = self.users.get(username)

        if not user:
            return False

        if user.get("blocked"):
            return False

        return user["password"] == password

    def add_user(self, username, password):

        if username in self.users:
            return False

        self.users[username] = {
            "password": password,
            "blocked": False
        }

        save_json(USERS_FILE, self.users)
        return True

    def add_book(self, book):

        self.books.append(book)
        save_json(BOOKS_FILE, [b.to_dict() for b in self.books])

    def delete_book(self, book_id):

        self.books = [b for b in self.books if b.id != book_id]
        save_json(BOOKS_FILE, [b.to_dict() for b in self.books])

    def add_order(self, username, items, total):

        order = {
            "username": username,
            "items": items,
            "total": total
        }

        self.orders.append(order)
        save_json(ORDERS_FILE, self.orders)
