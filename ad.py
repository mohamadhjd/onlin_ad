from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    describeMe = "show ad"

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.advertiser = advertiser

    def getTitle(self):
        print(self.__title)

    def setTitle(self, newTitle):
        self.__title = newTitle

    def getImgUrl(self):
        print(self.__imgUrl)

    def setImgUrl(self, newImgUrl):
        self.__imgUrl = newImgUrl

    def getLink(self):
        print(self.__link)

    def setLink(self, newLink):
        self.__link = newLink

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe

