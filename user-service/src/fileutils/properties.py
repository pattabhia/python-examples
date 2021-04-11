from jproperties import Properties
from pathlib import Path


class AppProperties:

    __configs = object()

    def __init__(self):
        print('AppProperties = Constructor')
        self.__configs = Properties()
        self.init_properties()

    def exists(file):
        try:
            with open(file) as f:
                print('file exists')
        except IOError:
            print('file not accessible')

    def init_properties(self):
        project_root = Path(__file__).parents[2]
        prop_file_path = project_root / 'resources/app-config.properties'
        try:
            with open(prop_file_path, 'rb') as config_file:
                self.get_config().load(config_file)
        except Exception as ex:
            print('prop file error', str(ex))

    def get_property(self, key):
        return self.get_config().get(key)

    def get_config(self):
        return self.__configs