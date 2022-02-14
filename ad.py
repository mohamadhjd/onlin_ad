from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    describeMe = "show ad"

    idList = []

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.id = id
        self.idList.insert(100, self.id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.advertiser = advertiser
        self.checkId()

    def checkId(self):
        count = 0
        for i in range(0, len(self.idList)):
            if self.idList[i] == self.id:
                count += 1
            if count >= 2:
                print("Id have to be unique")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, newTitle):
        self.__title = newTitle

    @property
    def imgUrl(self):
        return self.__imgUrl

    @imgUrl.setter
    def imgUrl(self, newImgUrl):
        self.__imgUrl = newImgUrl

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, newLink):
        self.__link = newLink

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
