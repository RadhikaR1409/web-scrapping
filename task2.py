from bs4 import BeautifulSoup
import requests
import pprint
from t1 import x

# def scrap_top_list():
#     x=requests.get('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/')
#     soup=BeautifulSoup(x.text,'html.parser')
#     main=soup.find("table",class_="table")
#     sub=main.findAll("tr")
#     final=[]
#     for i in sub[1:]:
#         dic={}
#         x=i.findAll("td")
#         dic["position"]=" ".join((x[0].text).split())
#         dic["rating"]=" ".join((x[1].text).split())
#         dic["title"]=" ".join((x[2].text).split())
#         dic["No. of reviews"]=" ".join((x[3].text).split())
#         final.append(dic)

#     # pprint.pprint(final)
#     year=[]
#     for j in final:
#         year.append(j["title"][-5:-1])

#     year_vise={}
#     for i in final:
#         same_movie=[]
#         for j in year:
#             if i["title"][-5:-1]==j:
#                 same_movie.append(i)
#                 year_vise[j]=same_movie
#     return year_vise
# pprint.pprint(scrap_top_list())

# x=scrap_top_list

def scrap_year_wise(movie):
    year=[]
    for j in movie:
        year.append(j["title"][-5:-1])

    year_vise={}
    for i in movie:
        same_movie=[]
        for j in year:
            if i["title"][-5:-1]==j:
                same_movie.append(i)
                year_vise[int(j)]=same_movie
    return year_vise

y=scrap_year_wise(x)
# pprint.pprint(scrap_year_wise(x))