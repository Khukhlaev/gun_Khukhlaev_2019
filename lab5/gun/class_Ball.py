from random import choice, randrange
import math


class Ball:
    def __init__(self, canvas, x, y, vx=0, vy=0, ):

        """ Ball class constructor
        Args:
        x - initial horizontal position of the ball
        y - initial vertical position of the ball
        vx - initial horizontal velocity of the ball
        vy - initial vertical velocity of the ball
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = vx
        self.vy = vy
        self.canvas = canvas
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def set_coords(self):
        self.canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Move the ball after a unit of time.
        The method describes the movement of the ball in one frame of the redraw. That is, updates the values
        self.x and self.y considering self speeds: self.vx and self.vy, the force of gravity acting on the ball,
        and walls on the edges of the window (window size 800x600).
        """
        self.vy += 1  # Gravity :)
        dx = 0
        dy = 0
        if self.x + self.vx - self.r < 10:  # If ball will touch left wall
            dx = self.x + self.vx - self.r - 10
            self.vx *= -10 / randrange(10, 20)
            self.vy *= 10 / randrange(10, 15)
        if self.x + self.vx + self.r > 790:  # If ball will touch right wall
            dx = self.x + self.vx + self.r - 790
            self.vx *= -10 / randrange(10, 20)
            self.vy *= 10 / randrange(10, 15)
        if self.y + self.vy + self.r > 590:  # If ball will touch "floor"
            dy = self.y + self.vy + self.r - 590
            self.vy *= -10 / randrange(20, 30)
            self.vx *= 10 / randrange(10, 20)
        self.x += self.vx - dx
        self.y += self.vy - dy
        self.set_coords()

    def hittest(self, obj):
        """The function checks whether this object is pushed against the target described in object obj.
        Args:
            obj: The object with which the collision is checked.
        Returns:
            Returns True in case of a collision of the ball and the goal. Otherwise returns False.
        """
        coords = self.canvas.coords(obj.id)
        radius = abs(1 / 2 * (coords[2] - coords[0]))
        obj_x = coords[0] + radius
        obj_y = coords[1] + radius
        if math.sqrt((obj_x - self.x) ** 2 + (obj_y - self.y) ** 2) <= self.r + radius:
            return True
        return False

    def check_for_death(self):
        """this """
        if abs(self.vx) < 1 and abs(self.vy) < 1.1 and self.y > 550:
            self.canvas.delete(self.id)
            return True
        return False
