from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    describeMe = "show advertiser"

    total_clicks = 0
    count_id = 1

    def __init__(self, name, clicks=0):
        super().__init__(clicks)
        self.__id = Advertiser.count_id
        self.__clicks = clicks
        self.__name = name
        Advertiser.count_id += 1

    @property
    def id(self):
        return self.__id

    def inc_clicks(self):
        super(Advertiser, self).inc_clicks()
        Advertiser.total_clicks += 1

    @property
    def clicks(self):
        return self.__clicks

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    def help(self):
        return f'name of advertiser is {self.__name}.count of clicks is {self.clicks} and count of views {self.views}'

    @staticmethod
    def get_total_clicks():
        return Advertiser.total_clicks

    @staticmethod
    def describe_me():
        return "the task of this class" + Advertiser.describeMe
