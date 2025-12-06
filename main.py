from simulation import Simulation
from solarsystem import SolarSystem
from sun import Sun
from planet import Planet

def main():
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, 500, 500, 10000)

    the_sun = Sun('Sun', 5000, 100000000000000, 5800, 0, 0)
    solar_system.add_sun(the_sun)

    earth = Planet('Earth', 50, 100, 75, 60, 0, 3, 10, "green")
    solar_system.add_planet(earth)

    simulation.run()

if __name__ =='__main__':
    main()