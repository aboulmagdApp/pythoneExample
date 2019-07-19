# ** Default arguments can be used to set a default value. **
def report_person(name='Blank'):
    #print("reporting {}".format(name))
    print("reporting " + name)
report_person()


def add_num(num1,num2):
    return num1 + num2

result = add_num(5,11.9)
print(result + 10)

#Max and Min

print(min([1,2,3,4,5,6,7,8,9,10]))
print(max([1,2,3,4,5,6,7,8,9,10]))

#enumerate
mylist = ['a','b','c','d']
index = 0
for letter in mylist:
    print(letter)
    print("is at index : {}".format(index))
    index = index + 1
    print('')

#when using enum function
for index,item in enumerate(mylist):
    print(item)
    print("is at index : {}".format(index))
    print('')


#join
print('-'.join(mylist))

def secret_check(mystring):
    return 'secret' in mystring.lower()
       

result = secret_check('simple a Secret')
print(result)

def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output

print(code_maker('aboulmagd'))

def even_check(num):
    if num % 2 == 0:
        print("Number was even")
    else:
        print("Odd number")
even_check(7)