class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle as ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle as ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
    """Implementation-independent abstraction: for example, there could ..."""

    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another ..."""
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        """Implementation-independent"""
        self.radius *= percent


# Build the first circle object using API one
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# draw a circle
circle1.draw()
# Build the second circle object using API two
circle2 = Circle(1, 2, 3, DrawingAPITwo())
# draw a circle
circle2.draw()
