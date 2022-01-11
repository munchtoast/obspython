class item:
    def __init__(self, data):
        self.__data = data
        self.__record = 0
        self.__stream = 0
    
    def getData(self):
        return self.__data

    def getRecord(self):
        return bool (self.__record)
    
    def getStream(self):
        return bool (self.__stream)
    
    def setRecord(self, record):
        self.__record = record
    
    def setStream(self, stream):
        self.__stream = stream
    
    def setData(self, data):
        self.__data = data