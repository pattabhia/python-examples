from csvreader.csvread import CSVReader
from fileutils.pathresolver import resolve_path
from fileutils.properties import AppProperties


propObj = AppProperties()
file = resolve_path(propObj.get_property('base.path'), propObj.get_property('csv.read.filepath'))
CSVReader().parse_csv_file(file)
