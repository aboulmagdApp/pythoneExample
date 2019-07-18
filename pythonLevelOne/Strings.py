#[start:stop;step]
mystring = "Hello world"

#if remove 0 from start the default will be 0
# print(mystring[0:7:2])
# print(mystring[:7:2])
print(mystring[::2])

#Revers string
print(mystring[::-1])

#concatenate strings
print(mystring+mystring)
print('hello ' + 'aboulmagd')

print(mystring.upper())
print(mystring.lower())

print(mystring.split())
# We can use a print statement to print a string.

print('Hello World 1')
print('Hello World 2')
print('Use \nto print a new line')
print('\n')
print('See what I mean?')


# We can also use a function called len() to check the length of a string!

print(len('Hello World'))

# Assign s as a string
s = 'Hello World'

#Check
s

# Print the object
print(s)

username = "aboulmagd"
color = 'blue'

print("the {} favorite is {}.".format(username,color))

print(f"the {username} choose {color}")