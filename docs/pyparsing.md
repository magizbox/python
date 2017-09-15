# Pyparsing

```
from pyparsing import Word, alphas

greet = Word(alphas) + "," + Word(alphas) + "!"
greeting = greet.parseString("Hello World")
print greeting
```

| Character Classes |               | Code                   | Match       | Doesn't Match | Code                   |
|-------------------|---------------|------------------------|-------------|---------------|------------------------|
|  alphas           | A-Za-z        |                        |             |               | https://repl.it/LIFJ/2 |
| nums              | 0-9           |                        |             |               |                        |
| alphanums         | alphas + nums |                        |             |               |                        |
| empty             | Literal("")   |                        |             |               |                        |
| Literal           |               | Literal("Hello World") | Hello World |               |                        |

## Operator

* And (operator +): must match all (ignoring whitespace)

```
assignment = varName + Literal("=") + arithExperssion
assignment = varName + "=" + arithExperssion
```

* Or (operator ^): match longest

* MatchFirst (operator |) 

* Each (opeartor &): like And, must match all, but in any order

## Repetition and Collection

* OneOrMore, ZeroOrMOre
* Group
* Combine
* Optional

```
Literal("name") + LIteral("(") + Literral("x") + Literral(")")
```

matches: `"name(x)"`, `name (x)"`, `name( x )", "name( x )"
```

* oneOf: string of space-separated literl strings

## Advaned Pyparsing

Forward: to define recursive grammer

Regex: define regular expression to match

**Forward**


# References

* http://www.ptmcg.com/geo/python/howtousepyparsing.html#steps-to-follow
* Introduction to Pyparsing: An Object-oriented Easy-to-Use Toolkit for Building Recursive Descent Parsers, http://www.ptmcg.com/geo/python/confs/TxUnconf2008Pyparsing.html
