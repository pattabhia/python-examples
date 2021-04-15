from csvreader.csvread import CSVReader
from fileutils.pathresolver import resolve_path
from fileutils.properties import AppProperties, get_property

propObj = AppProperties()
file = resolve_path(get_property('base.path'), get_property('csv.read.filepath'))
CSVReader().parse_csv_file(file)
