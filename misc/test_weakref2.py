class Node:
    def __init__(self, value):
        self.value = value
        self.neighbor = None

a = Node(1)
b = Node(2)

# Circular reference
a.neighbor = b
b.neighbor = a

# Delete strong references
del a
del b

# Objects are still in memory because of the circular reference
import gc
print(gc.garbage)  # Objects with circular references may still exist
