# We just created a list of integers, but lists can actually
# hold different object types. For example:
myList = [1,100.2,'hello']
print(myList)

# to get len in list
print(len(myList))

myList1 = ['a','b','c','d','E','G']
myList1.append('z')
#print(myList1[1:4])
myList1.insert(1,'z')
print(myList1)

#pop for remove from list
popped_item = myList1.pop()

print(myList1)
print(popped_item)

mylist2 =[1,2,3]
mylist3 =[4,5,6]
mylist4 =[7,8,9]

mega_list = [mylist2,mylist3,mylist4]
print(mega_list)
print(mega_list[1][2])