seq = [1,2,3,4,5,6,7]

for item in seq:
    print(item)

mystring = 'hello'

for char in mystring:
    print(char)

salaries = {'aboulmagd':500,'Ahmed':200,'Eman':600,'Lisa':900}

for employee in salaries:
    print(employee)
    print("has salary of: ")
    print(salaries[employee])

mypairs = [('a',1),('b',2),('c',3)]

for letter,num in mypairs:
    print(letter)

#while loop

i = 1
while i < 5:
    print("i is currently: {}".format(i))
    i = i + 1

#range

for x in range(1,10,2):
    print(x)

result = list(range(0,11,2))
print(result)

print(1 in [1,2,3,4])


