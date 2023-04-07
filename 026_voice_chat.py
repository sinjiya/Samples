# pip install SpeechRecognition
# pip uninstall pyaudio
# pip install pipwin   ### for Windows environment
# pipwin install pyaudio

import speech_recognition as sr
import pyttsx3
import pyaudio
import winsound

import Ask  # self-defined function in Ask.py

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for voice in voices:
#      print(voice)
engine.setProperty('voice', voices[-1].id)
engine.setProperty('rate', 220)    # Speed percent (can go over 100)
engine.setProperty('volume', 1.0)  # Volume

recognizer = sr.Recognizer()
TERMINATIONS =["stop","停","停止","再見","再见","拜拜","不聊了"]
mic_List = sr.Microphone.list_microphone_names()
# for i, mic in enumerate(mic_List):
#     print(i, mic)
mic =  sr.Microphone(device_index=1)



waiting = True
print('Waiting command: ', waiting)

def take_command():
    try:
        with mic as audioSource:
            recognizer.adjust_for_ambient_noise(mic, 0.5)
            winsound.Beep(400, 200)
            print('Chat GPT is Listening ...')
            voice = recognizer.listen(audioSource)
            text = recognizer.recognize_google(voice, language="zh")
            # print(text)
            return text

    #         # pywhatkit.playonyt(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "對不起！我沒聽到你説了什麼。我們還聊嗎！"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; %s" % e)
    except Exception as e:
        print(e)
        return None

while waiting:
    cmd = take_command()
    
    if cmd in TERMINATIONS:
        waiting = False
        engine.say('好的！下次再聊')
        engine.runAndWait()
        print('Wait ended.  Status = ', waiting)
    else:
        print(cmd)
        chat_response = Ask.ChatGpt(cmd)
        engine.say(chat_response)
        engine.runAndWait()
        print(chat_response)
