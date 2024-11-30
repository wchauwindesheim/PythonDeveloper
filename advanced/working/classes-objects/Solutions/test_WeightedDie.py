from WeightedDie import WeightedDie
from collections import Counter

die = WeightedDie(weights=[1, 1, 1, 1, 1, 5])

die.roll()

# for i in range(100000):
#     roll = die.roll()

# c = Counter(die.rolls)
# c_sorted = sorted(c.items())
# print(c_sorted)