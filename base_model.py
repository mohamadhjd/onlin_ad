class BaseAdvertising:
    describeMe = "shorten the code"

    def __init__(self, id=1, clicks=0, views=0):
        self.__id = id
        self.__clicks = clicks
        self.__views = views

    def checkId(self):
        if self.__id <= 0:
            print("Id have to the integer")

    @property
    def clicks(self):
        return self.__clicks

    @property
    def views(self):
        return self.__views

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe

    def get_totalClicks(self):
        return self.totalClicks
