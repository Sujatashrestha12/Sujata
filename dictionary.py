#dictionary
"""
dictionary = {}
dictionary["name"]= "Ram"
dictionary["age"]=18
dictionary['Subject']=['Math', 'Science', 'Nepali']
dictionary ['education']= {'School':{
    'name': 'Xavier School',
    'address': 'Kalopul, Kathmandu'
},
'High School':{'name': 'DAV College',
               'address' : 'Jawlakhel, Lalitpur'},
'Bachelor level' : {
    'name': 'Xavier College',
    'address': 'Boudha, Kathmandu'
            }
}
print(dictionary)

for i in dictionary.keys():
    print(i)
for i in dictionary['Subject']:
    print(i)
for i in dictionary['education']:
    print(i)

#accessing the element of nested dictionary from the loop
for i, j in dictionary['education'] ['School'].items():
    print(i, "=", j )

#dictionary = [key: {nestkey: {subnestedkey:}]
    print(dictionary ['education'] ['School'] ['name'])

  #while loop  
    x = 0
    while x<=10:
       j=0
       while j<=10:
           print(x, "*", j, "=", x*j)  
           j+=1  
           x+=1    

#while loop inside for loop
for x in range(1, 11):
   print("Multiplication table: ", x)
   j= 1 
   while j <=10:
       print(x, "*", j, "=", x*j)
       j+=1
"""
#for loop inside while loop
x = 1
while x <= 10:
    print("Multiplication table: ", x)
    for j in range(1, 11):
        print(x, "*", j, "=", x*j)
    x += 1



