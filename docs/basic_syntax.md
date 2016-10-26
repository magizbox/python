## Print, print

```python
print "Hello World"
```

## Conditional

```
if you_smart:
    print "learn python"
else:
    print "go away"
```

## Loop

In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times.

Programming languages provide various control structures that allow for more complicated execution paths. A loop statement allows us to execute a statement or group of statements multiple times. The following diagram illustrates a loop statement

<div class="text-center">
<img src="https://www.tutorialspoint.com/python/images/loop_architecture.jpg"></img>
</div>

Python programming language provides following types of loops to handle looping requirements.

<table>
<tbody>
<tr>
<td class="col-xs-2"><strong>while loop</strong></td>
<td>Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.</td>
</tr>
<tr>
<td><strong>for loop</strong></td>
<td>Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.</td>
</tr>
<tr>
<td><strong>nested loops</strong></td>
<td>You can use one or more loop inside any another while, for or do..while loop.</td>
</tr>
</tbody>
</table>

### While Loop

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.

**Syntax**

The syntax of a while loop in Python programming language is

```
while expression:
   statement(s)
```

**Example**

```python
count = 0
while count < 9:
   print 'The count is:', count
   count += 1

print "Good bye!"
```

### For Loop

It has the ability to iterate over the items of any sequence, such as a list or a string.

**Syntax**

```
for iterating_var in sequence:
   statements(s)
```

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var. Next, the statements block is executed. Each item in the list is assigned to iterating_var, and the statement(s) block is executed until the entire sequence is exhausted.

**Example**

```python
for i in range(10):
    print "hello", i

for letter in 'Python':
   print 'Current letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
   print 'Current fruit :', fruit

print "Good bye!"
```

### Yield and Generator

Yield is a keyword that is used like return, except the function will return a generator.

```
def createGenerator():
    yield 1
    yield 2
    yield 3

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)
# 1
# 2
# 3
```

Visit [Yield and Generator explained](basic_syntax_yield.md) for more information

**Related Readings**

* ["Python Loops". www.tutorialspoint.com](https://www.tutorialspoint.com/python/python_loops.htm)
* ["What does the “yield” keyword do?". stackoverflow.com](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
* ["Improve Your Python: 'yield' and Generators Explained". jeffknupp.com](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

## Functions

### Variable-length arguments

```
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
```

**Example**

```python
#!/usr/bin/python

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

```
**Related Readings**

* ["Python Functions". www.tutorialspoint.com](http://www.tutorialspoint.com/python/python_functions.htm)

## Coding Convention

### Code layout

Indentation: 4 spaces

