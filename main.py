from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

baseAdvertising = BaseAdvertising()

advertiser1 = Advertiser("name1")
advertiser2 = Advertiser("name2")
advertiser3 = Advertiser("name3")
ad1 = Ad("title1", "img-url1", "lik1", advertiser1)
ad2 = Ad("title2", "img-url2", "lik2", advertiser2)

print(ad1.id)
print(ad2.id)
print(advertiser1.id)
print(advertiser2.id)
print(advertiser3.id)
print(advertiser1.help())
print(ad1.help())