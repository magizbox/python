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

### Related Readings

* How to get current time in Python, [stackoverflow](http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python)
* Does Python's time.time() return the local or UTC timestamp?, [stackoverflow](http://stackoverflow.com/a/16299439)
* Measure time elapsed in Python?, [stackoverflow](http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python)
