> Testing your code is very important.

Getting used to writing testing code and running this code in parallel is now considered a good habit. Used wisely, this method helps you define more precisely your code’s intent and have a more decoupled architecture.

## The Basics

**Unittest**

unittest is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.

Creating test cases is accomplished by subclassing unittest.TestCase.

```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

## Skipping tests

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


## Related Readings

* Testing Your Code, [The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/)
* unittest — Unit testing framework, [docs.python.org](https://docs.python.org/2.7/library/unittest.html#organizing-test-code)