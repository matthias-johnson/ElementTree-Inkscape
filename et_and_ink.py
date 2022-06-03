import xml.etree.ElementTree as etree

tree = etree.parse('drawing.svg')
tr = tree.getroot()

students = [
    "John Doe",
    "Bridget Yolo",
    "Roger Waters",
    ]

cnt = 0
for names in students:
    tr[3][1][0].text = "{0}" .format(names)
    new = etree.ElementTree(tr)
    new.write('drawing'+str(cnt)+'.svg')
    cnt += 1
