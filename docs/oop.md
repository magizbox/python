# Object Oriented Programming

[^1]

```
class BankAccount:
  id = None
  balance = 0

  def __init__(self, id, balance=0):
    self.id = id
    self.balance = balance

  def __get_balance():
     pass
  def withdraw():
     pass
   def deposite():
     pass
```

[^1]: [Why are Python's 'private' methods not actually private?](http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private)

# Object

Convert dict to object [^1]

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

# Singleton

### Non-thread-safe

Paul Manta's implementation of singletons [^2]

```python
@Singleton
class Foo:
   def __init__(self):
       print 'Foo created'

f = Foo() # Error, this isn't how you get the instance of a singleton

f = Foo.Instance() # Good. Being explicit is in line with the Python Zen
g = Foo.Instance() # Returns already created instance

print f is g # True

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
```

### Thread safe

werediver's implementation of singletons. A thread safe implementation of singleton pattern in Python. Based on tornado.ioloop.IOLoop.instance() approach.

```python
import threading

# Based on tornado.ioloop.IOLoop.instance() approach.
# See https://github.com/facebook/tornado
class SingletonMixin(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

class A(SingletonMixin):
    pass

class B(SingletonMixin):
    pass

if __name__ == '__main__':
    a, a2 = A.instance(), A.instance()
    b, b2 = B.instance(), B.instance()

    assert a is a2
    assert b is b2
    assert a is not b

    print('a:  %s\na2: %s' % (a, a2))
    print('b:  %s\nb2: %s' % (b, b2))
```

[^1]: [stackoverflow, Convert Python dict to object?](http://stackoverflow.com/questions/1305532/convert-python-dict-to-object)
[^2]: [Is there a simple, elegant way to define singletons?](http://stackoverflow.com/a/7346105/772391)