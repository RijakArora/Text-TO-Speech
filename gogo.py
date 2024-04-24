import speech_recognition as sr
import playsound
import os
import json
import pyttsx3

from gtts import gTTS
from openai import OpenAI


male = True

def speakMS(X):
	global male
	maleVoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVIV_11.0"
	try:
		print("Speaking...")
		audio = pyttsx3.init()
		audio.setProperty('rate', 130)
		audio.setProperty('volume', 5)
		audio.setProperty('voice', maleVoice )
		audio.say(X)
		audio.runAndWait()
	except Exception:
		print("Error playing audio:")
		

def speak(X):
	print(X)
	speakMS(X)
	
if __name__ == "__main__":
    X = input("Enter the text to be converted into audio : ")
    speak(X)


