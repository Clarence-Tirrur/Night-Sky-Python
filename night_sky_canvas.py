import tkinter as tk
import random


class Star:

    def __init__(self, width, height):
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)
        self.size = random.randint(1, 3)


class NightSkyCanvas(tk.Canvas):

    def __init__(self, parent, width=900, height=700):

        super().__init__(parent, width=width, height=height, bg="#0a0a23")

        self.width = width
        self.height = height

        self.stars = [
            Star(width, height) for _ in range(80)
        ]

        self.animate()

    def animate(self):

        self.delete("star")

        for s in self.stars:

            self.create_oval(
                s.x, s.y,
                s.x + s.size,
                s.y + s.size,
                fill="white",
                outline="",
                tags="star"
            )

        self.after(100, self.animate)
