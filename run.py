# BİSMİLLAHİRRAHMANİRRAHİM Fİ EVVELİHİ VEL AHİRİ



from komut import *
import webbrowser
import speech_recognition as sr
from bs4 import BeautifulSoup
from datetime import *
import random
from random import choice
import time
import deneme.aramayap as aramayap
from deneme.aramayap import dinle
from kur import doviz_com_verial
from democanbrowser import *



while True:
         
        voice = komut().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if "sosyal" in voice or "sosyal medya ara" in voice:
            konuş("What social media are you searching for on Google??\n")
            print("Google'da hangi sosyal medyayı arıyorsunuz?")
            time.sleep(1)
            ara=komut().lower()
            webbrowser.open("https://{}.com".format(ara))
        elif 'tarih' in voice or "bugün günlerden ne" in voice:
            bugün=time.strftime("%A")
            konuş (bugün)
            if bugün =="Monday":
                print("Pazartesi")
            elif bugün =="Tuesday":
                print("Salı")
            elif bugün =="Wednesday":
                print("Çarşamba")
            elif bugün =="Thursday":
                print("Perşembe")
            elif bugün =="Friday":
                print("Cuma")
            elif bugün =="Saturday":
                print("Cumartesi")
            elif bugün =="Sunday":
                print("Pazar")
        elif "saat kaç" in voice or "what time is it" in voice:
            selection =["saat :","time is:","ım looking at the clock at the moment, wait for me to say time is:"]
            saat=datetime.now().strftime("%H:%M")
            selection=random.choice(selection)
            konuş(selection+saat)
        elif 'saati söyle' in voice:
            strTime = datetime.now().strftime("%H:%M:%S")   
            konuş(f"okey, the time is {strTime}")
            print(strTime)
        elif "görüşürüz" in voice or "programı kapat" in voice or "sonra görüşürüz" in voice:
            selection =["see you again","see you","see you tomorrow","see you later","good bye","good bye azad"]
            selection=random.choice(selection)
            konuş(selection)
            exit()
        elif "arama yap" in voice or "benim için arama yapar mısın" in voice:
            konuş("what do you want to search on google")
            time.sleep(1)
            print("google'da ne aramak istiyorsun")
            time.sleep(1)
            ara=komut().lower()
            ara=str(ara)
            url="https://google.com/search?q"+ara
            time.sleep(1)
            webbrowser.get().open(url)
            konuş(ara+"ile ilgili google de bulduklarım")
        elif "dosyayı aç"in voice:
            konuş("which file do you want to open")
            time.sleep(1)
            print("Hangi doyayı açmak istiyorsun")
            time.sleep(1)
            dosyaismi=komut().lower()
            file=open("{}.txt".format(dosyaismi), "r")
            for yazı in file:
                motor.say(yazı)
                motor.setProperty("rate",120)
                motor.setProperty("volume",0.9)
                motor.runAndWait()
            file.close()
        elif "kur verilerini getir" in voice or "döviz" in voice:
            doviz_com_verial()
        elif "motora git" in voice :
            arama()