# #exception -> an event that occurs to disrupt the flow of operation.
# try:
#     age = int(input("Enter the age: "))
#     print(age)
# except:
#     print("please provide numeric value")

# print('Xavier College')

# try:
#     a = int(input("Enter the value: "))
#     b = int(input("Enter the value: "))
#     c = a/b
# except ValueError:
#     print("Please provide numeric value")
# except ZeroDivisionError:
#     print('Zero will not divide any other number')
# else:
#     print('The value of c is:',c)
def login():
    user1 = 'admin'
    pass1 = 'admin'
    try: 
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if user1 != username:
            raise ZeroDivisionError
        elif pass1 != password:
            raise ValueError
        
    except ZeroDivisionError:
        print("Username is invalid")
    except ValueError:
        print("Password is invalid")
        login()
    else:
        print("login successful")
    finally:
        print("Home")
    login()