import math


class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)

    def calc_area(self):
        area = (self.radius) ** 2 * math.pi
        return area


x = Circle(5)
print(x.calc_area())
