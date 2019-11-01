from random import randrange as rnd


class Target:
    def __init__(self, canvas):
        self.points = 0
        self.live = 1
        self.canvas = canvas
        self.id = self.canvas.create_oval(0, 0, 0, 0)
        self.id_points = self.canvas.create_text(30, 30, text=self.points, font='28')
        x = self.x = rnd(600, 760)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        color = self.color = 'red'
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.canvas.coords(self.id, x - r, y - r, x + r, y + r)
        self.canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        self.canvas.itemconfig(self.id_points, text=self.points)

    def move(self):
        if self.x >= 800 or self.x <= 0:
            self.vx = -self.vx
        if self.y >= 600 or self.y <= 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        self.canvas.move(self.id, self.vx, -self.vy)
