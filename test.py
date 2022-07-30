import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozila/5.0 (Winodws NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
URL = 'https://www.melon.com/chart/index.htm' 
response = requests.get(URL,headers=header) # 홈페이지에서 html 가져오기

html = response.text

soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다

title = soup.find_all("div",{"class":"ellipsis rank01"}) #노래 제목
singer = soup.find_all("div",{"class":"ellipsis rank02"}) #가수

title_list = []
singer_list = []

for i in title:
    title_list.append(i.find('a').text)

for j in singer:
    singer_list.append(j.find('a').text)

rank = 50
for r in range(rank):
    print("%2d위 : %s - %s"%(r+1, title_list[r], singer_list[r]))