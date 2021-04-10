from csv.reader import CSVReader
from fileutils.fileutilities import exists

csvObject = CSVReader()

csvObject.setFileName("test.txt")

exists(csvObject.getFileName())
