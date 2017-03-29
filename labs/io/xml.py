import lxml.etree as ET

root = ET.Element('note')

comment = ET.Comment(' this is a xml sample file ')
root.insert(1, comment)

to = ET.SubElement(root, 'to')
to.text = "Tove"
from_ = ET.SubElement(root, 'from')
from_.text = "Jani"
heading = ET.SubElement(root, 'heading')
heading.text = "Reminder"
body = ET.SubElement(root, 'body')
body.text = "Don't forget me this weekend!"


tree = ET.ElementTree(root)
tree.write("sample_note.xml", pretty_print=True, xml_declaration=True, encoding='utf-8')
