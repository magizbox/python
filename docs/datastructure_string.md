## Format

```python
'{0}, {1}, {2}'.format('a', 'b', 'c')
# 'a, b, c'
```

## Regular Expressions

The aim of this chapter of our Python tutorial is to present a detailed led and descriptive introduction into regular expressions. This introduction will explain the theoretical aspects of regular expressions and will show you how to use them in Python scripts. 

Regular Expressions are used in programming languages to filter texts or textstrings. It's possible to check, if a text or a string matches a regular expression. 

There is an aspect of regular expressions which shouldn't go unmentioned: The syntax of regular expressions is the same for all programming and script languages, e.g. Python, Perl, Java, SED, AWK and even X#.

### Functions

#### match function

This function attempts to match RE pattern to string with optional flags.

```
re.match(pattern, string, flags=0)
```

Example

```python
import re

line = "Cats are smarter than dogs"

matched_object = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matched_object:
    print "matched_object.group()  : ", matched_object.group()
    print "matched_object.group(1) : ", matched_object.group(1)
    print "matched_object.group(2) : ", matched_object.group(2)
else:
    print "No match!!"
```

When the code is executed, it produces following results

```
matched_object.group()  :  Cats are smarter than dogs
matched_object.group(1) :  Cats
matched_object.group(2) :  smarter
```

#### search function

This function searches for first occurrence of RE pattern within stirng with optional flags

```
re.search(pattern, string, flags=0)
```

Example

```python
#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

search_object = re.search(r'dogs', line, re.M | re.I)
if search_object:
    print "search --> search_object.group() : ", search_object.group()
else:
    print "Nothing found!!"
```

When the code is executed, it produces following results

```
search --> search_object.group() :  dogs
```

#### sub function

This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max provided. This method returns modified string.

```
re.sub(pattern, repl, string, max=0)
```

Example

```python
#!/usr/bin/python
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
```

When the code is executed, it produces following results

```
Phone Num :  2004-959-559
Phone Num :  2004959559
```

### Tokens Cheatsheet

<table class="highlight-table">
<tr>
<th colspan=3>Character Classes</th>
<tr>
<td>.</td> <td>any character except newline</td>
<td class="example">
<f> /go<h>.</h>gle/ </f>
<t> <h>google</h> <h>goggle</h> gogle </t>
</td>
</tr>

<tr>
<td>\w \d \s</td> <td>word, digit, whitespace</td>
<td class="example">
<f> /<h>\w</h>/ </f>
<t> <h>AaYyz09</h> ?! </t>
<f> /<h>\d</h>/ </f>
<t> <h>0</h><h>1</h><h>2</h><h>3</h><h>4</h><h>5</h> aZ? </t>
<f> /<h>\s</h>/ </f>
<t> 0123456789<h> </h>abcd?/ </t>
</td>
</tr>


<tr>
<td>\W \D \S</td> <td>not word, digit, whitespace</td>
<td class="example">
<f> /<h>\W</h>/ </f>
<t> abcded<h>&nbsp;</h><h>&nbsp;</h><h>&nbsp;</h>1234<h> </h><h>?</h><h>></h></t>
<f> /<h>\D</h>/ </f>
<t> <h>a</h><h>b</h><h>c</h> 12345 <h>?</h><h><</h><h>.</h><h>&nbsp;</h><h>&nbsp;</h></t>
<f> /<h>\S</h>/ </f>
<t> <h>a</h><h>b</h><h>c</h>&nbsp;&nbsp;&nbsp;<h>1</h><h>2</h><h>3</h><h>?</h>&nbsp;&nbsp;<h><</h><h>.</h></t>
</td>
</tr>

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
<f> /analy<h>[</h>^sz<h>]</h>e/ </f>
<t>analyse analyze <h>analyxe</h> </t>
</td>
</tr>

<tr>
<td>[a-g]</td> <td>character between a & g</td>
<td class="example">
<f> /<h>[</h>2<h>-</h>4<h>]</h>/ </f>
<t> demo1 <h>demo2</h> <h>demo3</h> <h>demo4</h> demo5</t>
</td>
</tr>

<th colspan=3>Quantifiers & Alternation</th>
<tr><td>a* a+ a?</td> <td>0 or more, 1 or more, 0 or 1</td>
<td class="example">
<f> /go<hb>*</hb>gle/ </f>
<t> <h>gogle</h> <h>gogle</h> <h>google</h> <h>gooooogle</h> hgle</t>
<f> /go<hb>+</hb>gle/ </f>
<t> ggle <h>gogle</h> <h>google</h> <h>gooooogle</h> hgle</t>
<f> /go<hb>?</hb>gle/ </f>
<t> <h>ggle</h> <h>gogle</h> google gooooogle hgle</t>
</td>
</tr>

