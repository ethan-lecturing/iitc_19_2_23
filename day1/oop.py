import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_from_origin(self):
        return self.get_distance_from_other_point(Point(0, 0))

    def get_distance_from_other_point(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(3, 5)
p2 = Point(5, 2)
print(p1.get_distance_from_other_point(p2))
