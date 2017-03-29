## Format

```python
'{0}, {1}, {2}'.format('a', 'b', 'c')
# 'a, b, c'
```

## Regular Expressions

The aim of this chapter of our Python tutorial is to present a detailed led and descriptive introduction into regular expressions. This introduction will explain the theoretical aspects of regular expressions and will show you how to use them in Python scripts. 

Regular Expressions are used in programming languages to filter texts or textstrings. It's possible to check, if a text or a string matches a regular expression. 

There is an aspect of regular expressions which shouldn't go unmentioned: The syntax of regular expressions is the same for all programming and script languages, e.g. Python, Perl, Java, SED, AWK and even X#.

**A Simple Regular Expression**

We already said in the previous section that we can see the variable "sub" as a very simple regular expression. 
If you want to use regular expressions in Python, you have to import the re module, which provides methods and functions to deal with regular expressions. 

**Cheatsheet**

<table class="highlight-table">
<tr>
<th colspan=3>Character Classes</th>
<tr>
<td>.</td> <td>any character except newline</td>
<td class="example">
<f> / goo<h>.</h>gl / </f>
<t> <h>google</h> <h>goggle</h> gogle </t>
</td>
</tr>

<tr>
<td>\w \d \s</td> <td>word, digit, whitespace</td>
</tr>
<tr><td>\W \D \S</td> <td>not word, digit, whitespace</td></tr>

<tr>
<td>[abc]</td> <td>any of a, b or c</td>
<td class="example">
<f> /analy<h>[</h>sz<h>]</h>e/ </f>
<t><h>analyse</h> <h>analyze</h> analyxe </t>
</td>
</tr>

<tr>
<td>[^abc]</td> <td>not a, b or c</td>
<td class="example">
<f> /analy<h>[</h>sz<h>]</h>e/ </f>
<t>analyse analyze <h>analyxe</h> </t>
</td>
</tr>

<tr>
<td>[a-g]</td> <td>character between a & g</td>
<td class="example">
<f> /demo<h>[</h>2<h>-</h>4<h>]</h>/ </f>
<t> demo1 <h>demo2</h> <h>demo3</h> <h>demo4</h> demo5</t>
</td>
</tr>

<th colspan=2>Anchors</th>
<tr><td>^abc$</td> <td>start / end of the string</td></tr>
<tr><td>\b \B</td> <td>word, not-word boundary</td></tr>

<th colspan=2>Escaped characters</th>
<tr><td>\. \* \\</td> <td>escaped special characters</td></tr>
<tr><td>\t \n \r</td> <td>tab, linefeed, carriage return</td></tr>
<tr><td>\u00A9</td> <td>unicode escaped ©</td></tr>

<th colspan=2>Groups and Lockaround</th>
<tr><td>(abc)</td> <td>capture group</td></tr>
<tr><td>\1</td> <td>backreference to group #1</td></tr>
<tr><td>(?:abc)</td> <td>non-capturing group</td></tr>
<tr><td>(?=abc)</td> <td>positive lookahead</td></tr>
<tr><td>(?!abc)</td> <td>negative lookahead</td></tr>

<th colspan=2>Quantifiers & Alternation</th>
<tr><td>a* a+ a?</td> <td>0 or more, 1 or more, 0 or 1</td></tr>
<tr><td>a{5}, a{2,}</td> <td>exactly five, two or more</td></tr>
<tr><td>a{1,3}</td> <td>between one & three</td></tr>
<tr><td>a+? a{2,}?</td> <td>match as few as possible</td></tr>
<tr><td>ab|cd</td> <td>match ab or cd</td></tr>
</table>

**Related Readings**

* [http://regexr.com/](http://regexr.com/)
