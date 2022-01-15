from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

# print(soup)
def scrap_top_list():
    main_div=soup.find('div',class_='lister')
    tbody=main_div.find('tbody',class_="lister-list")
    trs=tbody.find_all('tr')
    movie_rank=[]
    movie_name=[]
    year_of_release=[]
    movie_url=[]
    movie_rating=[]

    for tr in trs:
        position=tr.find('td',class_='titlecolumn').get_text().strip()
        rank=''
        for i in position:
            if "." in i:
                rank+=i
            else:
                break
        movie_rank.append(rank)
        title=tr.find('td',class_='titlecolumn').a.get.text()
        movie_name.append(title)
        year=tr.find('td',class_='titlecolumn').span.get_text()
        year_of_release.append(year)
        imdb_rating=tr.find('td',class_='')
    
        






