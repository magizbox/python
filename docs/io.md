# JSON

**Write json file with pretty format and unicode**

```python
import json
import io

data = {
    "menu": {
        "header": "Sample Menu",
        "items": [
            {"id": "Open"},
            {"id": "OpenNew", "label": "Open New"},
            None,
            {"id": "Help"},
            {"id": "About", "label": "About Adobe CVG Viewer..."}
        ]
    }}

with io.open("sample_json.json", "w", encoding="utf8") as f:
    content = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    f.write(unicode(content))
```

Result

```
{
    "menu": {
        "header": "Sample Menu",
        "items": [
            {
                "id": "Open"
            },
            {
                "id": "OpenNew",
                "label": "Open New"
            },
            null,
            {
                "id": "Help"
            },
            {
                "id": "About",
                "label": "About Adobe CVG Viewer..."
            }
        ]
    }
}
```

**Read json file**

```python
import json
from pprint import pprint

with open('sample_json.json') as data_file:
    data = json.load(data_file)

pprint(data)
```

Result

```
{u'menu': {u'header': u'Sample Menu',
           u'items': [{u'id': u'Open'},
                      {u'id': u'OpenNew', u'label': u'Open New'},
                      None,
                      {u'id': u'Help'},
                      {u'id': u'About',
                       u'label': u'About Adobe CVG Viewer...'}]}}
```

**Related Reading**

* Parsing values from a JSON file in Python, [stackoverflow](http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python)
* How do I write JSON data to a file in Python?, [stackoverflow](http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python)

# XML

**Write xml file with `lxml` package**

```python
import lxml.etree as ET
# root declaration
root = ET.Element('catalog')
# insert comment
comment = ET.Comment(' this is a xml sample file ')
root.insert(1, comment)
# book element
book = ET.SubElement(root, 'book', id="bk001")
# book data
author = ET.SubElement(book, 'author')
author.text = "Gambardella, Matthew"
title = ET.SubElement(book, 'title')
title.text = "XML Developer's Guide"
# write xml to file
tree = ET.ElementTree(root)
tree.write("sample_book.xml", pretty_print=True, xml_declaration=True, encoding='utf-8')
```

Result

```xml
<?xml version='1.0' encoding='UTF-8'?>
<catalog>
  <!-- this is a xml sample file -->
  <book id="bk001">
    <author>Gambardella, Matthew</author>
    <title>XML Developer's Guide</title>
  </book>
</catalog>
```

**Read xml file with `lxml` package**

```python
from lxml import etree as ET

tree = ET.parse("sample_book.xml")
root = tree.getroot()
book = root.find('book')
print "Book Information"
print "ID     :", book.attrib["id"]
print "Author :", book.find('author').text
print "Title  :", book.find('title').text
```

Result

```
Book Information
ID     : bk001
Author : Gambardella, Matthew
Title  : XML Developer's Guide
```



