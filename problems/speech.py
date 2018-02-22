
import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except:
	pass
