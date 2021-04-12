import pandas


class CSVReader:

    def __init__(self):
        print("CSVReader = Inside Constructor")

    @staticmethod
    def parse_csv_file(file_name):
        df = pandas.read_csv(file_name)
        print(df)
