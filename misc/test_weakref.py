import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbor = None  # Could form a cycle

a = Node(1)
b = Node(2)

# Create a circular reference
a.neighbor = b
b.neighbor = a

# Use weak references to break the cycle
a.neighbor = weakref.ref(b)
b.neighbor = weakref.ref(a)
