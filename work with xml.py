from xml.etree import ElementTree
xmlstr = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
root = ElementTree.fromstring(xmlstr)
rgb = {'red':0,"green":0,"blue":0}

def value(start,v=0):
    v += 1
    rgb[start.attrib["color"]] += v
    for e in start:
        value(e, v)


value(root)

print(rgb['red'], rgb['green'], rgb['blue'])

