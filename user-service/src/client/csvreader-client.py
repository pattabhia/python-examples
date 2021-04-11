from fileutils.properties import AppProperties
from csvreader.csvread import CSVReader

propObj = AppProperties()
filepath = propObj.get_property('csv.read.filepath')
csvObject = CSVReader(filepath)
csvObject.parse_csv_file()
