#!/usr/bin/env python3


class MyDecorator(object):

    def __init__(self, f):
        print("Inside MyDecorator.__init__")
        f()

    def __call__(self):
        print("Inside MyDecorator.__call__")


# Decorating a function calls the __init__ method
# @MyDecorator
# def aFunction():
#     print("Inside aFunction")

# print("Finished decorating aFunction")

# At this point, the function is decorated and hence __call__ method of the
# class is called.
# aFunction()


class EntryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering ", self.f.__name__)
        self.f()
        print("Exiting ", self.f.__name__)

# The object a decorator returns has to be callable, in class based
# implementation, we are providing a __call__ method and hence the
# execution logic is built right inside of it. In the same spirit,
# a decorator function has to return a function.
def entryExit(f):
    def g():
        print("Entering ", f.__name__)
        f()
        print("Exiting ", f.__name__)
    return g

@entryExit # -- The value of entryExit is used as a decorator
def func4(): pass


class decoratorWithoutArgument(object):

    def __init__(self, f):
        # If there are no arguments, the function
        # to be decorated is passed to the constructor.
        print("inside __init__")
        self.f = f

    def __call__(self, *args):
        # The call method isn't called until the
        # decorated function is called.
        print("Inside __call__")
        self.f(*args)
        print("After self.f(*args)")


class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        # The function isn't passed to init if there
        # are arguments in the decorator
        print("Inside init")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        # If there are args, the function is passed to the call
        # method. __call__() is only called once, as part of the
        # decoration process. The only argument it accepts is the
        # function object
        print("Inside call")
        def wrapped_f(*args):
            print("Inside wrapped_f")
            print("Decorator args: ", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

        
    
def fDecoratorWithArguments(arg1, arg2, arg3):
    print("inside init")
    def decoratorWithArguments(func):
        print("inside call")
        def wrapped_f(*args):
            print("inside wrapped_f")
            print("decorator args: ", arg1, arg2, arg3)
            func(*args)
            print("after f(args)")
        return wrapped_f
    return decoratorWithArguments

# The value returned by fDecoratorWithArguments is used as a decorator
@fDecoratorWithArguments("Hello", "World", 42) 
def func3(a1, a2, a3, a4):
    print("func3 arguments")
    print(a1, a2, a3, a4)

print("After decoration")
print("First call to func3")
func3("This", "is", "his", "shit")
print("done")
