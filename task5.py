from bs4 import BeautifulSoup
import requests
import pprint
from t1 import x
import json

def scrap_movie_details(movie_url):
    x=requests.get(movie_url)
    soup=BeautifulSoup(x.text,'html.parser')
    z=soup.find('ul',class_='content-meta info')
    a=z.findAll('li',class_="meta-row clearfix")
    # print(a)

    final={}
    list=[]
    for i in a:
        # s=" ".join((i.find("div",class_="meta-label subtle").text).split())
        # b=" ".join((i.find("div",class_="meta-value").text).split())
        final[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
        
    return final



# pprint.pprint(scrap_movie_details("https://www.rottentomatoes.com/m/1046129-fugitive"))

def scrap_movie_list_details():
    k=[]
    for i in x:
        k.append(scrap_movie_details(i["url"]))
    return k
# pprint.pprint(scrap_movie_list_details())
r6=scrap_movie_list_details()
        # pprint.pprint(k)

with open("movie_details.json","w") as f:
    json.dump(r6,f,indent=2)









