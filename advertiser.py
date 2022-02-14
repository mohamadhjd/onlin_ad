from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    describeMe = "show advertiser"

    idList = []

    def __init__(self, id, name):
        super().__init__(id)
        self.id = id
        self.idList.insert(100, self.id)
        self.__name = name
        self.checkId()

    def checkId(self):
        count = 0
        for i in range(0, len(self.idList)):
            if self.idList[i] == self.id:
                count += 1
            if count >= 2:
                print("Id have to be unique")


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
