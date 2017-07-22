# Collection

In this post I will cover 4 most popular data types in python `list`, `tuple`, `set`, `dictionary`

## List

The most basic data structure in Python is the **sequence**. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

**Usage**

* A list keeps *order*, dict and set don't: when you care about order, therefore, you must use list (if your choice of containers is limited to these three, of course)

**Most Popular Operations**

<table class="highlight-table">

<tr>
<td><a href="#create-a-list">Create a list</a></td>
<td class="example">
<f> a = ["a", "b", 3] </f>
</td>
</tr>

<tr>
<td><a href="#access-values-in-list">Access values in list</a></td>
<td class="example">
<f> a[1] </f>
</td>
</tr>

<tr>
<td><a href="#updated-list">Updated List</a></td>
<td class="example">
<f> a[0] = 5 </f>
</td>
</tr>

<tr>
<td><a href="#delete-list-elements">Delete list elements</a></td>
<td class="example">
<f> del a[1] </f>
</td>

<tr>
<td><a href="#delete-list-elements">Reverse a list</a></td>
<td class="example">
<f> a[::-1] </f>
</td>

<tr>
<td><a href="#itertools">Itertools</a></td>
<td class="example">
<f> [a + b for (a, b) in itertools.product(x, y)] </f>
</td>

<tr>
<td><a href="#select-random-elements-in-list">Select random elements in list</a></td>
<td class="example">
<f> random.choice(x) </f>
<f> random.sample(x, 3) </f>
</td>

</tr>

</table>

#### Create a list

```python
a = [1, 2, 3]
# [1, 2, 3]
```

#### Access values in list

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print list1[0]   # physics

print list2[1:5] # [2, 3, 4, 5]
```

#### Updated lists

```python
list = ['physics', 'chemistry', 1997, 2000]
print list[2] # 1997

list[2] = 2001
print list[2] # 2001
```

#### Delete list elements

```python
list1 = ['physics', 'chemistry', 1997, 2000];

print list1
# ['physics', 'chemistry', 1997, 2000]

del list1[2]

print list1
# ['physics', 'chemistry', 2000]
```

#### Reverse a list

```python
[1, 3, 2][::-1]
# [2, 3, 1]
```

#### Itertools

```python
import itertools

x = [1, 2, 3]
y = [2, 4, 5]

[a + b for (a, b) in itertools.product(x, y)]
# [3, 5, 6, 4, 6, 7, 5, 7, 8]
```

#### Select random elements in list

```python
import random

x = [13, 23, 14, 52, 6, 23]

random.choice(x) # 52

random.sample(x, 3) # [23, 14, 52]
```

## Tuples

A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

**Usage**

* Tuples have structure, lists have order
* Tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences


**Most Popular Operations**

<table class="highlight-table">

<tr>
<td><a href="#create-a-tuple">Create a tuple</a></td>
<td class="example">
<f> t = ("a", 1, 2) </f>
</td>
</tr>

<tr>
<td><a href="#accessing-values-in-tuples">Accessing Values in Tuples</a></td>
<td class="example">
<f> t[0], t[1:] </f>
</td>
</tr>

<tr>
<td><a href="#updating-tuples">Updating Tuples</a></td>
<td class="example">
<f> Not allowed </f>
</td>
</tr>
</table>

#### Create a tuple

```python
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup4 = ()
tup5 = (50, )
```

#### Accessing Values in Tuples

```python
#!/usr/bin/python

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

tup1[0]
# physics

tup2[1:5]
[2, 3, 4, 5]
```

#### Updating Tuples

Tuples are immutable which means you cannot update or change the values of tuple elements. You are able to take portions of existing tuples to create new tuples as the following example demonstrates

```python
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3
```

## Dictionary

Each **key** is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

**Usage**

* dict associates with each *key a value*, while list and set just contain values: very different use cases, obviously.

**Most Popular Operations**

<table class="highlight-table">

<tr>
<td><a href="#create-a-dictionary">Create a dictionary</a></td>
<td class="example">
<f> d = {"a": 1, "b": 2, "c": 3} </f>
</td>
</tr>

<td><a href="#update-dictionary">Update dictionary</a></td>
<td class="example">
<f> d["a"] = 4 </f>
</td>
</tr>

<td><a href="#delete-dictionary-elements">Delete dictionary elements</a></td>
<td class="example">
<f> del d["a"] </f>
</td>
</tr>
</table>

#### Create a dictionary 

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
```

#### Update dictionary

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
```

#### Delete dictionary elements

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
* In Python, when to use a Dictionary, List or Set?, [stackoverflow](https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set)
* What's the difference between lists and tuples?, [stackoverflow](https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples)