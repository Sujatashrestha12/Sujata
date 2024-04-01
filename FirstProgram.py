"""
#for range()to get range of number
for i in range(1, 21):
    if i % 3 ==0 and i % 5 ==0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
"""
    #nested loop
for i in range(1, 11):
        print("Multiplication table : ", i)
        for j in range(1, 11):
            print(i, "*", j,"=", i*j, end=" ")

a = ['red', 'blue', 'orange', 'black']
b = ['football', 'volleyball', 'basketball', 'baseball']
for i in a:
    for j in b:
         print(i, j, end=" ")
         
