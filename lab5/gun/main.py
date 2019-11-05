import tkinter as tk
from time import sleep

from class_Ball import Ball
from class_Gun import Gun
from class_Target import Target

# make window
root = tk.Tk()
root.title('The Gun Game')
root.resizable(0, 0)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

# make global variables

targets = []
balls = []
gun = ""
screen1 = canv.create_text(400, 300, text='', font='28')
score = 0
number_targets = 0


def make_targets(number):
    return {Target(canv) for i in range(number)}


def game():
    """main function of the game, is called every 30 ms"""
    global gun, targets, balls, score, screen1, number_targets
    for b in balls:
        b.move()
        delete = ''
        for t in targets:
            if b.hittest(t):
                t.hit()
                delete = t
                score += 1
        if delete:
            targets.remove(delete)
        if b.check_for_death():
            balls.remove(b)
    if score == number_targets:
        canv.bind('<Button-1>', '')
        canv.bind('<ButtonRelease-1>', '')
        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(gun.bullet) + ' выстрелов')
    for t in targets:
        t.move()
    canv.update()
    if gun.draw_new_ball:
        balls.append(gun.new_ball)
        gun.draw_new_ball = False
    gun.power_up()
    root.after(30, game)


def new_game():
    global gun, targets, number_targets, score, balls
    # canv.delete(ALL)??????????????
    score = 0
    if gun:
        canv.delete(gun.id)
    gun = Gun(canv)
    balls.clear()
    canv.create_line(10, 0, 10, 590)
    canv.create_line(10, 590, 790, 590)
    canv.create_line(790, 0, 790, 590)
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)
    number_targets = 2  # You can change number of targets if you want
    targets.clear()
    targets = make_targets(number_targets)
    game()
    root.after(10000, new_game)


new_game()

root.mainloop()
