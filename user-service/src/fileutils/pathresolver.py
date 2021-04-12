from pathlib import *
import os


def resolve_path(file_name):
    if "data" in str(file_name):
        return os.path.join(Path(__file__).parents[2], file_name.data)
    else:
        print('incorrect path given for csv file')
    return
