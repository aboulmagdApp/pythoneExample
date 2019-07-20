x = 'outside'

def report():
    #Grap the global level of x
    global x
    print(x)
    #Reassign global variable
    x = 'inside'
    return x

print(report())
print(x)

#Local
def report_1():
    #local Assignment
    x = 'local'
    print(x)

#Enclosing
z = 'is the global level'

def enclosing():
   # z = 'Enclosing Level'

    def inside():
        print(z)

    inside()

enclosing()