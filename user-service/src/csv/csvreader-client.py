from csv.reader import CSVReader
from fileutils.fileutilities import FileUtils
csvObject = CSVReader()
csvObject.setFileName("test.txt")
FileUtils.exists(csvObject.getFileName())
