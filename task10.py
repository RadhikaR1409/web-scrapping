from bs4 import BeautifulSoup
import requests
import pprint
import pprint
import json


def analys_language_and_directors(r6):
    dic={}
    for i in r6:
        for j in r6:
            lan={}
            if i["Director:"]==j["Director:"]:
                c=0
                c1=0
                if i["Original Language:"]==j["Original Language:"]:
                    c+=1
                    lan.update({i["Original Language:"]:c})
                else:
                    c1+=1
                    lan.update({i["Original Language:"]:c1})
                dic[i["Director:"]]=lan
    return dic
# for i in r6[:1]:
with open("movie_details.json", 'r') as file:
    r6=json.load(file)
pprint.pprint(analys_language_and_directors(r6))
r10=analys_language_and_directors(r6)

with open("director_language_num.json","w") as fn:
    json.dump(r10,fn,indent=2)

