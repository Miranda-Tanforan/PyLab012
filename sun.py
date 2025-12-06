import turtle


class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: int, y: int):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._temp = temp
        self._x = x
        self._y = y

        self._t = turtle.Turtle()
        self._t.color("yellow")
        self._t.shape("circle")
        self._t.goto(self._x, self._y)
        #self._t.penup()
        #self._t.pendown()


    def get_mass(self) -> float:
        return self._mass

    def get_x_pos(self) -> int:
        return self._x

    def get_y_pos(self) -> int:
        return self._y

    def __str__(self) -> str:
        return f"{self._name}, mass={self._mass}, radius={self._radius}, temp={self._temp}, position=({self._x}, {self._y}"




