import html
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print(s)

print(html.escape(s))

# disable escaping quotes
print(html.escape(s, quote=False))
print()

# embed entities for non-ASCII characters
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
print()

# should use an html or xml parser first, but may need this at some point:
s = 'Spicy &quot;Jalape&#241;o&quot'
print(html.unescape(s))
print()

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
