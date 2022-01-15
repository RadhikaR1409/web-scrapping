from bs4 import BeautifulSoup
import requests
import pprint
from task4 import scrap_movie_details
import os
import json
from t1 import x

# with open("/home/navgurukul/Desktop/web scrapping/scrap_top_list.json","r") as file:
#     fdata=file.read()
#     pdata=json.loads(fdata)
#     for i in pdata[:10]:
#         fname=i["url"][33:]+".json"
#         # print(fname)
#         if os.path.exists(fname)==True:
#             with open(fname,"r") as dfile:
#                 detail=dfile.read()
#                 final=json.loads(detail)
#                 print(final)
#         else:
#             x=requests.get(i["url"][33:])
#             soup=BeautifulSoup(x.text,'html.parser')
#             z=soup.find('ul',class_='content-meta info')
#             a=z.findAll('li',class_="meta-row clearfix")
#             final={}
#             for i in a:
#                 final[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
#             with open(fname,"w") as ffile:
#                 json.dump(final,indent=2)
#             print(final)


# file=os.path.exists("movie_details.json")
# if file==True:
#     with open("movie_details.json","r") as f:
#         fil=json.load(f)
# print(fil)

# x=requests.get('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/')
# soup=BeautifulSoup(x.text,'html.parser')
# main=soup.find("table",class_="table")
# sub=main.findAll("tr")
# final=[]
# for i in sub[1:]:
#     x=i.findAll("td")
#     y=x[2].find("a")["href"]
#     final.append(y)
# # pprint.pprint(final)
# movie_name=[]
# for j in final:
#     movie_name.append(j[3:])
#     # print(movie_name)

# with open("movie_name.json","w") as fs:
#     json.dump(movie_name,fs,indent=2)

# file1=os.path.exists("movie_name.json")
# if file1==True:
#     with open("movie_name.json","r") as fn:
#         fil1=fn.read()
# # print(fil1)

# for i in fil1[:1]:
#     r=i.json
#     k=0
#     for j in fil:
#         with open("r","w") as f:
#             json.dump(j[k],f,indent=2)
#         k+=1


def scrap_new_movie_detail(url2):
    for i in x:
        if i["url"]==url2:
            url=i["url"][33:]
            url1=i["url"]
            name=i["title"]
    filename="/home/navgurukul/Desktop/web scrapping/"+url+".json"

    file=os.path.exists(filename)
    # print(file)
    if file==True:
        print("it exists")
        with open(filename,"r") as m:
            detail=json.load(m)
            print(detail)
    else:
        print("it doesnt exists")
        data=scrap_movie_details(url1)
        print(data)

        with open(filename,"w") as n:
            json.dump(data,n,indent=2)

i=0
while i<=3:
    url2=x[i]["url"]
    scrap_new_movie_detail(url2)
    i+=1









