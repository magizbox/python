> Testing your code is very important.

Getting used to writing testing code and running this code in parallel is now considered a good habit. Used wisely, this method helps you define more precisely your code’s intent and have a more decoupled architecture.

## Unittest

unittest is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.

### The Basics

Creating test cases is accomplished by subclassing unittest.TestCase.

```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

### Skipping tests

Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a .code `TestResult`.

Skipping a test is simply a matter of using the `skip() decorator` or one of its conditional variants.

```python
import sys
import unittest

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```

## Tox

tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.

Tox is a generic virtualenv management and test command line tool you can use for:

* checking your package installs correctly with **different Python versions** and interpreters
* running your tests in each of the environments, configuring your test tool of choice
* acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

**Installation**

You can install tox with pip using the following command

```
$ pip install tox
```

**Setup default environment in Windows with conda**

```
$ conda create -p C:\python27 python=2.7 
$ conda create -p C:\python34 python=3.4
```

## Related Readings

* Testing Your Code, [The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/)
* unittest — Unit testing framework, [docs.python.org](https://docs.python.org/2.7/library/unittest.html#organizing-test-code)
* Is it possible to use tox with conda-based Python installations?, [stackoverflow](http://stackoverflow.com/questions/30555943/is-it-possible-to-use-tox-with-conda-based-python-installations)