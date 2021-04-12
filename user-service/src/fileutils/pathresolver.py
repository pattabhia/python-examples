import os


def resolve_path(basepath, file_name):
    if "data" in str(file_name):
        return os.path.join(basepath.data, file_name.data)
    else:
        print('incorrect path given for csv file')
    return
