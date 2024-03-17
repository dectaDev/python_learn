# name of class in first latter of part any word big and another small



class Point:
    help = "this a pointer"
    def __init__(self, x = 0, y = 0):
            self.x = x; self.y = y
    def draw(self):
        return (f'point({self.x}, {self.y})')
    @classmethod
    def zero(cls):
        return Point(0, 0)
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    def __add__(self, other):
        ret = Point(0, 0)
        ret.x, ret.y = self.x + other.x, self.y + other.y

        return ret
# x = Point()
# x.draw()
# print(type(x))

# y = isinstance(x, Point)

# print(y)
        
# cx = Point(1, 2)

# print(cx.draw())
# cx.z = 12
# cx.draw()
# print(cx.help)

# xc =  Point()

# Point.help = 90
# print(Point.help, cx.help, xc.help
#       )
    
# p = Point.zero()
# print(p.draw())
    
print("magic metode see in google")

# cx = Point()
# print(cx)


cx = Point(1, 3)
xc = Point(9, 3)

print(cx + xc)
