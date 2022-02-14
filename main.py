from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "lik1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "lik2", advertiser2)


print(baseAdvertising.describeMe())
print(ad2.describeMe())
print(advertiser1.describeMe())
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
advertiser1.incClicks()
advertiser1.incClicks()
advertiser2.incClicks()
print(advertiser1.getClicks())
print(advertiser2.getName())
print(ad1.getClicks())
print(advertiser2.getClicks())
totalClicks = baseAdvertising.get_totalClicks()
Advertiser.getTotalClicks(totalClicks)
print(advertiser1.help())
print(advertiser2.help())
