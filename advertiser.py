from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    describeMe = "show advertiser"

    idList = []
    total_clicks = 0

    def __init__(self, id, name, clicks=0):
        super().__init__(id, clicks)
        self.__id = id
        self.__clicks = clicks
        self.idList.insert(100, self.__id)
        self.__name = name
        self.checkId()

    def checkId(self):
        count = 0
        for i in range(0, len(self.idList)):
            if self.idList[i] == self.__id:
                count += 1
            if count >= 2:
                print("Id have to be unique")

    def incClicks(self):
        self.__clicks += 1
        Advertiser.total_clicks += 1
        return Advertiser.total_clicks
    @property
    def clicks(self):
        return self.__clicks

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
    def getTotalClicks(totalClicks=total_clicks):
        print(totalClicks)

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
