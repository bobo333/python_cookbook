from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape,unescape


def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem

s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e)
print(tostring(e))

# can attach additional attributes
e.set('_id', '1234')
print(tostring(e))
print()

# can escape and unescape characters manually if desired
escaped = escape('<spam>')
print(escaped)
print(unescape(escaped))

