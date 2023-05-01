import xml.etree.ElementTree as ET


def serialize(data):
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    return ET.tostring(root)


def deserialize(data):
    root = ET.fromstring(data)
    res = {}
    for child in root:
        res[child.tag] = child.text
    return res
