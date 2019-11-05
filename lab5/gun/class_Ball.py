from random import choice, randrange
import math


class Ball:
    def __init__(self, canvas, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
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
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy += 1
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
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        coords = self.canvas.coords(obj.id)
        radius = abs(1 / 2 * (coords[2] - coords[0]))
        obj_x = coords[0] + radius
        obj_y = coords[1] + radius
        if math.sqrt((obj_x - self.x) ** 2 + (obj_y - self.y) ** 2) <= self.r + radius:
            return True
        return False

    def check_for_death(self):
        if abs(self.vx) < 1 and abs(self.vy) < 1.1 and self.y > 550:
            self.canvas.delete(self.id)
            return True
        return False
