from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import time

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def get_audio():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
    said = ""

    try:
      said = r.recognize_google(audio)
      print(said)
    except Exception as e:
      print('Exception: ' + str(e))
  return said
  
speak("hello boss! what can i help you with?")
get_audio()
