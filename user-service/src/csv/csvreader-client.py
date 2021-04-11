from fileutils.properties import AppProperties
from csv.reader import CSVReader
csvObject = CSVReader()
csvObject.setFileName("test.txt")
propObj = AppProperties()
print(propObj.get_property('DB_User'))
