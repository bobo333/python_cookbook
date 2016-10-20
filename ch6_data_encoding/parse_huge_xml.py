from xml.etree.ElementTree import parse, iterparse
from collections import Counter

# rank zip codes by pot holes in Chicago
potholes_by_zip = Counter()

doc = parse('data_files/chicago_potholes.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


# above code works, but it reads the entire doc into memory
# this does it iteratively. It is slower, but much more memory-efficient
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    # skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':                # start events are when the beginning of an element is found, but it hasn't
                                            # been populate with data yet
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':                # end events are when an element is completed and has data
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)     # removes the previously-yielded element (the previous row) to be
                                                # removed from its parent. As long as there is no reference to it
                                                # elsewhere, its memory will be collected
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


potholes_by_zip2 = Counter()

# get this file from https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Pot-Holes-Reported/7as2-ds3y
data = parse_and_remove('data_files/chicago_potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip2[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip2.most_common():
    print(zipcode, num)
