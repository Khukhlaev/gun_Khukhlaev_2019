import math
from class_Ball import Ball


class Gun:
    def __init__(self, canvas):
        """Ball class constructor """
        self.fire_power = 10  # Power of the gun
        self.fire_on = False  # This flag indicates when new shot starts
        self.an = 1  # Angle of the gun
        self.bullet = 0  # Number of shots
        self.canvas = canvas
        self.id = self.canvas.create_line(20, 450, 50, 420, width=7)
        self.draw_new_ball = False  # This flag indicates when we should draw new ball
        self.new_ball = ""  # It will be reference to the new ball we should draw

    def fire_start(self, event):
        """ Make code known that the process of shooting started """
        self.fire_on = True

    def fire_end(self, event):
        """ Shot the ball.
        Happened when you release the mouse button.
        The initial values of the ball velocity components vx and vy depend on the position of the mouse."""
        self.bullet += 1
        vx = self.fire_power * math.cos(self.an)
        vy = self.fire_power * math.sin(self.an)
        self.new_ball = Ball(self.canvas, self.canvas.coords(self.id)[2], self.canvas.coords(self.id)[3], vx, vy)
        self.an = math.atan((event.y - self.new_ball.y) / (event.x - self.new_ball.x))
        self.fire_on = False
        self.fire_power = 10
        self.draw_new_ball = True

    def targeting(self, event=0):
        """Targeting. Depends on the position of the mouse. """
        if event:
            if event.x - 20 == 0:  # To prevent error division by zero
                event.x = 20.01
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.fire_on:
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
        self.canvas.coords(self.id, 20, 450,
                           20 + max(self.fire_power, 20) * math.cos(self.an),
                           450 + max(self.fire_power, 20) * math.sin(self.an)
                           )

    def power_up(self):
        """Increasing power of the gun, make the gun orange if there is process of shooting"""
        if self.fire_on:
            if self.fire_power < 100:
                self.fire_power += 1
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
