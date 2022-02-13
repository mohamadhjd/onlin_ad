from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    def __init__(self, id,  name):
        super().__init__(id)
        self.__name = name

    def getName(self):
        print(self.__name)

    def setName(self, newNme):
        self.__name = newNme

    @staticmethod
    def help():
        print("We have a class called Advertiser that contains the information and methods of system advertisers")

    @staticmethod
    def getTotalClicks():
        pass

    def get_describeMe(self):
        print(f'{self.describeMe} show advertiser')
