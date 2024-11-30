from collections import Counter
from WeightingDie import WeightingDie

die = WeightingDie()

for i in range(10000):
    roll = die.roll()

c = Counter(die.rolls)
c_sorted = sorted(c.items())
print(c_sorted)