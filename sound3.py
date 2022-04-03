import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound 
from datetime import datetime
import os
r = sr.Recognizer()
with  sr.Microphone() as source:
    # playsound("test.wav")
    os.system("test.wav")
    audio = r.record(source, duration=5)
    # playsound("test.wav")
    os.system("test.wav")
    try:
      text = r.recognize_google(audio, language="th")
    except:
      text = "ขอโทษค่ะ"
tts = gTTS(text, lang="th")
tts.save("oak.mp3")
os.system("start oak.mp3")
    # playsound("oak.mp3", True)