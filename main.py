from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(2, "title1", "img-url1", "lik1", advertiser1)
ad2 = Ad(3, "title2", "img-url2", "lik2", advertiser2)


print(baseAdvertising.describeMe())
print(ad2.describeMe())
print(advertiser1.describeMe())
ad1.incClicks()
ad1.link = 'new lik'
print(ad1.clicks)
print(ad1.link)
