## Print, print

```python
print "Hello World"
```

## Conditional

```python
if you_smart:
    print "learn python"
else:
    print "go away"
```

## Loop

```python
for i in range(10):
    print "hello again"
```

## Functions

### Variable-length arguments

[^1]

```python
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
```

Example

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

## Coding Convention

### Code layout

Indentation: 4 spaces

[^1]: [tutorialpoints, Python Functions](http://www.tutorialspoint.com/python/python_functions.htm)