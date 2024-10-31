# Python

[Back Home](/)

# Object Orientated Programming

- [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming), or "OOP", is a pattern or [[Paradigm]] for writing clean and maintainable code. Not everyone _agrees_ that object-oriented principles are the best way to write code, but, to be a good engineer, you should at least understand them.
- `Clean Code` is code that is easy for humans to understand. 
    - `Any fool can write code that a computer can understand. Good programmers write code that humans can understand.`

## Classes

- A [class](https://docs.python.org/3/tutorial/classes.html) is a special type of value in an object-oriented programming language like Python. It's similar to a dictionary in that it usually stores other types inside itself.
- Just like a string, integer or float, a class is a _type_, but instead of being a built-in type, your classes are custom types that you define.
- An object is just an [instance](https://stackoverflow.com/questions/20461907/what-is-meaning-of-instance-in-programming) of a class type.

### Methods

- A [method](https://docs.python.org/3/tutorial/classes.html#method-objects) is a function that's tied directly to a class and has access to all its properties.
- If a normal function doesn't return anything, it's typically not a very useful function. In contrast, methods often don't return anything explicitly because they can mutate the properties of the object instead.

### Self

- Methods are nested within the `class` declaration. Their first parameter is always the instance of the class that the method is being called on. By convention, it's called ["self"](https://docs.python.org/3/glossary.html#term-method). Because `self` is a reference to the object, you can use it to read and update the properties of the object.

### Constructors

- A [constructor](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)) is used to define how objects of a class will be instantiated.
- In Python, if you name a method [`__init__`](https://docs.python.org/6/reference/datamodel.html#object.__init__), that's the constructor and it is called when a new object is created.

## Four Pillars of OOP

### Encapsulation

- [Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) is the practice of hiding complexity inside a ["black box"](https://en.wikipedia.org/wiki/Black_box) so that it's easier to focus on the problem at hand.
- Encapsulation does not make code more secure, it is more about organisation.
- The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.
- Python is a dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards that languages like [Go](https://go.dev/) do. That's why encapsulation in Python is achieved mostly by [convention](https://en.wikipedia.org/wiki/Coding_conventions) rather than by _force_. Prefixing methods and properties with a double underscore is a _strong_ suggestion to the users of your class that they shouldn't be touching that stuff.

#### Public and Private

- By default, all properties and methods in a class are _public_. That means that you can access them with the `.` operator.
- [Private](https://docs.python.org/3/tutorial/classes.html#tut-private) data members are how we encapsulate logic and data within a class. To make a property or method private, you just need to prefix it with two underscores.

### Abstraction

#### Abstraction vs encapsulation

- Abstraction is about _creating a simple interface for complex behaviour._ It focuses on what's exposed.
- Encapsulation is about _hiding internal state._ It focuses on tucking implementation details away so no one depends on them.
- Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.

### Inheritance

- [Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) allows one class, the "child" class, to _inherit_ the properties and methods of another class, the "parent" class.
- Inheritance is a powerful tool, but it is a _really_ bad idea to try to overuse it. Inheritance should only be used when all instances of a child class are also instances of the parent class.
- A good child class is a strict [subset](https://en.wikipedia.org/wiki/Subset) of its parent class.
- Inheritance has no limit as to how deep it can run - don't go overboard.
- Usually, inheritance hierarchies form trees, not lines. A parent class can have multiple children.

### Polymorphism

- Polymorphism is the ability of a variable, function or object to take on multiple forms.
- Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).
- A **function signature** (or method signature) includes the name, inputs, and outputs of a function or method. For example, `hit_by_fire` in the `Human` and `Archer` classes have identical signatures.

#### Overriding

- Method overriding, in object-oriented programming, is **a language feature that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super classes or parent classes**.
- If you change the function signature of a parent class when overriding a method, it could be a disaster. The whole point of overriding a method is so that the caller of your code _doesn't have to worry_ about what different things are going on inside the methods of different object types.

#### Operator Overloading

- Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the `+` operator works for built-in types like integers and strings.
- Custom classes don't support the "+" operation *EG: Shape + Shape*
- However, we can add our own support! If we create an `__add__(self, other)` method on our class, the Python interpreter will use it when instances of the class are being added with the `+` operator. Here's an example:

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)
p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
```

- To make instances of an object to print themselves: The [`__str__`](https://docs.python.org/3/reference/datamodel.html#object.__str__) method (short for "string") lets us do just that. It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's `print()` function.
- _Note: the [`__repr__`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) method works in a similar way, you'll see it from time to time._

# Functional Programming

## What is FP

Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming) is more about declaring _what_ you want to happen, rather than _how_ you want it to happen.
    - `return clean_windows(add_gas(create_car()))`
- [Imperative](https://en.wikipedia.org/wiki/Imperative_programming) (or procedural) programming declares both the _what_ and the _how_.
    - `car = create_car()`
    - `car.add_gas(10)`
    - `car.clean_windows()`

Python is _not_ the best language for functional programming. Reasons include:

1. No [static typing](https://developer.mozilla.org/en-US/docs/Glossary/Static_typing).
2. Everything is [mutable](https://en.wikipedia.org/wiki/Immutable_object).
3. No [tail call optimization](https://exploringjs.com/es6/ch_tail-calls.html).
4. [Side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)) are common.
5. Imperative and OOP styles abound in popular libraries.
6. [Purity](https://en.wikipedia.org/wiki/Pure_function) is not enforced (and sometimes not even encouraged).
7. [Sum Types](https://en.wikipedia.org/wiki/Algebraic_data_type) are hard to define.
8. [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) is weak at best.

- In FP, we strive to make data _[immutable](https://en.wikipedia.org/wiki/Immutable_object)_.
- Functional programming aims to be _declarative_. We prefer to declare _what_ we want the computer to do, rather than muck around with the details of _how_ to do it.
- The following code does _not_ execute line-by-line like an imperative language. Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.

```css
button {
    color: red;
}
```

- You'll encounter developers who love functional programming and others who love object-oriented programming. However, contrary to popular opinion, FP and OOP are _not_ always at odds with one another. They aren't opposites. Of the four pillars of OOP, [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) is the only one that doesn't fit with functional programming.

## First Class Functions

- **First-class function:** A function that is treated like any other value
- A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables
- Python supports first-class and higher-order functions
- First Order Example:

```py
def square(x):
    return (x) x (x)
# Assign function to a variable
f = square
print(f(5))
# 25
```

## [Higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function)

- **Higher-order function:** A function that accepts another function as an argument or returns a function.
- This allows us to avoid stateful iteration and mutation of variables
- Python supports first-class and higher-order functions
- Higher Order Example:

```py
def square(x):
    return (x) x (x)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```

- "Map", "filter", and "reduce" are three commonly used [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) in functional programming.

### Map

- In Python, the built-in [map](https://docs.python.org/3/library/functions.html#map) function takes a function and an [iterable](https://docs.python.org/3/glossary.html#term-iterable) (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.
- With `map`, we can operate on lists without using loops and nasty stateful variables. For example:

```py
def square(x):
    return (x) x (x)
nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

### Filter

- The built-in [filter](https://docs.python.org/3/library/functions.html#filter) function takes a function and an iterable (in this case a list) and returns a _new_ iterable that only contains elements from the original iterable where the result of the function on that item returned `True`

```py
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

### Reduce

- The built-in [functools.reduce()](https://docs.python.org/3/library/functools.html#functools.reduce) function takes a function and a list of values, and applies the function to each value in the list, _accumulating a single result_ as it goes.

## [Pure functions](https://en.wikipedia.org/wiki/Pure_function)

Pure functions have two properties:
- They _always_ return the same value given the same arguments.
- Running them causes no side effects
- Always try and use pure functions if possible - they have no randomness (deterministic)

### Reference vs. Value

- These types are passed by **reference** (mutable):
    - Lists
    - Dictionaries
    - Sets
    - Custom objects
- These types are passed by **value** (immutable):
    - Integers
    - Floats
    - Strings
    - Booleans
    - Tuples

- Basically only all iterable types (APART FORM TUPLES) are passed by reference (and therefore need to be copied to not modify the original values)

### i/o

The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". "Outside world" just means anything that's not stored in our application's memory (like variables).

#### Examples of i/o

- Reading from or writing to a file on the hard drive
- Accessing the internet
- Reading from or writing to a database
- Even simply _printing to the console_ is considered i/o!
- 
_All i/o is a form of "side effect"._

In functional programming, i/o is viewed as _dirty_ but _necessary_. We know we can't _eliminate_ i/o from our code, so we just _contain_ it as much as possible. There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure:
![io](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/45emq7q.png)

### [no-op](https://en.wikipedia.org/wiki/NOP_(code))

- An operation that does nothing
- If a function doesn't return anything, it's probably impure - if there is no return, the only reason for it to exist would be to cause a side effect.

### [Memoization](https://en.wikipedia.org/wiki/Memoization)

- At its core, [memoization](https://en.wikipedia.org/wiki/Memoization) is just [caching](https://en.wikipedia.org/wiki/Cache_(computing)) (storing a copy of) the result of a computation so that we don't have to compute it again in the future. **A trade off between memory and speed!**
- A call to `add(5, 7)` will _always_ evaluate to `12`. So, if you think about it, once we know that `add(5, 7)` can be replaced with `12`, we can just store the value `12` somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to `add(5, 7)` again, we can just look up the value `12` instead of doing a (potentially expensive) CPU operation.
- The slower and more complex the function, the more memoization can help speed things up.

- Pure functions are always [referentially transparent](https://www.baeldung.com/cs/referential-transparency#referential-transparency).
- "Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. **Referentially transparent functions can be safely memoized.** For example `add(2, 3)` can be smartly replaced by the value `5`.

## [Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))

- A function that calls itself
- Avoid infinite looping with a base case
- Programs will generally get to the base case and then work their way back up:
```py
def factorial_r(x):
    if x == 0 or x == 1:
        return 1 
    return (x) x factorial_r(x - 1)
```
- Particularly useful for dealing with tree data-structures

## Function Transformations

- "Function transformation" is just a more concise way to describe a specific type of [higher order function](https://en.wikipedia.org/wiki/Higher-order_function).
- It's when a function takes a function (or functions) as input and returns a _new_ function.

When to use function transformations:
- Creating variations of the same function dynamically can make it a lot easier to share common functionality.
- Most of the time function transformations are used to create a closure.

## [Closures](https://en.wikipedia.org/wiki/Closure_(computer_programming))

- *Objects* are *data* with *methods* attached, *closures* are *functions* with *data* attached.
- A closure is a function that references variables from outside its own function body. The function definition and its environment and bundled together into a single entity.
- Put simply, a closure is just a function that **keeps track of some values** from the place where it was _defined_, no matter where it is executed later on.
- [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) is a python keyword that is required to access variables from an enclosing score. Most languages don't require this but python does.
- The whole point of a closure is that it's _stateful_. It's a function that "remembers" the values from the enclosing scope even after the enclosing scope has finished executing.
- When not to use the `nonlocal` keyword: when the variable is mutable (such as a list, dictionary or set), and you are modifying its contents rather than reassigning the variable. You only need the `nonlocal` keyword if you are reassigning a variable instead of modifying its contents (which you must do to change immutable values such as strings and integers).

## [Currying](https://en.wikipedia.org/wiki/Currying)

- Function currying is a specific kind of function transformation where we translate a single function that accepts multiple arguments into multiple functions that each accept a single argument.
- Why Curry? It seems to just be more complicated.
    - Currying is often used to change a function's signature to make it conform to a specific shape.

## [Python decorators](https://book.pythontips.com/en/latest/decorators.html)

- [Python decorators](https://book.pythontips.com/en/latest/decorators.html) are just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) for [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function).
- These two pieces of code are _identical_:

```py
@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")
process_doc("Something wicked this way comes")
```

```py
def process(doc):
    print(f"Document: {doc}")
process_doc = vowel_counter(process)
process_doc("Something wicked this way comes")
```

### [`args` and `kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html)

- `args` collects positional arguments into a _tuple_
- `kwargs` collects keyword (named) arguments into a _dictionary_

- Any positional arguments _must come before_ keyword arguments.

## [Sum Types](https://en.wikipedia.org/wiki/Tagged_union)

- A "sum" type is the opposite of a "product" type. This Python object is an example of a _product_ type: (The total number of combinations a `man` can have is `4`, the _product_ of `2 x 2`)

```py
man.studies_finance = True
man.has_trust_fund = False
```

- We can _reduce_ the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible _types_:

```py
class Person:
    def __init__(self, name):
        self.name = name
class Dateable(Person):
    pass
class MaybeDateable(Person):
    pass
class Undateable(Person):
    pass
```

```py
def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid Person type")
```

- As opposed to product types, which can have many (often infinite) combinations, sum types have a _fixed_ number of possible values. To be clear: **Python doesn't really support sum types**. We have to use a workaround and invent our own little system and enforce it ourselves.

### [enums](https://docs.python.org/3/library/enum.html)

- Good for representing a fixed set of values (but not store additional data within them)

# Data Structures

## Dictionaries

Loop over key value pairs in a dictionary by using `dict.items()` which returns the key value pairs of the dictionary as tuples in a list:

```py
for key, value in dict.items():
    print(key)
    print(value)
```

# Virtual Environments

To create a virtual environment:
- Ensure the package manager is up to date:
    - `sudo apt-get update`
- Install the relevant package:
    - `sudo apt install python3.10-venv`
- Create the virtual environment:
    - `python3 -m venv venv`
    - - `python3`: This invokes the Python 3 interpreter. You are explicitly specifying that Python 3 should be used to execute the following module.
    - `-m venv`: The `-m` flag tells Python to run a module as a script. In this case, the `venv` module is responsible for creating a virtual environment. A virtual environment isolates project dependencies, ensuring that packages installed in one environment don't affect others.
    - `venv`: This is the **name** of the directory where the virtual environment will be created. You can use any name you like here, but it's common to name it `venv` to easily identify it.
- Activate the virtual environment
    - `source venv/bin/activate`
    - You should now see (venv) at beginning of your terminal prompt
