username = 'Admin'
check = 'Admin1'

if username == check and 1 == 1:
    print('Access Granted!')
elif 1 == 3:
    print('Middel condiiotion is True')
elif 4 == 4:
    print('third condiotion is True')
else:
    print('conditions not True')

username = "aboulmagd"
permission = False

if username == 'admin' and permission:
    print('Full Access')
elif username == 'admin' and permission == False:
    print('Admin Access only, Not Full Permission')
else:
    print('No Access')