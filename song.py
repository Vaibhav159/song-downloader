import requests
import vlc
from bs4 import BeautifulSoup as soup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

x=input("enter the song you want to search : ")
x=x.replace(" ","+")

with requests.Session() as s:
    url="https://www.google.com/search?source=hp&ei=EZeGXIf6DNmy9QO2sIXQCQ&q="+x
    r=s.get(url,headers=headers)
    soup1=soup(r.content,"html.parser")
    j=soup1.body.find_all("cite",{"class":"iUh30"})
    y=j[0].text
    song=y[29:]
    download="https://www.easy-youtube-mp3.com/download.php"
    new_link=download+song

with requests.Session() as s:
    m=s.get(new_link,headers=headers)
    soup2=soup(m.content,"html.parser")
    gg=soup2.body.find_all("a",{"class":"btn btn-lg btn-success"})
    download_song=gg[0]["href"]
    down=requests.get(str(download_song))
    print("downloading pls wait")

y=x.replace("+"," ")+".mp3"
with open(y, 'wb') as f:
    f.write(down.content)
    print("Done downloading!")

