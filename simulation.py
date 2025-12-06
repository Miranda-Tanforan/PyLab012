from solarsystem import SolarSystem
from sun import Sun
from planet import Planet
import turtle

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods

        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._screen = turtle.Screen()
        self._screen.setup(width= self._width, height= self._height)
        self._screen.bgcolor("black")
        self._t.clear()



    def run(self):
        self._solar_system.show_planets()
        for _ in range(self._num_periods):

            self._solar_system.move_planets()
            self._solar_system.show_planets()
        self._screen.exitonclick()  #not freezing simulation when done in run method

    def __str__(self):
        return f'{SolarSystem}'




solar_system = SolarSystem()
simulation = Simulation(solar_system, 500, 500, 10000)

the_sun = Sun('Sun',5000,100000000000000,5800,0,0)
solar_system.add_sun(the_sun)

earth = Planet('Earth',50,100,75, 60,0,3,10,"green")
solar_system.add_planet(earth)

simulation.run()

