from random import choice
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
        # TODO :написать нормальный мув для шариков (с гравттыйией и тд)
        if (self.x <= 0 and self.vx < 0) or (self.x >= 780 and self.vx > 0):
            self.vx = -self.vx / 3
        if self.y >= 570 and self.vy > 0:
            self.vy = -self.vy / 2
        if self.y >= 570 and abs(self.vy) < 1:
            self.y = 569
            self.vy = 0
        self.vy += 1
        self.x += self.vx
        self.y += self.vy
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
        if abs(self.vy) < 1.1 and self.y > 550:  # TODO: исправить этот иф!!!
            self.canvas.delete(self.id)
            return True
        return False
