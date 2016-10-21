from xml.etree.ElementTree import parse, iterparse

# parsing xml documents with multiple levels of nesting can become tedious
doc = parse('data_files/author.xml')
print(doc.findtext('author'))

print(doc.find('content'))

# query involving a namespace (doesn't work)
print(doc.find('content/html'))     # prints None

# also doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))    # prints None

# works if fully qualified
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
                   '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))
print()


# but there's an easier way...
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, url in kwargs.items():
            self.register(name, url)

    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'

    def __call__(self, path):
        return path.format_map(self.namespaces)

# to use the class
# still not great, but better
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))
print()

# can also use iterparse and get more information about the namespaces
for evt, elem in iterparse('data_files/author.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)

print(elem)     # this is the topmost element

# in general, if using more advanced features like namespaces, probably better to use lxml
