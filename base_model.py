
class BaseAdvertising:
    totalClicks = 0
    describeMe = "shorten the code"

    def __init__(self, id):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def checkId(self):
        if self.__id <= 0:
            print("Id have to the integer")

    def getClicks(self):
        return self.__clicks

    def getViews(self):
        return self.__views

    def incClicks(self):
        self.__clicks += 1
        self.totalClicks += 1

    def incViews(self):
        self.__views += 1

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe

    def get_totalClicks(self):
        return self.totalClicks
