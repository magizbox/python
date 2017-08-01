# Metaclasses


## Python, Classes, and Objects

Most readers are aware that Python is an object-oriented language.  By
object-oriented, we mean that Python can define *classes*, which bundle
**data** and **functionality** into one entity.  For example, we may
create a class ``IntContainer`` which stores an integer and allows
certain operations to be performed:


```python
class IntContainer(object):
    def __init__(self, i):
        self.i = int(i)

    def add_one(self):
        self.i += 1
```


```python
ic = IntContainer(2)
ic.add_one()
print(ic.i)
```

    3
    

This is a bit of a silly example, but shows the fundamental nature of
classes: their ability to bundle data and operations into a single
*object*, which leads to cleaner, more manageable, and more adaptable code.
Additionally, classes can inherit properties from parents and add or
specialize attributes and methods.  This *object-oriented*
approach to programming can be very intuitive and powerful.

What many do not realize, though, is that quite literally
[*everything*](http://www.diveintopython.net/getting_to_know_python/everything_is_an_object.html)
in the Python language is an object.

<!-- PELICAN_END_SUMMARY -->

For example, integers are simply instances of
the built-in ``int`` type:


```python
print type(1)
```

    <type 'int'>
    

To emphasize that the ``int`` type really is an object, let's derive from it
and specialize the ``__add__`` method (which is the machinery underneath
the ``+`` operator):

*(Note: We'll used the* ``super`` *syntax to call methods from the parent class: if you're unfamiliar with this, take a look at*
[*this StackOverflow question*](http://stackoverflow.com/questions/576169/understanding-python-super-and-init-methods)*).*


```python
class MyInt(int):
    def __add__(self, other):
        print "specializing addition"
        return super(MyInt, self).__add__(other)

i = MyInt(2)
print(i + 2)
```

    specializing addition
    4
    


Using the ``+`` operator on our derived type goes through our ``__add__``
method, as expected.
We see that ``int`` really is an object that can be subclassed and extended
just like user-defined classes.  The same is true
of ``float``s, ``list``s, ``tuple``s, and everything else in the Python
language.  They're all objects.

## Down the Rabbit Hole: Classes as Objects

We said above that *everything* in python is an object: it turns out that this
is true of *classes themselves*.  Let's look at an example.

We'll start by defining a class that does nothing


```python
class DoNothing(object):
    pass
```

If we instantiate this, we can use the ``type`` operator to see the type
of object that it is:


```python
d = DoNothing()
type(d)
```




    __main__.DoNothing



We see that our variable ``d`` is an instance of the class
``__main__.DoNothing``.

We can do this similarly for built-in  types:


```python
L = [1, 2, 3]
type(L)
```




    list



A list is, as you may expect, an object of type ``list``.

But let's take this a step further: what is the type
of ``DoNothing`` itself?


```python
type(DoNothing)
```




    type



The type of ``DoNothing`` is ``type``.  This tells us that the *class*
``DoNothing`` is itself an object, and that object is of type ``type``.

It turns out that this is the same for built-in datatypes:


```python
type(tuple), type(list), type(int), type(float)
```




    (type, type, type, type)



What this shows is that in Python, *classes are objects*, and they are objects of
type ``type``.  ``type`` is a *metaclass*: a class which instantiates classes.
All [new-style classes](http://www.python.org/doc/newstyle/)
in Python are instances of the ``type`` metaclass, including ``type`` itself:


```python
type(type)
```




    type



Yes, you read that correctly:
the type of ``type`` is ``type``.  In other words, ``type`` is *an
instance of itself*.  This sort of circularity cannot (to my knowledge)
be duplicated in pure Python, and the behavior is created through a bit of a
hack at the implementation level of Python.

## Metaprogramming: Creating Classes on the Fly

Now that we've stepped back and considered the fact that classes in Python
are simply objects like everything else, we can think about what is known
as *metaprogramming*.  You're probably used to creating functions which
return objects.  We can think of these functions as an object factory: they
take some arguments, create an object, and return it.  Here is a simple example
of a function which creates an ``int`` object:


```python
def int_factory(s):
    i = int(s)
    return i

i = int_factory('100')
print(i)
```

    100
    

This is overly-simplistic, but any function you write in the course
of a normal program can be boiled down to this: take some arguments,
do some operations, and create & return an object.
With the above discussion in mind, though, there's nothing to stop
us from creating an object of type ``type`` (that is, a class), 
and returning that instead -- this is a *metafunction:*


```python
def class_factory():
    class Foo(object):
        pass
    return Foo

F = class_factory()
f = F()
print(type(f))
```

    <class '__main__.Foo'>
    

Just as the function ``int_factory`` constructs an returns an instance of
``int``,
the function ``class_factory`` constructs and returns an instance of ``type``:
that is, a class.

But the above construction is a bit awkward: especially if we were going to do some
more complicated logic when constructing ``Foo``, it would be nice to avoid all the
nested indentations and define the class in a more dynamic way.
We can accomplish this by instantiating ``Foo`` from ``type`` directly:


```python
def class_factory():
    return type('Foo', (), {})

F = class_factory()
f = F()
print(type(f))
```

    <class '__main__.Foo'>
    

In fact, the construct


```python
class MyClass(object):
    pass
```

is identical to the construct


```python
MyClass = type('MyClass', (), {})
```

``MyClass`` is an instance of type ``type``, and that can be seen
explicitly in the second version of the definition.
A potential confusion arises from the more common use of ``type`` as
a function to determine the type of an object, but you should strive
to separate these two uses of the keyword in your mind:
here ``type`` is a class (more precisely, a *metaclass*),
and ``MyClass`` is an instance of ``type``.

The arguments to the ``type`` constructor are:
type(name, bases, dct)
- ``name`` is a string giving the name of the class to be constructed
- ``bases`` is a tuple giving the parent classes of the class to be constructed
- ``dct`` is a dictionary of the attributes and methods of the class to be constructed

So, for example, the following two pieces of code have identical results:


```python
class Foo(object):
    i = 4

class Bar(Foo):
    def get_i(self):
        return self.i
    
b = Bar()
print(b.get_i())
```

    4
    


```python
Foo = type('Foo', (), dict(i=4))

Bar = type('Bar', (Foo,), dict(get_i = lambda self: self.i))

b = Bar()
print(b.get_i())
```

    4
    

This perhaps seems a bit over-complicated in the case of this contrived
example, but it can be very powerful as a means of dynamically creating
new classes on-the-fly.

## Making Things Interesting: Custom Metaclasses

Now things get really fun.  Just as we can inherit from and extend a class we've
created, we can also inherit from and extend the ``type`` metaclass, and create
custom behavior in our metaclass.

### Example 1: Modifying Attributes

Let's use a simple example where we want to create an API in which the user can
create a set of interfaces which contain a file object.  Each interface should
have a unique string ID, and contain an open file object.  The user could then write
specialized methods to accomplish certain tasks.  There are certainly good
ways to do this without delving into metaclasses, but such a simple example will
(hopefully) elucidate what's going on.

First we'll create our interface meta class, deriving from ``type``:


```python
class InterfaceMeta(type):
    def __new__(cls, name, parents, dct):
        # create a class_id if it's not specified
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()
        
        # open the specified file for writing
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')
        
        # we need to call type.__new__ to complete the initialization
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)
```

Notice that we've modified the input dictionary (the attributes and
methods of the class) to add a class id if it's not present, and to
replace the filename with a file object pointing to that file name.

Now we'll use our ``InterfaceMeta`` class to construct and instantiate
an Interface object:


```python
Interface = InterfaceMeta('Interface', (), dict(file='tmp.txt'))

print(Interface.class_id)
print(Interface.file)
```

    interface
    <open file 'tmp.txt', mode 'w' at 0x21b8810>
    

This behaves as we'd expect: the ``class_id`` class variable is created,
and the ``file`` class variable is replaced with an open file object.
Still, the creation of the ``Interface`` class
using ``InterfaceMeta`` directly is a bit clunky and difficult to read.
This is where ``__metaclass__`` comes in
and steals the show.  We can accomplish the same thing by
defining ``Interface`` this way:


```python
class Interface(object):
    __metaclass__ = InterfaceMeta
    file = 'tmp.txt'
    
print(Interface.class_id)
print(Interface.file)
```

    interface
    <open file 'tmp.txt', mode 'w' at 0x21b8ae0>
    

by defining the ``__metaclass__`` attribute of the class, we've told the
class that it should be constructed using ``InterfaceMeta`` rather than
using ``type``.  To make this more definite, observe that the type of
``Interface`` is now ``InterfaceMeta``:


```python
type(Interface)
```




    __main__.InterfaceMeta



Furthermore, any class derived from ``Interface`` will now be constructed
using the same metaclass:


```python
class UserInterface(Interface):
    file = 'foo.txt'
    
print(UserInterface.file)
print(UserInterface.class_id)
```

    <open file 'foo.txt', mode 'w' at 0x21b8c00>
    userinterface
    

This simple example shows how metaclasses can be used to create powerful and
flexible APIs for projects.  For example, the
[Django project](https://www.djangoproject.com/)
makes use of these sorts of constructions to allow concise declarations
of very powerful extensions to their basic classes.

### Example 2: Registering Subclasses

Another possible use of a metaclass is to automatically register all
subclasses derived from a given base class.  For example, you may have
a basic interface to a database and wish for the user to be able to
define their own interfaces, which are automatically stored in a master registry.

You might proceed this way:


```python
class DBInterfaceMeta(type):
    # we use __init__ rather than __new__ here because we want
    # to modify attributes of the class *after* they have been
    # created
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name.lower()
            cls.registry[interface_id] = cls
            
        super(DBInterfaceMeta, cls).__init__(name, bases, dct)
```

Our metaclass simply adds a ``registry`` dictionary if it's not already
present, and adds the new class to the registry if the registry is already
there.  Let's see how this works:


```python
class DBInterface(object):
    __metaclass__ = DBInterfaceMeta
    
print(DBInterface.registry)
```

    {}
    

Now let's create some subclasses, and double-check that they're added to
the registry:


```python
class FirstInterface(DBInterface):
    pass

class SecondInterface(DBInterface):
    pass

class SecondInterfaceModified(SecondInterface):
    pass

print(DBInterface.registry)
```

    {'firstinterface': <class '__main__.FirstInterface'>, 'secondinterface': <class '__main__.SecondInterface'>, 'secondinterfacemodified': <class '__main__.SecondInterfaceModified'>}
    

It works as expected!  This could be used in conjunction with
a function that chooses implementations from the registry,
and any user-defined ``Interface``-derived objects would be
automatically accounted for, without the user having to remember
to manually register the new types.

## Conclusion: When Should You Use Metaclasses?

I've gone through some examples of what metaclasses are, and some ideas 
about how they might be used to create very powerful and flexible APIs. 
Although metaclasses are in the background of everything you do in Python,
the average coder rarely has to think about them.

But the question remains: when should you think about using custom
metaclasses in your project?  It's a complicated question, but
there's a quotation floating around the web
that addresses it quite succinctly:

> Metaclasses are deeper magic than 99% of users should ever worry about.
> If you wonder whether you need them, you don’t (the people who actually
> need them know with certainty that they need them, and don’t need an
> explanation about why).
>
> – Tim Peters

In a way, this is a very unsatisfying answer: it's a bit reminiscent of
the wistful and cliched explanation of the border between attraction
and love: "well, you just... know!"

But I think Tim is right: in general,
I've found that most tasks in Python that can be accomplished through
use of custom metaclasses can also be accomplished more cleanly and with
more clarity by other means.  As programmers, we should always be careful
to avoid being clever for the sake of cleverness alone, though
it is admittedly an ever-present temptation.

I personally spent six years doing science with Python, writing code
nearly on a daily basis, before I found a problem for which metaclasses
were the natural solution.  And it turns out Tim was right:

I just knew.
