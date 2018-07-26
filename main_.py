import urllib.request
import requests
from bs4 import BeautifulSoup as bs

global i
global name
i = 0
image_adress = int(input())

def Download(url):
    title =str(name)
    n = str(i)
    fullName = title +"-"+ n +".jpg"
    urllib.request.urlretrieve(url,fullName)

respone = requests.get("https://hitomi.la/galleries/%d.html"%image_adress)
html = respone.text
soup = bs(html, 'html.parser')

title = soup.select('body > div > div.content > div.gallery.manga-gallery > h1 > a')

name = str(title[0].text)
print(name)
lengh = name.find('|')+1
name= name[lengh:]

while True:
    i=i+1
    link="https://aa.hitomi.la/galleries/%d/%d.jpg"%(image_adress,i)
    Download(link)


