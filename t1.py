from bs4 import BeautifulSoup
import requests
import pprint
import json
from random import randint
from time import sleep

def scrap_top_list():
    x=requests.get('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/')
    sleep(randint(1,3))
    soup=BeautifulSoup(x.text,'html.parser')
    main=soup.find("table",class_="table")
    sub=main.findAll("tr")
    final=[]
    for i in sub[1:]:
        dic={}
        x=i.findAll("td")
        dic["position"]=" ".join((x[0].text).split())
        dic["rating"]=" ".join((x[1].text).split())
        dic["title"]=" ".join((x[2].text).split())
        dic["No. of reviews"]=" ".join((x[3].text).split())
        y=x[2].find("a")["href"]
        dic["url"]='https://www.rottentomatoes.com'+y
        final.append(dic)
    return final

x=scrap_top_list()

with open("scrap_top_list.json","w") as f:
    json.dump(x,f,indent=2)


# pprint.pprint(scrap_top_list())
