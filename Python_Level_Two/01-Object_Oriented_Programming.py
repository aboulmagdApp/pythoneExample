# mylist = [1,2,3]

# mylist.append(4)

# print(mylist)
# print(type(mylist))
# print(type(23.9))

class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

#x = Dog('lab')
x = Dog('Huski','Sammy')
print(x.breed)
print(x.name)
print(x.species)

class circle():
    pi=3.14
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * self.pi
    def circumfrance(self):
        return 2 * self.pi * self.radius

mycircle = circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumfrance())