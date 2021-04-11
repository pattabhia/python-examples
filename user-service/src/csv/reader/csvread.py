
class CSVReader:

    __filename = ""

    def __init__(self):
        print("CSVReader = Inside Constructor")

    def getFileName(self):
        return self.__filename

    def setFileName(self, filename):
        self.__filename = filename
