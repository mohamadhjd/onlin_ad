from base_model import BaseAdvertising
from ad import Ad


class Advertiser(BaseAdvertising):
    describeMe = "show advertiser"

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name
        self.checkId()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def help(self):
        return f'name of advertiser is {self.__name}.count of clicks is {self.getClicks()} and count of views {self.getViews()} '

    @staticmethod
    def getTotalClicks(count):
        return count

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
