import requests
from bs4 import BeautifulSoup

def doviz_com_verial():
    
    url="https://www.doviz.com/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    doviz=soup.find("div",attrs={"class":"article-content"}).select("div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > table > tbody > tr:nth-of-type(1)>td ")
    doviz2=soup.find("div",attrs={"class":"header-secondary"}).select("div:nth-of-type(1) > div:nth-of-type(1) > div")
    for i in range(1,6):
        doviz3=doviz[i].find("a")
        doviz4=doviz3.find("span",attrs={'class':"value"}).text
        doviz5=doviz3.find("span",attrs={'class':"name"}).text
        print(doviz5 +" : "+ doviz4 +"₺ ")
doviz_com_verial()