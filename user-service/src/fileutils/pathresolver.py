import os


def resolve_path(path, file_name):
    if "data" in str(file_name):
        return os.path.join(path.data, file_name.data)
    else:
        print('incorrect path given for csv file')
    return
