import os

import speech_recognition as sr

os.chdir(os.path.abspath(os.path.dirname(__file__)))

AUDIO_FILE = 'voice2.wav' #これを変更してください

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

print('音声データの文字起こし結果：\n\n',r.recognize_google(audio,language='ja'))