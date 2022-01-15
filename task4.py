import json
from bs4 import BeautifulSoup
import requests
import pprint
# from task2 import y

def scrap_movie_details(movie_url):
    x=requests.get(movie_url)
    soup=BeautifulSoup(x.text,'html.parser')
    # main=soup.find("section",class_="panel panel-rt panel-box movie_info media", data_qa_="movie-info-section")
    # # b=main.find("data-qa")
    # y=main.find('div',class_='panel-body content_body')
    z=soup.find('ul',class_='content-meta info')
    a=z.findAll('li',class_="meta-row clearfix")
    # print(a)
    final={}
    # k=1
    for i in a:
        # final["rating"]=i.text[k]
        final[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
    return final
 
s=scrap_movie_details("https://www.rottentomatoes.com/m/1046129-fugitive")

with open("one_movie.json","w") as f:
    json.dump(s,f,indent=2)
