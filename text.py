import requests
import lxml.html
import json
import datetime
import csv
import time
import urllib.request
from bs4 import BeautifulSoup


total_rank = []
Osinjuku = []
# オリエンタルランド東京のみ
def test():
    yu = requests.get("https://oriental-lounge.com/")
    html = lxml.html.fromstring(yu.content)
    # 新宿店
    Osinjuku_man = html.xpath(
        '//*[@id="shop"]/div/div/div[6]/div[1]/ul/li[1]/span')[0].text
    Osinjuku_woman = html.xpath(
        '//*[@id="shop"]/div/div/div[6]/div[1]/ul/li[2]/span')[0].text
    shop_Osinjuku = "ORIENTAL LOUNGE新宿店"
    shop_Osinjuku_url = "https://goo.gl/maps/ZwFwF3Vb3pyHSu3a7"
    Osinjuku_total = int(Osinjuku_man) - int(Osinjuku_woman)
    Osinjuku.append(Osinjuku_man)
    Osinjuku.append(Osinjuku_woman)
    Osinjuku.append(shop_Osinjuku)
    Osinjuku.append(shop_Osinjuku_url)
    # Osinjuku_total = 2
    total_rank.append(Osinjuku_total)
    # Osinjuku = [int(Osinjuku_man), int(Osinjuku_woman),
    #             shop_Osinjuku, shop_Osinjuku_url, int(Osinjuku_total)]
# print(Osinjuku)
test()
print(Osinjuku)