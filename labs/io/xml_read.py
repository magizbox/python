from lxml import etree as ET

tree = ET.parse("sample_book.xml")
root = tree.getroot()
book = root.find('book')
print "Book Information"
print "ID     :", book.attrib["id"]
print "Author :", book.find('author').text
print "Title  :", book.find('title').text
