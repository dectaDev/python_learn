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
    def __ne__(self, other):
        return self.__x != other.__x or self.__y != other.__y
    def __lt__(self, other):
        return self.__x < other.__x and self.__y < other.__y
    def __le__(self, other):
        return self.__x <= other.__x and self.__y <= other.__y
    def __ge__(self, other):
        return self.__x >= other.__x and self.__y >= other.__y
    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)
    

