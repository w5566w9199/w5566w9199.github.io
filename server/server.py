from flask import Flask, request, render_template
import speech_recognition as sr

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form["name"]
        return name + " Hello"
    return render_template("index.html")

@app.route("/a", methods=['GET', 'POST'])
def a():
    r = sr.Recognizer()
    with sr.AudioFile("templates/tt.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
    try:
        return "Transcription: " + r.recognize_google(audio,language="zh-TW")   # recognize speech using Google Speech Recognition
    except LookupError:                                 # speech is unintelligible
        return "Could not understand audio"
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
