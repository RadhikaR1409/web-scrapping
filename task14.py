import json
import os
import json
import pprint


with open("movie_details.json",'r') as file:
    movie_detail=json.load(file)

with open("scrap_movie_cast.json",'r') as file1:
    cast_detail=json.load(file1)

movie_detail_with_cast=[]

j=0
for i in cast_detail:
    c=[]
    c.append(cast_detail[i][0])
    c.append(cast_detail[i][1])
    lis={}
    lis.update({i:c})
    movie_detail[j]["cast"]=lis
    j+=1
with open("task14.json", 'w') as file:
    json.dump(movie_detail, file, indent=2)
# pprint.pprint(movie_detail)

# for j in movie_detail.keys():


