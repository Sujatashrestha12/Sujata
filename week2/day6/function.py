# #function is a block of code. We use function to reuse the code. Two types of function.
# #1. BUILT -IN function
# #2. User defined function
# #def function_name():
#  #   function body

# #function()
# #positional arguments- takes value according to position.

# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello('Ram', 'Python with django')# Argument

# #keyword Arguemnets - takes value according to keywords.
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello(course_name='Python with django',name= 'Ram')# Argument

# #default arguments
# def hello(name, course_name= "Python with django"): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)

# hello(course_name='Python with Data Science', name="Ram")# Argument

# def sum(a, b, c):
#     total = a + b+ c
#     return total #return gives result of function and stop the execution of function.

# result = sum(2, 3, 5)
# print(result)

# def sum(*args):
#     total = args[0]+ args[1]+ args[2]
#     return total

# result = sum(2,3,5)
# print(result)

# # arbitratry arguments- *args
# def sum(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# result = sum(2,3,5)
# print(result)

# #arbitray keywords arguments - "kwargs"
# def hello(**kwargs):#parameter
#     print("Hello", kwargs["name"], "Welcome to Web development Training")
#     print(kwargs['course_name'])

# hello(name='Ram', course_name= 'Python with django', another_course= 'Python with Data Science')# Argument


# l = float(input("Enter a length: "))
# w = float(input("Enter a width: "))

# def area():
#     global area_of_object
#     area_of_object = l*w
#     return area_of_object

# def volume():
#     h= float(input("Enter a height: "))
#     v= area_of_object*h
#     return v

# result = area()
# result_volume = volume()
# print(result)
# print(result_volume)
# """
#lambda function: the function without name. it is used for instant use and its one-time uses. lambda keyword is used.

# x = lambda a, b: a*b
# area = x(2,3)
# print(area)


# #recursive function- function calling itself again and again
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))

# def add(n1, n2):
#     return n1+n2
# print(add(10, 20))

# add = lambda n1, n2 : n1+n2
# print(add(10,20))

#map function


