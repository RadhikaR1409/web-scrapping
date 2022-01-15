from bs4 import BeautifulSoup
import requests
import pprint
# from t1 import x
import json

def scrap_movie_cast(x):
    # y=requests.get(movie_cast_url)
    # soup=BeautifulSoup(y.text,'html.parser')
    # a=soup.find("div",class_="media-body")
    # b=a.find_all('a')
    # # print(b.text)
    # cast_list=[]
    # for j in b:
    #     cast_list.append(j.text)
    #     # print(j.text)
    # # return(cast_list)
    movie_cast={}
    # for i in x:
    #     movie_cast.update({i["title"]:cast_list})


    for i in x:
        y=requests.get(i["url"])
        soup=BeautifulSoup(y.text,'html.parser')
        a=soup.find("div",class_="media-body")
        b=a.find_all('a')
    # print(b.text)
        cast_list=[]
        for j in b:
            cast_list.append(j.text)
        movie_cast.update({i["title"]:cast_list})

    with open("scrap_movie_cast.json", "w") as file:
        json.dump(movie_cast,file,indent=2)

    return movie_cast

# k=[]
# for i in x:
    # k.append(i["url"])
    # for j in k:
with open("scrap_top_list.json", 'r') as file:
    x=json.load(file)
scrap_movie_cast(x)
    # pprint.pprint(l)


# main_dic={}
# for i in x:
    # main_dic.update({i["title"]:rad})





