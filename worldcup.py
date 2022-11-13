from bs4 import BeautifulSoup
import requests



web_link = "https://en.wikipedia.org/wiki/1930_FIFA_World_Cup"
web = requests.get(web_link)
content = web.content
soup = BeautifulSoup(content , 'lxml')


