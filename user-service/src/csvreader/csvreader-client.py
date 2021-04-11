from fileutils.properties import AppProperties
from csvreader.csvread import CSVReader

propObj = AppProperties()
filepath = propObj.get_property('csv.read.filepath')
csvObject = CSVReader()
csvObject.set_filename(filepath)
csvObject.parse_csv_file()
