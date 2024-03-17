# import math as mh

# print ("amin")
# print("mohammad amin")
# student_count = 30
# print(student_count)

# comment = "what is your name : "
# name = input(comment)
# print(f'I am {name}.')
# print(name[0:12:3])
# print("amin"[0:3]) 
# course = "python programming"
# print(course.upper())
# print(course.lower())
# print(course.count("P"))
# print(course.upper().strip())
# print(course.find("pro"))
# print(course.replace('p', 'z').upper())
# print('z' in course)
# print('l' not in course)

# #int
# x = 12
# # float 
# y = 67.09
# # complex
# z = 23 + 67j
# print(2e2)
# z = z + 4 + 78j
# print(z)

# print(round(2.3))
# print(mh)
# print(mh.log10(12)) 
# print(mh.ceil(90.090))
# # for learn all  math method you must go to the math python 3 madul
# print(mh.comb(3, 4))
# x = 45
# print(type(x).__name__)
# x = float()
# print(type(x).__name__)
# x = input('enter x : ')
# # y = int(x) + 45
# # print(type(x), type(y), y, sep="\t")
# x = int(x)
# x = bool(x)
# print(x)
# x = 10 > 34
# y = 78 < 89
# if not x is y:
#     print('yes')
# else :
#     print('no')
# print("mohammad" > "mohammad")



# x = 10 > 34
# y = 78 < 89
# if not x is y:
#     print('yes')
# else :
#     print('no')
# print("mohammad" > "mohammad")


# temp = int(input("who the wether : " ))
# if temp > 30:
#     print('hot')
# elif(20 < temp <= 30):
#     print("ok")
# else:
#     print("cold")

# age = int(input())
# if age > 18:
#     message = "Eligible"
# else :
#     message = "Not Eligible"

# print(message)

# age = int(input())
# message = "Eligible" if age > 18 else "Not Eligible"

# print(message)
# a = []
# for i in range(2, 34, 6):
#     a.append(i)

# print(a)
# succsesful = True
# for number in range(3):
#     print('try')
#     if succsesful:
#         message = "succsessfull"
#         break
#     else:
#         message = "Not succsessfull"
# print(message)
# for i in range(4):
#     for j in range(6):
#         print(f'{i} {j}')

# print(type(range(4)).__name__)

# numbers = int(input())
# while numbers > 0:
#     print(numbers)
#     numbers //= 2
# else:
#     print("finish ")

# command = ""
# while command.lower() != "exit":
#     try:
#         print(eval(command))
#     except:
#         print(command)
#     command = input(">>>")

# def name(name = None, age = 0):
#     return f"hi {age} years old {name}."

# # print(name("amin", 12))
# file = open("test.txt", "w")
# file.write(name("amin", 23))
# file = open("test.txt", "r")
# x = file.read()
# print(x)

# def emolument(hours, pay):
#     # 10 % of income
#     perc = ((hours * pay) / 100) * 10
#     real = hours * pay
#     return real - perc


# print(emolument(7, 8.00))
# def multiply(*numbers):
#     m = 1
#     for i in numbers:
#         m *= i
    
#     return m

# print(multiply(2, 5, 10, 190))
# def save_user(**user):
#     print(user)

# save_user(tr = 1, name = "ali", age = 90)

# message = 'a'
# def name(name):
#     global message
#     message = 'b'
# name("a")


# print(message)

# letters = ['a', 'b', 'c']
# print(letters)
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix)
# number = [0] * 12
# print(number)

# ran = list(range(89))
# # print(ran)
# le = list(range(len("amin")))
# print(len(le))

# x = list("mohammad amin baghyani")
# y, *z, g = x
# print(y, z, g)

# x = "mohammad amin baghyani"
# X = []
# for i in enumerate(x):
#     X.append(i)

# a, b, *c = X
# print(a, b, c)
# c = input()
# try:
#     print(x.count(c))
# except:
#     print("not exist")

# x = [1, 2, 4, 876543, 234, 0, 12]
# x .sort(reverse=True)
# print(x)


# x = [1, 2, 3, 4, 65, 5, 89, 6, 78, 7, 89, 89, 8, 9, 100000, 10, 0]
# print(sorted(x), x)
# x.sort()
# print(x)

# items = [
#     ("product1", 34),
#     ("product2", 45),
#     ("product3", 12)
# ]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)

# items.sort(key = lambda items: items[1])


# price = []
# # for item in items:
# #     price.append(item[1])

# # print(price)

# price = map(lambda items: items[1], items)
# filterd = filter(lambda item : item[1 ] <= 34, items)
# filterd = list(filterd)
# price = list(price)
# print(filterd)
# print(price)


# x = [item[1]*2 for item in items]
# print(x)
# y = [item[0] for item in items]
# print(y)

# x = [1, 2, 3]
# y = ['a', 'b', 'c']
# z = list(zip(y, x, "abc", '123'))
 
# print(z)

# points = 1, 2, 4, 5

# print(points)

# point = (1, 2, 3, 4, 5, 6)
# print(type(point[0]))
# x, y, z, *w = point

# print(x, y, z, w, sep="\t")


# x = 10
# y = 20

# x = x + y
# y = x - y
# x = x - y

# print(x, y)

# from array import array as ar

# x = ar('l', [1, 2, 3, 4, 5, 6])
# print(x[0])
# numbers = [1, 2, 1, 2, 1, 2, 3, 6, 7]
# uniq = set(numbers)

# print(uniq)

# first = {1, 2, 3, 4, 5, 5, 6, 5, 6, 5, 7}
# second = {7, 8, 7, 8, 9, 0, 9, 7, 8, 9, 9}
# al = (first | second)
# print(al)

# x = dict()
# x["name"] = "ali"
# x["age"] = 12
# x["gender"] = "male" 
# print(x)
# print(x.get("23", "not exist"))

# # del x["name"]
# # print(x)

# for i in x.items():
#     print(i)

# u = (x ** 2 for x in range(20))
# print(y)

# u = [x ** 2 for x in range(200)]
# for i in u:
#     print(i)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers) 

# numbers = [1, 2, 3, 4, 5]
# print(*numbers)

# name = input('enter name : ')
# print(*name)

# valus = list(range(2, 89, 2))
# print(*valus)

# valus = [*range(50)]
# print(valus)
# first = [1, 2, 3, 4, 5, 6, 7]
# secend = [8, 9, 10, 11, 12, 13, 14]

# full = [*first, *secend]

# print(full)

# x = {"x": 12, "y": 25}

# y = [i for i in x.items()]

# print(y)

# try :
#     inp = int(input())
#     print(inp)
# except:
#     print("enter a number.")  
# else:
#     print("enter another thing.")


# try:
#     x = open("amin.txt", "w")
#     x.write("amin")
#     age = int(input('how old are you : '))
#     sal = 10 // age
# except (ValueError, ZeroDivisionError) as ex:
#     print(ex) 
#     print("you didnt enter your age.")
# else:
#     print("every thing is good.")
# finally:
#     x.close()

# with open("amin.txt") as file:
#     print("file opened")


# print(
#     "amin"
# )

numbers = [x for x in range(90)]
print(*numbers)

dicts = {1: 1, 2 : 2, 3: 3}
print(*dicts)