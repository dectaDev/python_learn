import math as mh

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
# print(mh.comb())
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

x = [1, 2, 4, 876543, 234, 0, 12]
x .sort(reverse=True)
print(x)