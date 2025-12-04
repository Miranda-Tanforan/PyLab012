from simulation import Simulation
from solarsystem import SolarSystem
from sun import Sun
from planet import Planet

def main():


    solarsystem = SolarSystem()
    solarsystem.add_sun(Sun("sun", 12, 50000, 10000000, 0, 0))
    solarsystem.add_planet(Planet(name= "earth", radius= 10, mass= 5000, distance= 60, x= 100, y= 100, vel_x= 10, vel_y= 15))
    sim = Simulation(solarsystem,500,500,100)
    solarsystem.show_planets()
    sim.run()

if __name__ =='__main__':
    main()