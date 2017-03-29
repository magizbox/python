## Convert dict to object

Elegant way to convert a normal Python dict with some nested dicts to an object

```python
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
```

Then, you can use

```python
> args = {'a': 1, 'b': 2}
> s = Struct(**args)
> s
< __main__.Struct instance at 0x01D6A738 >
> s.a
1
> s.b
2
```

**Related Readings**

* [stackoverflow, Convert Python dict to object?](http://stackoverflow.com/questions/1305532/convert-python-dict-to-object)