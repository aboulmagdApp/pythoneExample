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