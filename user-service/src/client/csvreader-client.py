import fileutils.properties
import csvreader.csvread

propObj = fileutils.properties.AppProperties()
filepath = propObj.get_property('csv.read.filepath')
csvObject = csvreader.csvread.CSVReader(filepath)
csvObject.set_filename(filepath)
csvObject.parse_csv_file()
