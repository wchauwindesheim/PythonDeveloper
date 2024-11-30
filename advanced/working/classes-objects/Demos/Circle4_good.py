import math

class Circle:
    def __init__(self, val, prop='r'):
        # Initialize default values to prevent AttributeError
        self._radius = 0
        self._diameter = 0
        self._circumference = 0
        self._area = 0

        # Set the correct value based on `prop`
        if prop == 'r':
            self.radius = val
        elif prop == 'd':
            self.diameter = val
        elif prop == 'c':
            self.circumference = val
        elif prop == 'a':
            self.area = val
        else:
            raise ValueError("prop must be 'r', 'd', 'c', or 'a'")

    def resize_by(self, amount):
        """Resize the radius by a percentage."""
        self.radius *= (1 + amount)  # Use the radius setter

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @radius.setter
    def radius(self, r):
        """Setter for radius. Updates all dependent attributes."""
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi

    @property
    def diameter(self):
        """Getter for diameter."""
        return self._diameter

    @diameter.setter
    def diameter(self, d):
        """Setter for diameter. Updates radius and all dependent attributes."""
        self.radius = d / 2  # Updates everything via radius setter

    @property
    def circumference(self):
        """Getter for circumference."""
        return self._circumference

    @circumference.setter
    def circumference(self, c):
        """Setter for circumference. Updates radius and all dependent attributes."""
        self.radius = c / (2 * math.pi)  # Updates everything via radius setter

    @property
    def area(self):
        """Getter for area."""
        return self._area

    @area.setter
    def area(self, a):
        """Setter for area. Updates radius and all dependent attributes."""
        self.radius = (a / math.pi) ** 0.5  # Updates everything via radius setter
