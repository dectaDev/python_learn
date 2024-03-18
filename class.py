# name of class in first latter of part any word big and another small



# class Point:
#     help = "this a pointer"
#     def __init__(self, x = 0, y = 0):
#             self.x = x; self.y = y
#     def draw(self):
#         return (f'point({self.x}, {self.y})')
#     @classmethod
#     def zero(cls):
#         return Point(0, 0)
#     def __str__(self):
#         return f'{self.x}, {self.y}'
    
#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False
        
#     def __add__(self, other):
#         ret = Point(0, 0)
#         ret.x, ret.y = self.x + other.x, self.y + other.y

#         return ret
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


# cx = Point(1, 3)
# xc = Point(9, 3)

# print(cx + xc)


# class BagOfWord:
#     def __init__ (self):
#         self.__words = {}

#     def add(self, word):
#         self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1
#     def __getitem__(self, word):
#         return self.__words.get(word.lower(), 0)
#     def __setitem__(self, word, number):
#         self.__words[word.lower()] = number
#     def __len__(self):
#         return len(self.__words)
    
#     def __iter__(self):
#         return iter(self.__words)
    



    




# yt = BagOfWord()
# # yt.add("amin")
# # yt.add("Amin")
# # yt.add("amIn")
# # amin = yt["amin"]

# # print(yt.words)
# # print(yt["amin"])
# yt["amin"] = 90 

# print(yt["amin"])
# print(len(yt)) 
# print(yt.__words)

# ty = BagOfWord()
# ty.__words


# class product:
#     def __init__(self, price):
#         if price < 0 :
#             raise ValueError("price can not be less than 0")
#         else:
#             self.__price = price


# product = product(-10)

