import xml.etree.ElementTree as etree

tree = etree.parse('drawing.svg')
tr = tree.getroot()

for i in range(20):
    b = bin(i)[2:]
    tr[3][4][0].text = "{0}{1}" .format(' '*(6-len(str(i))), i)
    tr[3][5][0].text = "{0}{1}" .format(' '*(6-len(b)), b)
    new = etree.ElementTree(old)
    new.write('drawing'+str(i)+'.svg')

    
