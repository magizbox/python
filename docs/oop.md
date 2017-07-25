# Object Oriented Programming

Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. This chapter helps you become an expert in using Python's object-oriented programming support.

If you do not have any previous experience with object-oriented (OO) programming, you may want to consult an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts.

## Classes and Objects

Classes can be thought of as blueprints for creating objects. When I define a `BankAccount` class using the class keyword, I haven't actually created a bank account. Instead, what I've created is a sort of instruction manual for constructing "bank account" objects. Let's look at the following example code:

```python
class BankAccount:
	id = None
	balance = 0

	def __init__(self, id, balance=0):
		self.id = id
		self.balance = balance

	def __get_balance(self):
		return self.balance
		
	def withdraw(self, amount):
		self.balance = self.balance - amount

	def deposit(self, amount):
		self.balance = self.balance + amount
     
john = BankAccount(1, 1000.0)
john.withdraw(100.0)
```

The `class BankAccount` line *does not* create a new bank account. That is, just because we've *defined* a `BankAcount` doesn't mean we've *created* on; we've merely outlined the *blueprint* to create a `BankAccount` object. To do so, we call the class's `__init__` method with the proper number of arguments (minus `self`, which we'll get to in a moment)

So, to use the "blueprint" that we crated by defining the `class BankAccount` (which is used to create `BankAccount` objects), we call the class name almost as if it were a function: `john = BankAccount(1, 1000.0)`. This line simple say "use the `BankAccount` blueprint to create me a new object, which I'll refer to as `john`".

The `john` *object*, known as an `instance`, is the realized version of the `BankAccount` *class*. Before we called `BankAccount()`, no `BankAccount` object existed. We can, of course, create as many `BankAccount` objects as we'd like. There is still, however, only one `BankAccount` *class*, regardless of how many *instances* of the class we create.

### `self`

So what's with that `self` parameter to all of the `BankAccount` methods? What is it? Why, it's the instance, of course! Put another way, a method like withdraw defines the instructions for withdrawing money from some abstract customer's account. Calling `john.withdraw(100)` puts those instructions to use on the `john` instance.

So when we say def `withdraw(self, amount)`:, we're saying, "here's how you withdraw money from a `BankAccount` object (which we'll call `self`) and a dollar figure (which we'll call `amount`). `self` is the *instance* of the `BankAccount` that `withdraw` is being called on. That's not me making analogies, either. `john.withdraw(100.0)` is just shorthand for `BankAccount.withdraw(john, 100.0)`, which is perfectly valid (if not often seen) code.

### Constructors: `__init__`

`self` may make sense for other methods, but what about `__init__`? When we call `__init__`, we're in the process of creating an object, so how can there already be a `self`? Python allows us to extend the `self` pattern to when objects are constructed as well, even though it doesn't *exactly* fit. Just imagine that `john = (1, 1000.0)` is the same as calling `john = BankAccount(john, 1, 1000.0)`; the `john` that's passed in is also made the result.

This is why when we call `__init__`, we initialize objects by saying things like `self.id = id`. Remember, since `self` is the instance, this is equivalent to saying `john.id = id`, which is the same as `john.id= 1`. Similarly, `self.balance = balance` is the same as `john.balance = 1000.0`. After these two lines, we consider the `BankAccount` object "initialized" and ready for use.

### Be careful what you `__init__`

After `__init__` has finished, the caller can rightly assume that the object is ready to use. That is, after `john = BankAccount(1, 1000.0)`, we can start making `deposit` and `withdraw` calls on `john`; `john` is a **fully-initialized** object.

## Inheritance

While Object-oriented Programming is useful as a modeling tool, it truly gains power when the concept of *inheritance* is introduced. *Inheritance* is the process by which a "child" class *derives* the data and behavior of a "parent" class. An example will definitely help us here.

Imagine we run a car dealership. We sell all types of vehicles, from motorcycles to trucks. We set ourselves apart from the competition by our prices. Specifically, how we determine the price of a vehicle on our lot: $5,000 x number of wheels a vehicle has. We love buying back our vehicles as well. We offer a flat rate - 10% of the miles driven on the vehicle. For trucks, that rate is $10,000. For cars, $8,000. For motorcycles, $4,000.

If we wanted to create a sales system for our dealership using Object-oriented techniques, how would we do so? What would the objects be? We might have a `Sale` class, a `Customer` class, an `Inventory` class, and so forth, but we'd almost certainly have a `Car`, `Truck`, and `Motorcycle` class.

What would these classes look like? Using what we've learned, here's a possible implementation of the `Car` class:

```python
class Car(object):
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 8000 - (.10 * self.miles)
```

OK, that looks pretty reasonable. Of course, we would likely have a number of other methods on the class, but I've shown two of particular interest to us: `sale_price` and `purchase_price`. We'll see why these are important in a bit.

Now that we've got the `Car` class, perhaps we should create a `Truck` class? Let's follow the same pattern we did for car:

```python
class Truck(object):
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 10000 - (.10 * self.miles)
```

Wow. That's *almost* identical to the car class. One of the most important rules of programming (in general, not just when dealing with objects) is "DRY" or "**D**on't **R**epeat **Y**ourself. We've definitely repeated ourselves here. In fact, the `Car` and `Truck` classes differ only by a single character (aside from comments).

So what gives? Where did we go wrong? Our main problem is that we raced straight to the concrete: `Car` and `Truck` are real things, tangible objects that make intuitive sense as classes. However, they share so much data and functionality in common that it seems there must be an *abstraction* we can introduce here. Indeed there is: the notion of `Vehicle`.

### Abstract Classes

A `Vehicle` is not a real-world object. Rather, it is a *concept* that some real-world objects (like cars, trucks, and motorcycles) embody. We would like to use the fact that each of these objects can be considered a vehicle to remove repeated code. We can do that by creating a `Vehicle` class:

```python
class Vehicle(object):
    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on


    def sale_price(self):
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)
```

Now we can make the `Car` and `Truck` class *inherit* from the `Vehicle` class by replacing `object` in the line class `Car(object)`. The class in parenthesis is the class that is inherited from (`object` essentially means "no inheritance". We'll discuss exactly why we write that in a bit).

We can now define `Car` and `Truck` in a very straightforward way:

```python
class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000
```

# Object

Convert dict to object

```python
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
```

Then, you can use

```
> args = {'a': 1, 'b': 2}
> s = Struct(**args)
> s
< __main__.Struct instance at 0x01D6A738 >
> s.a
1
> s.b
2
```


## Suggested Readings

* [Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
* [stackoverflow, Convert Python dict to object?](http://stackoverflow.com/questions/1305532/convert-python-dict-to-object)
* [Why are Python's 'private' methods not actually private?](http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private)
