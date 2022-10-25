# from collections import  namedtuple
#
# Vector = namedtuple("Vector", "x, y, z")
# v1 = Vector(10, 2, "abc")
# print(v1)
#
# x, y, z = v1
# print(x)


# Creating a class that behaves like a list in Python
#___________________________________________________________________________#


class Vector:


    def __init__(self, *xs):
        for x in xs:
            if not isinstance(x, float) and not isinstance(x, int):
                raise  TypeError("Vector co-ordinates must be real number")

        self.xs = xs


    def __repr__(self):
        return  f"Vector{self.xs}"


    def __len__(self):
        return  len(self.xs)

    def __getitem__(self, item):
        return  self.xs[item]




v1 = Vector(10, 5.0, 3.)
print(v1[0:2])

x, y, _ = v1
print(x, y)

