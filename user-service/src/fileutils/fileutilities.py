from jproperties import Properties

configs = Properties()


def exists(file):
    try:
        with open(file) as f:
            print('file exists')
    except IOError:
        print('file not accessible')


def getproperty():
    try:
        with open('app-config.properties', 'rb') as config_file:
            configs.load(config_file)
    except IOError:
        print('prop file error')


getproperty()
print(configs.get("csv.read.filepath"))
