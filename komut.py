



# BİSMİLLAHİRRAHMANİRRAHİM Fİ EVVELİHİ VEL AHİRİ

import pyttsx3
import speech_recognition as sr
import time


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
        time.sleep(7)
        
motor.say("SELAMUN ALEYKUM")
motor.runAndWait()
print ("bana söyleyebileceğin bazı komutlar:")
komutlarım()

def konuş(audio):
    motor.say(audio)
    motor.runAndWait()
    
def komut(ask=False):
     
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