from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    describeMe = "show advertiser"

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name
        self.checkId()

    def getName(self):
        return self.__name

    def setName(self, newNme):
        self.__name = newNme

    def help(self):
        return f'name of advertiser is {self.__name}.count of clicks is {self.getClicks()} and count of views {self.getViews()}'

    @staticmethod
    def getTotalClicks(totalClicks):
        print(totalClicks)

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
