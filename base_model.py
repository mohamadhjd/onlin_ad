
class BaseAdvertising:
    totalClicks = 0

    def __init__(self, id):
        self.__id = id
        self.clicks = 0
        self.views = 0
        self.describeMe = "The task of this class"

    def getClicks(self):
        print(self.clicks)

    def getViews(self):
        print(self.views)

    def incClicks(self):
        self.clicks += 1
        self.totalClicks += 1

    def incViews(self):
        self.views += 1

    def get_describeMe(self):
        print(f'{self.describeMe} shorten the code')
        return self.describeMe

    def get_totalClicks(self):
        return self.totalClicks
