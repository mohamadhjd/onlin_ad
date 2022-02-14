from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    describeMe = "show ad"

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.advertiser = advertiser
        self.checkId()

    def getTitle(self):
        return self.__title

    def setTitle(self, newTitle):
        self.__title = newTitle

    def getImgUrl(self):
        return self.__imgUrl

    def setImgUrl(self, newImgUrl):
        self.__imgUrl = newImgUrl

    def getLink(self):
        return self.__link

    def setLink(self, newLink):
        self.__link = newLink

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe

