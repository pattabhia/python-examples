from fileutils import BaseProperties


class AppProperties(BaseProperties):

    def __init__(self):
        super().__init__()
        print('AppProperties = Constructor')


def get_property(key):
    return BaseProperties().get_property(key)
