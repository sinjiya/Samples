# 1. File Access
# 2. Text to Speech
# 3. Adjust the Pronunciation

import pyttsx3
import pronunciation

# pyttsx3 initialization
engine = pyttsx3.init()
# Get installed Voices


voices = engine.getProperty('voices')
### 請檢查並設定您想要使用的電腦語音
# print("-"*20)
# for voice in voices:
#     print(voice)
#     print("-"*20)
### 以下選用 voices[2] # Microsoft ZH-TW HANHAN

engine.setProperty('voice', voices[2].id) # Microsoft ZH-TW HANHAN
engine.setProperty('rate', 200)  # word speed

file_name = "data/紅樓夢001.txt"

with open(file_name, mode="r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        print(str(i), '\t', line)
        engine.say(pronunciation.adjust(line))
        engine.runAndWait()
        