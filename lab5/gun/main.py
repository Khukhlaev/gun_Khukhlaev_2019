from random import randrange as rnd
import tkinter as tk
import math
import time
from class_Ball import Ball

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Gun:
    def __init__(self, canvas):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...
        self.canvas = canvas
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши."""
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.canvas)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) / 2
        new_ball.vy = - self.f2_power * math.sin(self.an) / 2
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 760)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        color = self.color = 'red'
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        if self.x >= 800 or self.x <= 0:
            self.vx = -self.vx
        if self.y >= 600 or self.y <= 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        canv.move(self.id, self.vx, -self.vy)


def make_targets(number):
    goals = {Target() for i in range(number)}
    for t in goals:
        t.new_target()
    return goals


# make global variabales

targets = []
balls = []
gun = Gun(canv)
score = 0
bullet = 0


def game():
    """main function of the game"""
    global gun, targets, balls, score, bullet
    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t):
                t.live = 0
                t.hit()
                score += 1
        if b.check_for_death():
            balls.remove(b)
    if score == len(targets):
        canv.bind('<Button-1>', '')
        canv.bind('<ButtonRelease-1>', '')
    #        canv.itemconfig(canv, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
    canv.update()
    for t in targets:
        t.move()
    gun.targetting()
    gun.power_up()
    root.after(20, game)


def new_game():
    global gun, targets
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)
    targets = make_targets(2)
    game()
    canv.delete(gun)


new_game()

root.mainloop()
