from bs4 import BeautifulSoup
import requests



web_link = "https://en.wikipedia.org/wiki/1930_FIFA_World_Cup"
web = requests.get(web_link)
content = web.content
soup = BeautifulSoup(content , 'lxml')


matches= soup.find_all("div", class_="footballbox")

home =[]
score =[]
away =[]

for match in matches:
    home = home.append(match.find("th",class_="fhome").get_text())
    score = score.append(match.find("th",class_="fscore").get_text())
    away = away.append(match.find("th",class_="faway").get_text())