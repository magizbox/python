## List

```python
a = [1, 2, 3]
```

### Reverse a list

```python
[1, 3, 2][::-1]
# [2, 3, 1]
```

### Itertools

```python
import itertools

x = [1, 2, 3]
y = [2, 4, 5]

[a + b for (a, b) in itertools.product(x, y)]
# [3, 5, 6, 4, 6, 7, 5, 7, 8]
```

## Dictionary

```
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
```

**Update dictionary**

```
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
```

**Delete dictionary elements**

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
```

