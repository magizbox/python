## Datetime

Print current time

```python
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# '2015-12-29 14:02:27'
```


Get current time

```python
import datetime
datetime.datetime.now()
# datetime(2009, 1, 6, 15, 8, 24, 78915)
```


Unixtime

```python
import time
int(time.time())
```

Measure time elapsed

```python
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)
```

### Moment

Dealing with dates in Python shouldn't have to suck.

**Installation**

```
pip install moment
```

**Usage**

```python
import moment
from datetime import datetime

# Create a moment from a string
moment.date("12-18-2012")

# Create a moment with a specified strftime format
moment.date("12-18-2012", "%m-%d-%Y")

# Moment uses the awesome dateparser library behind the scenes
moment.date("2012-12-18")

# Create a moment with words in it
moment.date("December 18, 2012")

# Create a moment that would normally be pretty hard to do
moment.date("2 weeks ago")

# Create a future moment that would otherwise be really difficult
moment.date("2 weeks from now")

# Create a moment from the current datetime
moment.now()

# The moment can also be UTC-based
moment.utcnow()

# Create a moment with the UTC time zone
moment.utc("2012-12-18")

# Create a moment from a Unix timestamp
moment.unix(1355875153626)

# Create a moment from a Unix UTC timestamp
moment.unix(1355875153626, utc=True)

# Return a datetime instance
moment.date(2012, 12, 18).date

# We can do the same thing with the UTC method
moment.utc(2012, 12, 18).date

# Create and format a moment using Moment.js semantics
moment.now().format("YYYY-M-D")

# Create and format a moment with strftime semantics
moment.date(2012, 12, 18).strftime("%Y-%m-%d")

# Update your moment's time zone
moment.date(datetime(2012, 12, 18)).locale("US/Central").date

# Alter the moment's UTC time zone to a different time zone
moment.utcnow().timezone("US/Eastern").date

# Set and update your moment's time zone. For instance, I'm on the
# west coast, but want NYC's current time.
moment.now().locale("US/Pacific").timezone("US/Eastern")

# In order to manipulate time zones, a locale must always be set or
# you must be using UTC.
moment.utcnow().timezone("US/Eastern").date

# You can also clone a moment, so the original stays unaltered
now = moment.utcnow().timezone("US/Pacific")
future = now.clone().add(weeks=2)
```


### Related Readings

* How to get current time in Python, [stackoverflow](http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python)
* Does Python's time.time() return the local or UTC timestamp?, [stackoverflow](http://stackoverflow.com/a/16299439)
* Measure time elapsed in Python?, [stackoverflow](http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python)
* momnet, [https://github.com/zachwill/moment](https://github.com/zachwill/moment)
