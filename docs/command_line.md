# Command Line Arguments 

There are the following modules in the standard library:

* The getopt module is similar to GNU getopt.
* The optparse module offers object-oriented command line option parsing.

Here is an example that uses the latter from the docs:

```python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
```

optparse supports (among other things):

* Multiple options in any order.
* Short and long options.
* Default values.
* Generation of a usage help message.

# Suggest Reading

* [Command Line Arguments In Python](https://stackoverflow.com/a/1009864/772391)