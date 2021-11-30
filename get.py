# -*- coding: utf-8 -*-
import requests
import lxml.html
import json
import datetime
import csv
import time
import urllib.request



total_rank = []
Osinjuku = []
Osibuya = []
Osibuya_ekimae = []
Omachida= []
Akabukicho = []
Asinnjuku_east =[]
Aikebukuro_east = []
Aikebukuro_west = []
Aebisu = []
Aueno =[] 
Ashibuya = []
Akinshicho =[] 
Lshibuya =[]
Lebisu = []
vivo = []

def test():
    # -*- coding: utf-8 -*-
    yu = requests.get("https://oriental-lounge.com/")
    html = lxml.html.fromstring(yu.content)
    Osinjuku_man = html.xpath(
        '//*[@id="shop"]/div/div/div[6]/div[1]/ul/li[1]/span')[0].text
    Osinjuku_woman = html.xpath(
        '//*[@id="shop"]/div/div/div[6]/div[1]/ul/li[2]/span')[0].text
    shop_Osinjuku = "ORIENTAL LOUNGE新宿店"
    shop_Osinjuku_url = "https://goo.gl/maps/ZwFwF3Vb3pyHSu3a7"
    Osinjuku_total = int(Osinjuku_man) - int(Osinjuku_woman)
    total_rank.append(Osinjuku_total)
    Osinjuku.append(Osinjuku_man)
    Osinjuku.append(Osinjuku_woman)
    Osinjuku.append(shop_Osinjuku)
    Osinjuku.append(shop_Osinjuku_url)
    Osinjuku.append(Osinjuku_total)
    


    Osibuya_man = html.xpath(
        '//*[@id="shop"]/div/div/div[7]/div[1]/ul/li[1]/span')[0].text
    Osibuya_woman = html.xpath(
        '//*[@id="shop"]/div/div/div[7]/div[1]/ul/li[2]/span')[0].text
    shop_Osibuya = "ORIENTAL LOUNGE渋谷本店"
    shop_Osibuya_url = "https://goo.gl/maps/byJoUQht9eSSR9P96"
    Osibuya_total = int(Osibuya_man) - int(Osibuya_woman)
    total_rank.append(Osibuya_total)
    Osibuya.append(Osibuya_man)
    Osibuya.append(Osibuya_woman)
    Osibuya.append(shop_Osibuya)
    Osibuya.append(shop_Osibuya_url)
    Osibuya.append(Osibuya_total)


    
    Osibuya_ekimae_man = html.xpath(
        '//*[@id="shop"]/div/div/div[9]/div[1]/ul/li[1]/span')[0].text
    Osibuya_ekimae_woman = html.xpath(
        '//*[@id="shop"]/div/div/div[9]/div[1]/ul/li[2]/span')[0].text
    shop_Osibuya_ekimae = "ORIENTAL LOUNGE渋谷駅前店"
    shop_Osibuya_ekimae_url = "https://goo.gl/maps/AxemztM6eavXB6XY9"
    Osibuya_ekimae_total = int(Osibuya_ekimae_man) - int(Osibuya_ekimae_woman)
    total_rank.append(Osibuya_ekimae_total)
    Osibuya_ekimae.append(Osibuya_ekimae_man)
    Osibuya_ekimae.append(Osibuya_ekimae_woman)
    Osibuya_ekimae.append(shop_Osibuya_ekimae)
    Osibuya_ekimae.append(shop_Osibuya_ekimae_url)
    Osibuya_ekimae.append(Osibuya_ekimae_total)

    
    Omachida_man = html.xpath(
        '//*[@id="shop"]/div/div/div[10]/div[1]/ul/li[1]/span')[0].text
    Omachida_woman = html.xpath(
        '//*[@id="shop"]/div/div/div[10]/div[1]/ul/li[2]/span')[0].text
    shop_Omachida = "ORIENTAL LOUNGE町田店"
    shop_Omachida_url = "https://g.page/oriental-lounge-machida?share"
    Omachida_total = int(Omachida_man) - int(Omachida_woman)
    total_rank.append(Omachida_total)
    Omachida.append(Omachida_man)
    Omachida.append(Omachida_woman)
    Omachida.append(shop_Omachida)
    Omachida.append(shop_Omachida_url)
    Omachida.append(Omachida_total)

    
    yu = requests.get("https://aiseki-ya.com/")
    html = lxml.html.fromstring(yu.content)
    
    Akabukicho_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[1]/div[2]/span')[0].text
    Akabukicho_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[1]/div[3]/span')[0].text
    shop_Akabukicho = "相席屋歌舞伎町店"
    shop_Akabukicho_url = "https://goo.gl/maps/BBXWjksqacTDrnKT6"
    Akabukicho_total = int(Akabukicho_man) - int(Akabukicho_woman)
    total_rank.append(Akabukicho_total)
    Akabukicho.append(Akabukicho_man)
    Akabukicho.append(Akabukicho_woman)
    Akabukicho.append(shop_Akabukicho)
    Akabukicho.append(shop_Akabukicho_url)
    Akabukicho.append(Akabukicho_total)

    
    Asinnjuku_east_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[2]/div[2]/span')[0].text
    Asinnjuku_east_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[2]/div[3]/span')[0].text
    shop_Asinnjuku_east = "相席屋２ON２新宿東口店"
    shop_Asinnjuku_east_url = "https://goo.gl/maps/wRfFYikryS3zPmoUA"
    Asinnjuku_east_total = int(Asinnjuku_east_man) - int(Asinnjuku_east_woman)
    total_rank.append(Asinnjuku_east_total)
    Asinnjuku_east.append(Asinnjuku_east_man)
    Asinnjuku_east.append(Asinnjuku_east_woman)
    Asinnjuku_east.append(shop_Asinnjuku_east)
    Asinnjuku_east.append(shop_Asinnjuku_east_url)
    Asinnjuku_east.append(Asinnjuku_east_total)

    
    Aikebukuro_east_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[3]/div[2]/span')[0].text
    Aikebukuro_east_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[3]/div[3]/span')[0].text
    shop_Aikebukuro_east = "相席屋池袋東口店"
    shop_Aikebukuro_east_url = "https://goo.gl/maps/vHW1Bgp4hKmcBFfA9"
    Aikebukuro_east_total = int(Aikebukuro_east_man) - int(Aikebukuro_east_woman)
    total_rank.append(Aikebukuro_east_total)
    Aikebukuro_east.append(Aikebukuro_east_man)
    Aikebukuro_east.append(Aikebukuro_east_woman)
    Aikebukuro_east.append(shop_Aikebukuro_east)
    Aikebukuro_east.append(shop_Aikebukuro_east_url)
    Aikebukuro_east.append(Aikebukuro_east_total)

    
    Aikebukuro_west_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[4]/div[2]/span')[0].text
    Aikebukuro_west_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[4]/div[3]/span')[0].text
    shop_Aikebukuro_west = "相席屋池袋西口店"
    shop_Aikebukuro_west_url = "https://goo.gl/maps/Zf2w9ZqEAvbTq3qR7"
    Aikebukuro_west_total = int(Aikebukuro_west_man) - int(Aikebukuro_west_woman)
    total_rank.append(Aikebukuro_west_total)
    Aikebukuro_west.append(Aikebukuro_west_man)
    Aikebukuro_west.append(Aikebukuro_west_woman)
    Aikebukuro_west.append(shop_Aikebukuro_west)
    Aikebukuro_west.append(shop_Aikebukuro_west_url)
    Aikebukuro_west.append(Aikebukuro_west_total)

    
    Aebisu_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[5]/div[2]/span')[0].text
    Aebisu_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[5]/div[3]/span')[0].text
    shop_Aebisu = "相席屋恵比寿店"
    shop_Aebisu_url = "https://goo.gl/maps/yymhRVSxGoBXQowE6"
    Aebisu_total = int(Aebisu_man) - int(Aebisu_woman)
    total_rank.append(Aebisu_total)
    Aebisu.append(Aebisu_man)
    Aebisu.append(Aebisu_woman)
    Aebisu.append(shop_Aebisu)
    Aebisu.append(shop_Aebisu_url)
    Aebisu.append(Aebisu_total)

    
    Aueno_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[6]/div[2]/span')[0].text
    Aueno_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[6]/div[3]/span')[0].text
    shop_Aueno = "相席屋上野店"
    shop_Aueno_url = "https://goo.gl/maps/Wj73XkeCaVZk7DMB9"
    Aueno_total = int(Aueno_man) - int(Aueno_woman)
    total_rank.append(Aueno_total)
    Aueno.append(Aueno_man)
    Aueno.append(Aueno_woman)
    Aueno.append(shop_Aueno)
    Aueno.append(shop_Aueno_url)
    Aueno.append(Aueno_total)

    
    Ashibuya_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[7]/div[2]/span')[0].text
    Ashibuya_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[7]/div[3]/span')[0].text
    shop_Ashibuya = "相席屋渋谷店"
    shop_Ashibuya_url = "https://goo.gl/maps/oGAq5EtJVzviju4v7"
    Ashibuya_total = int(Ashibuya_man) - int(Ashibuya_woman)
    total_rank.append(Ashibuya_total)
    Ashibuya.append(Ashibuya_man)
    Ashibuya.append(Ashibuya_woman)
    Ashibuya.append(shop_Ashibuya)
    Ashibuya.append(shop_Ashibuya_url)
    Ashibuya.append(Ashibuya_total)

    
    Akinshicho_man = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[8]/div[2]/span')[0].text
    Akinshicho_woman = html.xpath(
        '//*[@id="js-container"]/main/div[4]/div[8]/div[3]/span')[0].text
    shop_Akinshicho = "相席屋錦糸町店"
    shop_Akinshicho_url = "https://goo.gl/maps/pYmJvA87gsv7yHBC6"
    Akinshicho_total = int(Akinshicho_man) - int(Akinshicho_woman)
    total_rank.append(Akinshicho_total)
    Akinshicho.append(Akinshicho_man)
    Akinshicho.append(Akinshicho_woman)
    Akinshicho.append(shop_Akinshicho)
    Akinshicho.append(shop_Akinshicho_url)
    Akinshicho.append(Akinshicho_total)

    
    yu = requests.get("https://lux-g.com/")
    html = lxml.html.fromstring(yu.content)
    
    try:
        Lshibuya_man = html.xpath(
            '//*[@id="services"]/div/div[2]/div/a/div/div[2]/div[2]/p/strong[1]/text()')[0]
    except:
        Lshibuya_man = 0
    try:
        Lshibuya_woman = html.xpath(
            '//*[@id="services"]/div/div[2]/div/a/div/div[2]/div[2]/p/strong[2]/text()')[0]
    except:
        Lshibuya_woman = 0
    shop_Lshibuya = "渋谷 相席ラウンジミラス"
    shop_Lshibuya_url = "https://goo.gl/maps/75c7tgk9HdGBqN2w7"
    Lshibuya_total = int(Lshibuya_man) - int(Lshibuya_woman)
    total_rank.append(Lshibuya_total)
    Lshibuya.append(Lshibuya_man)
    Lshibuya.append(Lshibuya_woman)
    Lshibuya.append(shop_Lshibuya)
    Lshibuya.append(shop_Lshibuya_url)
    Lshibuya.append(Lshibuya_total)
    
    try:
        Lebisu_man = html.xpath(
            '//*[@id="services"]/div/div[2]/div[2]/a/div/div[2]/div[2]/p/strong[1]/text()')[0]
    except:
        Lebisu_man = 0
    try:
        Lebisu_woman = html.xpath(
            '//*[@id="services"]/div/div[2]/div[2]/a/div/div[2]/div[2]/p/strong[2]/text()')[0]
    except:
        Lebisu_woman = 0
    shop_Lebisu = "恵比寿 相席ラウンジミラス"
    shop_Lebisu_url = "https://goo.gl/maps/kbWu4j3c2qCs2MdT6"
    Lebisu_total = int(Lebisu_man) - int(Lebisu_woman)
    total_rank.append(Lebisu_total)
    Lebisu.append(Lebisu_man)
    Lebisu.append(Lebisu_woman)
    Lebisu.append(shop_Lebisu)
    Lebisu.append(shop_Lebisu_url)
    Lebisu.append(Lebisu_total)


    response = requests.get(
        "https://line.saucer-aiseki.com/shop_info.json?shop_id=1")
    jsonData = response.json()
    vivo_woman = jsonData["data"]["female"]
    vivo_man = jsonData["data"]["male"]
    shop_vivo = "BLIND DATE LOUNGE VIVO"
    shop_vivo_url = "https://goo.gl/maps/NP4FoUb5oUGg4esz6"
    vivo_total = int(vivo_man) - int(vivo_woman)
    total_rank.append(vivo_total)
    vivo.append(vivo_man)
    vivo.append(vivo_woman)
    vivo.append(shop_vivo)
    vivo.append(shop_vivo_url)
    vivo.append(vivo_total)


def ranking():
    # -*- coding: utf-8 -*-
    rank = sorted(total_rank)
    
    for number in range(0,len(rank)):
        if rank[int(number)] == Osinjuku[4]:
            if len(Osinjuku) == 5:
                Osinjuku.append(number+1)
            else:
                pass
        elif rank[int(number)] == Osibuya[4]:
            if len(Osibuya) == 5:
                Osibuya.append(number+1)
            else:
                pass
        elif rank[int(number)] == Osibuya_ekimae[4]:
            if len(Osibuya_ekimae) == 5:
                Osibuya_ekimae.append(number+1)
            else:
                pass
        elif rank[int(number)] == Omachida[4]:
            if len(Omachida) == 5:
                Omachida.append(number+1)
            else:
                pass
        elif rank[int(number)] == Akabukicho[4]:
            if len(Akabukicho) == 5:
                Akabukicho.append(number+1)
            else:
                pass
        elif rank[int(number)] == Asinnjuku_east[4]:
            if len(Asinnjuku_east) == 5:
                Asinnjuku_east.append(number+1)
            else:
                pass
        elif rank[int(number)] == Aikebukuro_east[4]:
            if len(Aikebukuro_east) == 5:
                Aikebukuro_east.append(number+1)
            else:
                pass
        elif rank[int(number)] == Aikebukuro_west[4]:
            if len(Aikebukuro_west) == 5:
                Aikebukuro_west.append(number+1)
            else:
                pass
        elif rank[int(number)] == Aebisu[4]:
            if len(Aebisu) == 5:
                Aebisu.append(number+1)
            else:
                pass
        elif rank[int(number)] == Aueno[4]:
            if len(Aueno) == 5:
                Aueno.append(number+1)
            else:
                pass
        elif rank[int(number)] == Ashibuya[4]:
            if len(Ashibuya) == 5:
                Ashibuya.append(number+1)
            else:
                pass
        elif rank[int(number)] == Akinshicho[4]:
            if len(Akinshicho) == 5:
                Akinshicho.append(number+1)
            else:
                pass
        elif rank[int(number)] == Lshibuya[4]:
            if len(Lshibuya) == 5:
                Lshibuya.append(number+1)
            else:
                pass
        elif rank[int(number)] == Lebisu[4]:
            if len(Lebisu) == 5:
                Lebisu.append(number+1)
            else:
                pass
        elif rank[int(number)] == vivo[4]:
            if len(vivo) == 5:
                vivo.append(number+1)
            else:
                pass


