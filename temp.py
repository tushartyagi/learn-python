def outer(outer_arg):
    def inner(inner_arg):
        print(inner_arg)
        print(outer_arg)
    inner(12)

#outer

def fib(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def log_expensive(expensive_func):
    def new_func():
        print(expensive_func.__name__, "started at ", time.strftime("%H:%M:%S"))
        expensive_func()
    return new_func

@log_expensive
def expensive_func():
    print("Expensive function")

expensive_func()
