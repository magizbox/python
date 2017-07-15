The most basic data structure in Python is the **sequence**. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

## List

The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

**Create a list**

```python
a = [1, 2, 3]
# [1, 2, 3]
```

**Access values in lists**

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print list1[0]   # physics

print list2[1:5] # [2, 3, 4, 5]
```

**Updated lists**

```python
list = ['physics', 'chemistry', 1997, 2000]
print list[2] # 1997

list[2] = 2001
print list[2] # 2001
```

**Delete list elements**

```python
list1 = ['physics', 'chemistry', 1997, 2000];

print list1
# ['physics', 'chemistry', 1997, 2000]

del list1[2]

print list1
# ['physics', 'chemistry', 2000]
```

**Reverse a list**

```python
[1, 3, 2][::-1]
# [2, 3, 1]
```

**Itertools**

```python
import itertools

x = [1, 2, 3]
y = [2, 4, 5]

[a + b for (a, b) in itertools.product(x, y)]
# [3, 5, 6, 4, 6, 7, 5, 7, 8]
```

**Select random elements in list**

```python
import random

x = [13, 23, 14, 52, 6, 23]

random.choice(x) # 52

random.sample(x, 3) # [23, 14, 52]
```

## Dictionary

Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

**Create a dictionary**

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
```

**Update dictionary**

```python
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

## Related Readings

* Python Lists, [tutorialspoint.com](https://www.tutorialspoint.com/python/python_lists.htm)
* Python Dictionary, [tutorialspoint.com](https://www.tutorialspoint.com/python/python_dictionary.htm)
* Python Dictionary Methods, [guru99](https://www.guru99.com/python-dictionary-beginners-tutorial.html)
