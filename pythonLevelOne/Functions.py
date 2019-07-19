# ** Default arguments can be used to set a default value. **
def report_person(name='Blank'):
    #print("reporting {}".format(name))
    print("reporting " + name)
report_person()


def add_num(num1,num2):
    return num1 + num2

result = add_num(5,11.9)
print(result + 10)