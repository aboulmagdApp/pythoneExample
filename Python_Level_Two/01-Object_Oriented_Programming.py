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

#Inheritance

class Animal():
    def __init__(self,fav):
        self.fav = fav
    
    def report(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self,fav):
        Animal.__init__(self,fav)
        print("Dog Created")
    def report(self):
        print('I am a dog')


d = Dog('buzzy')
d.report()
d.eat()
print(d.fav)

###################
# Special Methods
###################


class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        # Notice how this is return, NOT print()
        return f"Title:{self.title} , author:{self.author}, pages:{self.pages}"

    def __len__(self):
        return self.pages


book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))



