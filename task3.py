from bs4 import BeautifulSoup
import requests
import pprint
from task2 import y


# y=scrap_year_wise()
year=[]
def group_by_decade():
    for i,j in y.items():
        year.append(i)
    # return year
    year.sort()
    j=0
    dic={}
    decade_list=[]
    while j<len(year):
        year_1=(year[j]//10)*10
        if year_1 not in decade_list:
            decade_list.append(year_1)
        j+=1
    
    for i in decade_list:
        range=i+9
        final=[]
        for k,v in y.items():
            r=0
            while r<len(v):
                if k>=i and k<=range:
                    final.append(v[r])
                r+=1
        dic[i]=final
    return dic
    # return decade_list
pprint.pprint(group_by_decade())

    # pprint.pprint(year_vise)




