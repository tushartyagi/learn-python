# Decorators in Python #

Decorators in Python are constructs that allow us to change the executing
functions or classes and make them behave differently from their usual self.

Usually when you want to change the way a function behaves, or maybe add to the
functionality of the function, there are chances that it demands change in the
body of the function. With decorators, there's a high chance that you can avoid
that.

We use functions in order to avoid repetitive code, any piece of code which
repeats itself multiple times is hidden behind a function. Using the same logic
if we have some code that is a part of multiple functions, and is independent
of the function's core behavior, can be hidden in a decorator.

### Useful Concepts ###

#### Functions as Objects ####

Python provides the functionality of treating functions as first class objects,
so anything that can be done with objects can be done with functions.
We can

a. Pass them around

	def f():
		print("foo")

	def execute_function(f):
		f()

	>>> execute_function(f)
	foo

b. Store them in tuples/lists

	def f():
		print("foo")

	def g():
		print("bar")
	
	def h():
		print("baz")
	
	>>> for function in (f, g, h):
		    function()
	foo
	bar
	baz

c. Add attributes

	def f():
		print("foo")

	f.__author__ = 'Me'

	>>> print(f.__author__)
	Me


#### Inner functions and closures ####
Functions can also contain other functions and these inner functions have
access to the data of the parent function.

	def outer(arg_outer):
		outer_data = "some data"
		def inner(arg_inner):
			print("arg_inner: ", arg_inner)
			print("arg_outer: ", arg_outer)
			print("arg_outer: ", outer_data)
		inner(12)

	>>> outer(21)
	12
	21
	some data

### Syntax ###
Decorators are just functions which take a function, modify and return it.
Returning a function is an  important aspect of decorating the function.
Whatever a decorator returns has to be callable, it can either be another
function, or a class which implements `__call__` method.

The syntax is straight forward:

	def deco(func):
		# Let new_func = do something to func
		return new_func

And we can use it like this:

	@deco
	def some_func(*args, **kwargs):
		pass

And behind the scenes, this happens:

	some_func = deco(some_func)

So the original function is replace with the modified function.

### Some examples which make sense ###
Let's just say that you have some very expensive functions which are
finding solutions to some of the greatest problems ever encountered by mankind.
These aren't called just like that since they're expensive computationally, and
hence we'll have to log each one of them.

One way of doing that is to add the logging statements inside each of the
functions, something like:

	def expensive_func_1():
		print("expensive_func_1 called at ", time.strftime("%H:%S:%M"))
		# do something expensive

	def expensive_func_2():
		print("expensive_func_2 called at ", time.strftime("%H:%S:%M"))
		# do something expensive

Now adding something like this has multiple bad things.
* We are going against the practice of DRY (Don't repeat yourself)
* The logging itself isn't required by the function to do its job, so it
shouldn't be part of it.

So we sense that it's repeated code, and repeated code needs to have a function
for itself. But function inside function?? Yes that's possible and we can have
something like:

	def log_it(func_name):
		print(func_name, " called at ", time.strftime("%H:%S:%M"))

	def expensive_func_1():
		log_it(expensive_func_1.__name__)
		# do something expensive

	def expensive_func_2():
		log_it(expensive_func_2.__name__)
		# do something expensive
	
But again, we are including something inside a function that shouldn't be part
of it. It's code inside a function that repeats itself, but isn't really needed
inside it. So in situations like these, we can start using generators.

	def log_it(func):
		def new_func():
			print(func.__name__, "started at ", time.strf_time("%H:%M:%S"))
			func()
		return new_func()

What happened? We just created a decorator.
Like I mentioned before, a decorator is a function which changes another
function, in a way enhances it's working. So this generator takes in an
expensive function and returns another function which
a. print the log time
b. calls expensive function.

And how's it different from the previous approach?
Because it's nicer to look, for starters. This is how we use it:

	@log_it
	def expensive_func_1():
		print("Running expensive_func_1")

	@log_it
	def expensive_func_2():
		print("Running expensive_func_2")


	>>> expensive_func_1()
	expensive_func_1 started at 21:36:03
	Running expensive_func_1

	>>> expensive_func_2()
	expensive_func_2 started at 22:36:03 # It's expensive
	Running expensive_func_2


While this doesn't seem much at such small scale, the most important point in 
the favor of decorators is that they are independent of function body. So, 
let's say you have to do some extra logging in one of the functions; with the
previous approach, we'll have to change the name of the function call inside
the expensive function, like:

	def expensive_func_2():
		better_log_it(expensive_func_2.__name__)
		# do something expensive
	
With generators, we don't have to touch the body of the expensive function:

	@better_log_it
	def expensive_func_2():
		# do something expensive
	
Still not impressed? Let's take the thing a bit further:

#### Decorator chaining ####
Decorator syntax is influenced by mathematical functions. In mathematics,
the statement: `h(g(f(x)))` means that function g will take the the output of
f, and function h will take use to the output of g for the calculation.

You can chain decorators as well:

	@h
	@g
	def f(x):
		# do something with x

This modifies the function f like this:

	f = h(g(f(x)))

### Passing arguments in decorators ###
