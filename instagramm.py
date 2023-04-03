from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import kullanicibilgileri as  kullanıcı
import pandas as pd
import pyttsx3 as pt
import speech_recognition as sr
motor = pt.init() 
ara=[]
index=[]
def konuş(audio):
    motor.say(audio)
    motor.runAndWait()
def kullanıcıyıselamla():
    konuş("Selamun Aleykum {}".format(kullanıcı.username))
class Browser:
    def komut(self):
         
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            konuş("I m listening you")
            print("Dinliyorum...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("İşleniyor...")   
            voice = r.recognize_google(audio, language ='tr-TR')
            print(f"Söylenen cümle: {voice}\n")
    
        except Exception as e:
            print(e)   
            print("Sesini algılayamadım.") 
            return "None"
        
        return voice
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goInstagram(self)
    def goInstagram(self):
        self.browser.get(self.link) 
        sleep(9)
        Browser.login(self)
        Browser.followers(self)
        Browser.kapat(self)
        Browser.biyografi(self)
        Browser.arama(self)
    def followers(self):
        sleep(9)
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
        sleep(9)
        Browser.bar(self)
        takipçiler=self.browser.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade")
        """sayaç=0
        for takipçi in takipçiler:
            sayaç+=1
            print(str(sayaç)+"="+takipçi.text)
        sleep(5)"""
        for takip in takipçiler:
            takip=takip.text
            takip=str(takip)
            ara.append(takip)
    def biyografi(self):
        for i in range(1,len(ara)+1):
            index.append(i)
        veri=pd.read_csv("veriler.csv",delimiter=",")
        veri["numara"]=index
        veri=veri.set_index("numara")
        veri["kullanıcıadı"]=ara
        veri.to_csv("veriler.csv",sep=",")
        print(veri)
        konuş("I think you have {} followers because ı found just these".format(len(ara)))
        print("I think you have {} followers because ı found just these".format(len(ara)))
        self.browser.get(self.link+"/"+kullanıcı.username+"/")
    def kapat(self):
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div").click()
        sleep(10)
    def arama(self):
        konuş("do you want to see your folllowers accounts")
        print("takipçilerinin hesaplarını merak ediyor musun?")
        yanıt=Browser.komut(self).lower()
        if "evet"in yanıt:
            
            for i in range(len(ara)):
                sleep(1)
                self.browser.get(self.link+"/"+ara[i]+"/")
                sleep(3)
        else :
            pass
    def bar(self):
        js_komut="""
        sayfa=document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfasonu=sayfa.scrollHeight;
        return sayfasonu;
        """
        sayfasonu= self.browser.execute_script(js_komut)
        while 1:
            son=sayfasonu
            sleep(3)
            sayfasonu= self.browser.execute_script(js_komut)
            if son==sayfasonu:
                break
    def login(self):
        kullanıcı_adı=self.browser.find_element(By.NAME,"username")
        pasaport=self.browser.find_element(By.NAME,"password")
        
        kullanıcı_adı.send_keys(kullanıcı.username)
        pasaport.send_keys(kullanıcı.password)
        sleep(3)
        loginbtn=self.browser.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(3) > button > div")
        loginbtn.click()
        sleep(13)
        self.browser.get(self.link+"/"+kullanıcı.username+"/")
        sleep(3)