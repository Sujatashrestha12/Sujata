import os,shutil
#file handling -> files can be opened, closed, maintained, read, write.


# my_file = open('test.txt')
# print(my_file)
# print(my_file.read()) # to read the text file
# print(my_file.writable()) #to check whether to write in file or not
# print(my_file. close()) # closing the file

# my_another_file = open('test.txt', 'r+') # 'r+' - to make it writable
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write("Ram \n")

# my_file = open('test.txt')
# print(my_file)
# print(my_file.read()) # to read the text file
# print(my_file.writable()) #to check whether to write in file or not
# print(my_file. close()) # closing the file

# my_another_file = open('test.txt', 'w+')
# print(my_another_file.read())
# print(my_another_file.readable())
# print(my_another_file.writable())

# my_another_file.write("Ram \n")
# print(my_another_file.seek(2))
# print(my_another_file.read())

my_next_file = open('next.txt', 'a+')
print(my_next_file.writable())
print(my_next_file.readable())
print(my_next_file.write("Hello \n World \n "))

print(my_next_file. seek(0))
print(my_next_file.read())
list1= ['\nRam \n', '\nShyam \n', '\nHari']
print(my_next_file. writelines(list1))
print(my_next_file.seek(0))
print(my_next_file.readline())
print(my_next_file.readlines())

# # shutil.copy('next.txt', 'next1.txt')
# os.remove('next1.txt')

shutil.move('test.txt', 'next1.txt')