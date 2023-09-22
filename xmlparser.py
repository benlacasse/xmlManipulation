import xml.etree.ElementTree as ET
import sys

if len(sys.argv) < 4:
    print("Enter the input from command line arguments.")
    print("usage: python xmlparser.py plant_catalog.xml plantName percent")
exit(0)

# Read the XML file
tree = ET.parse(sys.argv[1])
catalog = tree.getroot()


# Get catalog name from the command line argument
catalogName = sys.argv[2]

# Get percent change from the command line argument
percent = float(sys.argv[3])

if percent <= -90 or percent > 100:
    print("The percentage change Range is invalid")
    print("The range must be -90 < percentage < 100")
exit()

found = 0

for plant in catalog.findall('PLANT'):

     if plant.find('COMMON').text == catalogName:
        currPrice = float(plant.find('PRICE').text)
updatedPrice = (currPrice * percentChange)/100.00 + currPrice
plant.find('PRICE').text = str(updatedPrice)
found = 1

if found == 0:
    print("Data Not Found")
else:
    tree.write(sys.argv[1])
print("Data Updated Successfully")