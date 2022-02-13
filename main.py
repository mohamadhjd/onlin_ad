from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising


advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "lik1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "lik2", advertiser2)

ad1.get_describeMe()
