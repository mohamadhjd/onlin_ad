class BaseAdvertising:
    describeMe = "shorten the code"
    count_id = 0

    def __init__(self, clicks=0, views=0):
        self.__id = BaseAdvertising.count_id
        self.__clicks = clicks
        self.__views = views
        BaseAdvertising.count_id += 1

    @property
    def clicks(self):
        return self.__clicks

    @property
    def views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

    @staticmethod
    def describe_me():
        return "the task of this class" + BaseAdvertising.describeMe

