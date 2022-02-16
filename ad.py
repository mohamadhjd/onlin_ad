from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    describeMe = "show ad"
    count_id = 1

    def __init__(self, title, imgUrl, link, advertiser):
        super().__init__()
        self.__id = Ad.count_id
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser
        Ad.count_id += 1

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__advertiser.incClicks()

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, newTitle):
        self.__title = newTitle

    @property
    def imgUrl(self):
        return self.__imgUrl

    def help(self):
        return f'title of ad is {self.__title} . imgUrl is {self.__imgUrl} and link is {self.__link} . count of clicks is {self.clicks} and count of views {self.views} '

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
    def describe_me(DescribeMe=describeMe):
        return "the task of this class" + DescribeMe
