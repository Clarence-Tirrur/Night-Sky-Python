from datetime import datetime


class Book:

    def __init__(self, title, author, price, description,
                 cover_path="", book_id=None):

        self.title = title
        self.author = author
        self.price = float(price)
        self.description = description
        self.cover_path = cover_path
        self.id = book_id or f"bk{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "description": self.description,
            "cover_path": self.cover_path
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["title"],
            d["author"],
            d.get("price", 0),
            d.get("description", ""),
            d.get("cover_path", ""),
            d.get("id")
        )

    def __str__(self):
        return f"{self.title} by {self.author} - ₱{self.price:.2f}"
