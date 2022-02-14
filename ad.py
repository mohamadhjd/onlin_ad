from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    describeMe = "show ad"

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self._link = link
        self.advertiser = advertiser
        self.checkId()

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
        return self._link

    @link.setter
    def link(self, newLink):
        self._link = newLink

    @staticmethod
    def describeMe(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
