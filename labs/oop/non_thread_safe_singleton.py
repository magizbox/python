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


@Singleton
class Foo:
    def __init__(self):
        print 'Foo created'


@Singleton
class Bar:
    def __init__(self):
        print 'Bar created'


if __name__ == '__main__':
    try:
        f = Foo()  # Error, this isn't how you get the instance of a singleton
    except Exception, e:
        print e

    f1 = Foo.Instance()  # Good. Being explicit is in line with the Python Zen
    f2 = Foo.Instance()  # Returns already created instance

    b1 = Bar.Instance()
    b2 = Bar.Instance()

    print "Is f1 equal f2: ", f1 is f2  # True
    print "Is b1 equal b2: ", b1 is b2  # True
    print "Is foo equal bar: ", f1 is b1  # False
