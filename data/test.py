# def sqr(n):
#     for i in range(1, n+1):
#         yield i*i
# a = sqr(3)
# print(next(a))
# print(next(a))
# print(next(a))

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"my name is {self.name}I am  {self.age} year old.")


# c = student("Ayush", 22)
# c.info()


# *args python Example :
# def sum(*args):
#     total = 0
#     for a in args:
#         total = total+a
#     print(total)


# sum(1, 2, 3, 4, 5)

# **kwargs in python Example :
# def show(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# show(A=1, B=2, C=4)

dict={'A':1,'B':2,'C':3,'D':4}
dict.pop('A')
print(dict)