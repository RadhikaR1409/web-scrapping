from bs4 import BeautifulSoup
import requests
import pprint
from task5 import r6
import pprint
import json
import os


# file=os.path.exists("movie_details.json")
# if file==True:
    
# print(fil)



# with open("movie_details.json","r") as f:
    # rdata=f.read()
# print(rdata)

list1=[]
def anlisis_movie_genre(fil):
    # list1=[]
    for i in fil:
        z=i["Genre:"].split(",")
        list1.append(z)
    list2={}
    for i in list1:
        c=0
        for j in i:
            for k in i:
                if j==k:
                    c+=1
            list2.update({j:c})
    # return list2
    list3={}
    for i in list2.keys():
        if i not in list3:
            list3.update({i:list2[i]})
    return list3


with open("movie_details.json",'r') as f:
        fil=json.load(f)
pprint.pprint(anlisis_movie_genre(fil))
r11=anlisis_movie_genre(fil)
with open("genre.json","w") as fs:
    json.dump(r11,fs,indent=2)

        

