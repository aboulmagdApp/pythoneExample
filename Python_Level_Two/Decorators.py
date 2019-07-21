def hello(name='Jose'):
    print('the hello func() has been run!')

    def greet():
       return "    this is inside greet()"
    def welcome():
        return "       this is inside welcome"

    if name == 'Jose':
        return greet
    else:
        return welcome
x = hello()
print(x())

def new_decorator(func):

    def wrap_func():
        print("some code before executing func")
    
    func()

    print("some code after executing func")

    return wrap_func

@new_decorator
def func_need_decorator():
    print("please decorate me!!")

func_need_decorator()