<tr><td>a{5}, a{2,}</td> <td>exactly five, two or more</td>
<td class="example">
<f> /go<hb>{5}</hb>gle/ </f>
<t> gogle gogle google <h>gooooogle</h> hgle</t>
<f> /go<hb>{2,}</hb>gle/ </f>
<t> gogle gogle <h>google</h> <h>gooooogle</h> hgle</t>
</td>
</tr>
<tr><td>a{1,3}</td> <td>between one & three</td>
<td class="example">
<f> /go<hb>{1,3}</hb>gle/ </f>
<t> gogle <h>gogle</h> <h>google</h> <h>gooogle</h> gooooogle hgle</t>
</td>
</tr>
<tr><td>a+? a{2,}?</td> <td>match as few as possible</td>
<td class="example">
<f> /a<hb>+?</hb>/ </f>
<t> <h>a</h> <h>aa</h> <h>aaaaaa</h></t>
<f> /a<hb>{2,}?</hb>/ </f>
<t> a <h>aa</h> <h>aaaaaa</h></t>
</td>
</tr>
<tr><td>ab|cd</td> <td>match ab or cd</td>
<td class="example">
<f> /demo<hb>|</hb>example/ </f>
<t> <h>demo</h> <h>example</h> <h>example</h>1</t>
</td>
</tr>

<th colspan=3>Anchors</th>
<tr><td>^abc$</td> <td>start / end of the string</td>
<td class="example">
<f> /<h>^abc$</h>/ </f>
<t> <h>abc</h></t>
<f> /<h>^abc</h>/ </f>
<t> <h>abc</h> abc</t>
<f> /<h>abc$</h>/ </f>
<t> abc <h>abc</h></t>
</td></tr>
<tr>
<td>\b \B</td> <td>	word, not-word boundary</td>
<td class="example">
<f> /<h>\b</h>is<h>\b</h>/ </f>
<t>This island <h>is</h> beautiful.</t>
<f> /<h>\B</h>cat<h>\B</h>/ </f>
<t> cat certifi<h>cat</h>e</t>
</td>
</tr>

<th colspan=3>Escaped characters</th>
<tr><td>\. \* \\</td> <td>escaped special characters</td>
<td class="example">
<f> /<hp>\.</hp>/ </f>
<t> username@exampe<h>.</h>com 300<h>.</h>000 USD</t>
<f> /<hp>\*</hp>/ </f>
<t> abc@&%$<h>*</h>123</t>
<f> /<hp>\\</hp>/ </f>
<t> abc@&%$<h>\\</h>123</t>
</td>
</tr>

<tr><td>\t \n \r</td> <td>tab, linefeed, carriage return</td>
<td class="example">
<f> /<hp>\t</hp>/ </f>
<t> abc<h>&#09;</h>def</t>
<f> /ab<hp>\n</hp>/ </f>
<t> <h>ab</h></br></t>
<f> /<hp>\r</hp>/ </f>
<t> abc@&%$<h>\\</h>123</t>
</td>
</tr>

<tr>
<td>\u00A9</td> <td>unicode escaped ©</td><td class="example">
<f> /<hp>\u00A9</hp>/ </f>
<t> Copyright<h>©</h>2017 - All rights reserved</t>
</td>
</tr>

<th colspan=3>Groups and Lockaround</th>
<tr><td>(abc)</td> <td>capture group</td>
<td class="example">
<f> /<hbg><hg>(</hg>demo<hb>|</hb>example<hg>)</hbg><hby></hg><h>[0-9]</h></hby>/ </f>
<t> <h>demo1</h><h>example4</h>demo </t>
</td>
</tr>

<tr><td>\1</td> <td>backreference to group #1</td>
<td class="example">
<f> /<hbg><hg>(</hg>abc<hb>|</hb>def<hg>)</hbg>=<hg>\1</hg>/</f>
<t> <h>abc=abc</h> <h>def=def</h>abc=def </t>
</td>
</tr>

<tr><td>(?:abc)</td> <td>non-capturing group</td>
<td class="example">
<f> /<hbg><hg>(</hg><hg>?:</hg>abc<hg>)</hg></hbg><hb>{3}</hb>/</f>
<t> <h>abcabcabc</h> abcabc</h> </t>
</td>
</tr>

<tr><td>(?=abc)</td> <td>positive lookahead</td>
<td class="example">
<f> /t<hbg><hg>(?=</hg>s<hg>)</hg></hbg>/</f>
<t> tt<h>t</h>ssstt<h>t</h>ss </t>
</td>
</tr>

<tr><td>(?!abc)</td> <td>negative lookahead</td>
<td class="example">
<f> /t<hbg><hg>(?!</hg>s<hg>)</hg></hbg>/</f>
<t> <h>t</h><h>t</h>tsss<h>t</h><h>t</h>tss </t>
</td>
</tr>

<tr>
<td>(?<=abc)</td> <td>positive lookbehind</td>
<td class="example">
<f> /<hbg><hg>(?<=</hg>foo<hg>)</hg></hbg>bar/</f>
<t> foo<h>bar</h> fuubar </t>
</td>
</tr>

<tr>
<td>(?&lt;!abc)</td> <td>negative lookbehind</td>
<td class="example">
<f> /<hbg><hg>(?&lt;!</hg>foo<hg>)</hg></hbg>bar/ </f>
<t> foobar fuu<h>bar</h> </t>
</td>
</tr>

</table>

**Related Readings**

* Online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript, [regex101.com](https://regex101.com/)
* RegExr: Learn, Build, & Test RegEx, [regexr.com](http://regexr.com/)


