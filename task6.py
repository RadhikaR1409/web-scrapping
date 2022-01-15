from bs4 import BeautifulSoup
import requests
import pprint
from task5 import r6

def analysis_movie_language():
    ce=0
    ch=0
    che=0
    for i in r6:
        if i['Original Language:']== 'English':
            ce+=1
        elif i['Original Language:']== 'Hindi':
            ch+=1
        else:
            che+=1
    print("English movie",ce,"\n","hindi movie",ch,"\n","both language",che)
analysis_movie_language()




