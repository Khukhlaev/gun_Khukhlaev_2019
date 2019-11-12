import tkinter as tk

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
score = 0
number_targets = 0
points = 0
id_points = ''  # It will be reference to the text object on the canvas which shows number of the points player has
game_over = False


def make_targets(number):
    return {Target(canv) for i in range(number)}


def game():
    """main function of the each iteration of the game, is called every 30 ms"""
    global gun, targets, balls, score, number_targets, points, game_over, id_points
    for b in balls:
        b.move()
        delete = ''  # It may will be reference to the target we should delete
        for t in targets:
            if b.hittest(t):
                points += t.hit()
                canv.itemconfig(id_points, text=points)
                delete = t
                score += 1
        if delete:  # If delete != '' so if there is target to delete
            targets.remove(delete)
        if b.check_for_death():
            balls.remove(b)
    for t in targets:
        t.move()
    canv.update()
    if gun.draw_new_ball:
        balls.append(gun.new_ball)
        gun.draw_new_ball = False
    gun.power_up()
    if score == number_targets:  # If player hits all targets
        canv.bind('<Button-1>', '')
        canv.bind('<ButtonRelease-1>', '')
        canv.create_text(400, 300, text='Вы уничтожили цели за ' + str(gun.bullet) + ' выстрелов', font='Arial 20')
        game_over = True
    if not game_over:
        root.after(30, game)
    if game_over:
        root.after(5000, new_game)


def new_game():
    """this function starts new iteration of the game, is called 5 seconds after iteration finished"""
    global gun, targets, number_targets, score, balls, game_over, id_points
    canv.delete(tk.ALL)
    id_points = canv.create_text(30, 30, text=str(points), font='Arial 18')
    game_over = False
    score = 0
    gun = Gun(canv)
    balls.clear()
    canv.create_line(10, 0, 10, 590)
    canv.create_line(10, 590, 790, 590)
    canv.create_line(790, 0, 790, 590)
    canv.bind('<Button-1>', gun.fire_start)
    canv.bind('<ButtonRelease-1>', gun.fire_end)
    canv.bind('<Motion>', gun.targeting)
    number_targets = 2  # You can change number of targets if you want
    targets.clear()
    targets = make_targets(number_targets)
    game()


new_game()

root.mainloop()
