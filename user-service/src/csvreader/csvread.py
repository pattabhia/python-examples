import pandas

class CSVReader:
    __filename = ""

    def __init__(self):
        print("CSVReader = Inside Constructor")

    def get_filename(self):
        return self.__filename

    def set_filename(self, filename):
        self.__filename = filename

    def parse_csv_file(self):
        print(self.get_filename())
        df = pandas.read_csv('../../resources/employee.csv')
        print(df)