records = []
def tuika():
    # -*- coding: utf-8 -*-
    for numnum in range(1,16,1):
        if numnum == Osinjuku[5]:
            records.append(Osinjuku)
        else:
            pass
        if numnum == Osibuya[5]:
            records.append(Osibuya)
        else:
            pass
        if numnum == Osibuya_ekimae[5]:
            records.append(Osibuya_ekimae)
        else:
            pass
        if numnum == Omachida[5]:
            records.append(Omachida)
        else:
            pass
        if numnum == Akabukicho[5]:
            records.append(Akabukicho)
        else:
            pass
        if numnum == Asinnjuku_east[5]:
            records.append(Asinnjuku_east)
        else:
            pass
        if numnum == Aikebukuro_east[5]:
            records.append(Aikebukuro_east)
        else:
            pass
        if numnum == Aikebukuro_west[5]:
            records.append(Aikebukuro_west)
        else:
            pass
        if numnum == Aebisu[5]:
            records.append(Aebisu)
        else:
            pass
        if numnum == Aueno[5]:
            records.append(Aueno)
        else:
            pass
        if numnum == Ashibuya[5]:
            records.append(Ashibuya)
        else:
            pass
        if numnum == Akinshicho[5]:
            records.append(Akinshicho)
        else:
            pass
        if numnum == Lshibuya[5]:
            records.append(Lshibuya)
        else:
            pass
        if numnum == Lebisu[5]:
            records.append(Lebisu)
        else:
            pass
        if numnum == vivo[5]:
            records.append(vivo)
        else:
            pass
        with open('results.csv', 'w' , newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(records)


def tuika2():
    # -*- coding: utf-8 -*-
        records.append(Osinjuku)
        records.append(Osibuya)
        records.append(Osibuya_ekimae)
        records.append(Omachida)
        records.append(Akabukicho)
        records.append(Asinnjuku_east)
        records.append(Aikebukuro_east)
        records.append(Aikebukuro_west)
        records.append(Aebisu)
        records.append(Aueno)
        records.append(Ashibuya)
        records.append(Akinshicho)
        records.append(Lshibuya)
        records.append(Lebisu)
        records.append(vivo)
        with open('results.csv', 'w' , newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(records)




test()
tuika2()





