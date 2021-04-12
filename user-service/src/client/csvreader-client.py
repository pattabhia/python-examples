from fileutils.properties import *
from csvreader.csvread import CSVReader

propObj = AppProperties()
csvObject = CSVReader(propObj.get_property('csv.read.filepath'))
csvObject.parse_csv_file()
