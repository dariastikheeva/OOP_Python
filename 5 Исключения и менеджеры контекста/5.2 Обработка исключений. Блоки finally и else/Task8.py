class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.__top = ((self._x, self._y), (self._x + self._width, self._y))
        self.__botom = (
            (self._x, self._y + self._height),
            (self._x + self._width, self._y + self._height),
        )
        self.__left = ((self._x, self._y), (self._x, self._y + self._height))
        self.__right = (
            (self._x + self._width, self._y),
            (self._x + self._width, self._y + self._height),
        )

    def __setattr__(self, key, value):
        if key in ('_x', '_y'):
            if not isinstance(value, (int, float)):
                raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height'):
            if value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        super().__setattr__(key, value)

    def __eq__(self, rect):
        if (
            self._x == rect._x
            and self._y == rect._y
            and self._width == rect._width
            and self._height == rect._height
        ):
            return True
        return False

    def is_collision(self, rect):
        if not (
            self.top[0][1] > rect.botom[1][1]
            or self.botom[1][1] < rect.top[0][1]
            or self.left[0][0] > rect.right[1][0]
            or self.right[1][0] < rect.left[0][0]
        ):
            raise TypeError('прямоугольники пересекаются')

    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self, value):
        self.__top = value

    @property
    def botom(self):
        return self.__botom
    @botom.setter
    def botom(self, value):
        self.__botom = value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for rect in lst_rect:
    try:
        for other in lst_rect:
            if other != rect:
                rect.is_collision(other)
    except TypeError:
        pass
    else:
        lst_not_collision.append(rect)
