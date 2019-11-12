from random import randrange as rnd


class Target:
    def __init__(self, canvas):
        """ Ball class constructor """
        self.points = 1  # Points which are given to the player for hitting one target, you can change it if you want
        self.canvas = canvas
        self.id = self.canvas.create_oval(0, 0, 0, 0)
        x = self.x = rnd(600, 760)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        color = self.color = 'red'
        self.vx = rnd(-5, 5)  # Random x velocity, you can change it if you want
        self.vy = rnd(-5, 5)  # Random y velocity, you can change it if you want
        self.canvas.coords(self.id, x - r, y - r, x + r, y + r)
        self.canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """When something hit the target"""
        self.canvas.delete(self.id)
        return self.points

    def move(self):
        """ Move the target after a unit of time.
            The method describes the movement of the target in one frame of the redraw. That is, updates the values
            self.x and self.y considering self speeds: self.vx and self.vy,
            and walls on the edges of the window (window size 800x600)."""
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
        if self.y + self.vy - self.r < 0:  # If target will touch "roof"
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
