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


def entryExit(f):
    def g():
        print("Entering ", f.__name__)
        f()
        print("Exiting ", f.__name__)
    return g


class  decoratorWithoutArgument(object):

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

        
@entryExit
def func1():
    print("Inside func1()")


@entryExit
def func2():
    print("Inside func2()")


@decoratorWithoutArgument
def func3(a1, a2, a3, a4):
    print("func3 arguments")
    print(a1, a2, a3, a4)

print("After decoration")
print("First call to func3")
func3("This", "is", "his", "shit")
print("Second call to func3")
func3("another", "one of", "his", 'shit')
print("done")
    
