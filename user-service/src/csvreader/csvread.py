import pandas


class CSVReader:

    def __init__(self, filepath):
        print("CSVReader = Inside Constructor")
        self.__filename = filepath

    @property
    def get_filename(self) -> str:
        return self.__filename

    def parse_csv_file(self):
        print(self.get_filename)
        df = pandas.read_csv('../../resources/employee.csv')
        print(df)
