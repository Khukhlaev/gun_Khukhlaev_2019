from random import randrange as rnd


class Target:
    def __init__(self, canvas):
        self.points = 0
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
        self.canvas.delete(self.id)
        self.points += points
        self.canvas.itemconfig(self.id_points, text=self.points)

    def move(self):
        dx = 0
        dy = 0
        if self.x + self.vx - self.r < 10:  # If target will touch left wall
            dx = self.x + self.vx - self.r - 10
            self.vx *= -1
        if self.x + self.vx + self.r > 790:  # If target will touch right wall
            dx = self.x + self.vx + self.r - 790
            self.vx *= -1
        if self.y + self.vy + self.r > 590:  # If target will touch "floor"
            dy = self.y + self.vy + self.r - 590
            self.vy *= -1
        if self.y + self.vy - self.r < 0:  # If target will touch "floor"
            dy = self.y + self.vy - self.r
            self.vy *= -1
        self.x += self.vx - dx
        self.y += self.vy - dy
        self.canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )
