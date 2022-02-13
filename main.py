from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

baseAdvertising = BaseAdvertising(1)
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "lik1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "lik2", advertiser2)

baseAdvertising.get_describeMe()
ad2.get_describeMe()
advertiser1.get_describeMe()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
advertiser2.getName()
ad1.getClicks()
advertiser2.getClicks()
Advertiser.getTotalClicks()
Advertiser.help()