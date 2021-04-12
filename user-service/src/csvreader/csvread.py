import pathlib

import pandas
from pathlib import *
import os


class CSVReader:

    def __init__(self, filepath):
        print("CSVReader = Inside Constructor")
        self.__filename = filepath

    @property
    def get_filename(self) -> str:
        return self.__filename

    def parse_csv_file(self):
        print(self.get_filename)
        if "data" in str(self.get_filename):
            fn = os.path.join(Path(__file__).parents[2], self.get_filename.data)
            df = pandas.read_csv(fn)
            print(df)
        else:
            print('incorrect path given for csv file')
