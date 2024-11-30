from Die1 import Die
from Simulation import Simulation

die = Die()

sim = Simulation(die.roll, 1000)

print(sim.mean)

print(sim.median)

print(sim.mode)

