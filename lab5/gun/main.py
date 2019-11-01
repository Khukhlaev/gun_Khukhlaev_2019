import tkinter as tk
from class_Ball import Ball
from class_Gun import Gun
from class_Target import Target

# make window
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

# make global variables

targets = []
balls = []
gun = Gun(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
score = 0


def make_targets(number):
    goals = {Target(canv) for i in range(number)}
    return goals


def game():
    """main function of the game"""
    global gun, targets, balls, score, screen1
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
        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(gun.bullet) + ' выстрелов')
    canv.update()

    for t in targets:
        t.move()
    if gun.draw_new_ball:
        balls.append(gun.new_ball)
        gun.draw_new_ball = False
    gun.power_up()
    root.after(30, game)


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
