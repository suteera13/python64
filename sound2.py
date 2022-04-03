import speech_recognition as sr 
from gtts import gTTS
import os
tts = gTTS('ถึงม้วยดินสิ้นฟ้ามหาสมุทร ไม่สิ้นสุดความรัก สมัครสมาน  ', lang='th',slow=False)
tts.save('oak.mp3')
os.system("start oak.mp3")