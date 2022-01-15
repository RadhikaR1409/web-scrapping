from bs4 import BeautifulSoup
import requests
import pprint
from task5 import r6

def scrap_movie_director():
    lis=[]
    for j in r6:
        lis.append(j["Director:"])
    lis1={}
    for k in lis:
        c=0
        for r in lis:
            if k==r:
                c+=1
                lis1[r]=c

    return lis1
print(scrap_movie_director())
