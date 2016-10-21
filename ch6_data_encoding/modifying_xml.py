from xml.etree.ElementTree import parse, Element

# parse and modify document
doc = parse('data_files/pred.xml')
root = doc.getroot()
print(root)

# remove some elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
print(root.getchildren().index(root.find('nm')))    # will give 1, so insert as 2 to go after
e = Element('spam')
e.text = 'This is a test, this is only a test.'
root.insert(2, e)

# write back to a file
doc.write('data_files/newpred.xml', xml_declaration=True)

# remember that all modifications are generally made to the parent element, treating it as
# if it were a list
