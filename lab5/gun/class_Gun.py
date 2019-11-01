import math
from class_Ball import Ball


class Gun:
    def __init__(self, canvas):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.bullet = 0
        self.canvas = canvas
        self.id = self.canvas.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...
        self.draw_new_ball = False
        self.new_ball = ""

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """ Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши. """

        self.new_ball = Ball(self.canvas, self.canvas.coords(self.id)[2], self.canvas.coords(self.id)[3])
        self.new_ball.r += 5
        self.bullet += 1
        self.an = math.atan((event.y - self.new_ball.y) / (event.x - self.new_ball.x))
        self.new_ball.vx = self.f2_power * math.cos(self.an)
        self.new_ball.vy = self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        self.draw_new_ball = True

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
        self.canvas.coords(self.id, 20, 450,
                           20 + max(self.f2_power, 20) * math.cos(self.an),
                           450 + max(self.f2_power, 20) * math.sin(self.an)
                           )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
