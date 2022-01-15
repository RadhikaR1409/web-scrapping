import json
import os
import json
import pprint


with open("movie_details.json",'r') as file:
    movie_detail=json.load(file)

with open("scrap_movie_cast.json",'r') as file1:
    cast_detail=json.load(file1)

movie_detail_with_cast=[]

# for i in range(len(movie_detail)):
#     for j in cast_detail.keys():
#         movie_detail[i].update({j:cast_detail[j]})
    # movie_detail_with_cast.append(movie_detail[i])
    # movie_detail_with_cast.append(cast_detail[i])
j=0
for i in cast_detail:
    movie_detail[j][i]=cast_detail[i]
    j+=1
with open("task13.json", 'w') as file:
    json.dump(movie_detail, file, indent=2)
pprint.pprint(movie_detail)