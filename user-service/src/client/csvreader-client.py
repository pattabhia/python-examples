from fileutils.properties import AppProperties
from fileutils.pathresolver import resolve_path
from csvreader.csvread import CSVReader

propObj = AppProperties()
file = resolve_path(propObj.get_property('base.path'), propObj.get_property('csv.read.filepath'))
CSVReader().parse_csv_file(file)
