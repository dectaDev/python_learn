class Point:
    number_of_atributte = 2
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @classmethod
    def zero(self):
        return self(0, 0)
    def __str__(self):
        return f'{self.__x}, {self.__y}'
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
    def __gt__(self, other):
        return self.__x > other.__x or self.__y > other.__y
    
    
y = Point(2, 3)
x = Point(3, 4)
print(x < y)

x = (2, 3)
print(x)
print(type(x))