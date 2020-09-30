import requests
import speech_recognition as sr
from gtts import gTTS
import subprocess
from pygame import mixer
mixer.init()
bot_message = ""
message = ""
while bot_message != "再見" or bot_message != "結束":

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything~~")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio, language="zh-TW")
            message.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
            print("Your said :{}".format(message))
        except:
            print("無法辨識")

    if len(message) == 0:
        continue
    print("Wait...")

    with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")

    r = requests.post('https://cors-anywhere.herokuapp.com/https://adf3adc12797.ngrok.io/webhooks/rest/webhook', json={"message": message})

    print("Output： ",end='')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message, lang="zh-TW")
    myobj.save("speak.mp3")
    mixer.music.load("speak.mp3")
    mixer.music.play()
