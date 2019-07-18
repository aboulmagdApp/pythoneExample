d = {'Key1':'value1','Key2':'value2'}
print(d)
print(d['Key1'])

salaries = {'aboulmagd':20,'Ahemd':30,'Noha':45}
salaries['candy'] = 100
print(salaries['aboulmagd'])

salaries['aboulmagd'] = salaries['aboulmagd'] + 40

print(salaries['aboulmagd'])

pepole = {'john':[1,2,3],'Sally':[4,50,6]}
print(pepole)
print(pepole['Sally'])
print(pepole['Sally'][1])

#nested list
pepole1 = {'john':{'salary':1500,'age':36}}
print(pepole1)
print(pepole1['john']['age'])


d1 = {'k1':10,'K2':20,'k3':30}
print(d1.keys())
print(d1.values())
print(d1.items())