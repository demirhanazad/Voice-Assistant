# BİSMİLLAHİRRAHMANİRRAHİM Fİ EVVELİHİ VEL AHİRİ

import pyttsx3
import webbrowser
import speech_recognition as sr
from datetime import *
import random
from random import choice
import time
import deneme.aramayap as aramayap
from deneme.aramayap import dinle
#from kur import doviz_com_verial
from selenium import webdriver
#import instagram


#**********************************************************************************************#
#                                                                                              #
#             alt satırda ses motorunun çalışma özelliklerini belirttim                        #
#                                                                                              #
#**********************************************************************************************#
motor = pyttsx3.init()                                                                         #
hacim = motor.getProperty('volume') #geçerli ses seviyesini öğrenme (min=0 ve maks=1)          #
motor.setProperty('volume',1.0)# ses seviyesini 0 ile 1 arasında ayarlama                      #
oran = motor.getProperty('rate')# mevcut konuşma hızının ayrıntılarını alma                    #
motor.setProperty('rate',130)# yeni ses hızı ayarlama                                          #
sesler = motor.getProperty('voices')#geçerli sesin ayrıntılarını alma                          #
motor.setProperty('voice', sesler[0].id)#burada sesin türünü belirliyoruz                      #
#**********************************************************************************************#
def komutlarım():
    with open("komutlar.txt", "r",encoding='utf8') as dosya:
        for satir in dosya:
            txt = satir.split("\n")
            for i in range(len(txt)):
                print (txt[i])
        time.sleep(3)

def konuş(audio):
    motor.say(audio)
    motor.runAndWait()
motor.say("SELAMUN ALEYKUM")
motor.runAndWait()
print ("bana söyleyebileceğin bazı komutlar:")
komutlarım()
    
def komut():
     
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

while True:
         
        voice = komut().lower()
        voice=str(voice)
        voice=voice.lower()
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
        if "instagram'ı aç" in voice or "open instagram" in voice:
            konuş("do you want to openning your instagram account??\n")
            print("instagramı açmak mı istiyorsun?")
            yanıt=komut().lower()
            if "evet" in yanıt or "yes" in yanıt:
                #instagram.çalıştır()
                pass
            else:
                pass
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
        if "saat kaç" in voice or "what time is it" in voice:
            selection =["saat :","time is:","ım looking at the clock at the moment, wait for me to say time is:"]
            saat=datetime.now().strftime("%H:%M")
            selection=random.choice(selection)
            saat=selection+saat
            konuş(saat)
            print(saat)
        elif 'saati söyle' in voice:
            strTime = datetime.now().strftime("%H:%M:%S")   
            konuş(f"okey, the time is {strTime}")
            print(strTime)
        elif "görüşürüz" in voice or "programı kapat" in voice or "sonra görüşürüz" in voice:
            selection =["see you again","see you","see you tomorrow","see you later","good bye","good bye azad"]
            selection=choice(selection)
            konuş(selection)
            exit()
        elif "arama yap" in voice or "benim için arama yapar mısın" in voice:
            konuş("what do you want to search on google")
            time.sleep(1)
            print("google'da ne aramak istiyorsun")
            time.sleep(1)
            ara=komut().lower()
            ara=str(ara)
            ara="{}".format(ara)
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
        elif "kur verilerini getir" in voice or "döviz" in voice or "kur veri" in voice:
            #doviz_com_verial()
            pass

"""motor.say("nasıl yardımcı olabilirim")
motor.runAndWait()
while True:
    dinle=komut()
    print (dinle)
    konus(dinle)"""