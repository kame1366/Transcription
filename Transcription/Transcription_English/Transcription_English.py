import os

import speech_recognition as sr

os.chdir(os.path.abspath(os.path.dirname(__file__)))

AUDIO_FILE = 'voice3.wav'

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

print('Transcription results of audio data:\n\n',r.recognize_google(audio,language='en'))