import pyaudio
import wave
import speech_recognition as sr


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()


def initSpeech():
    print("Listening...")
    play_audio("./audio/audio_start.wav")  # Here the audio is played that we have supplied in our terminal

    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)  # Here recognizer r listens to whatever we say in source

    play_audio("./audio/audio_end.wav")
    command = ""

    try:
        command = r.recognize_google(audio)  # Here recognizer sends our listened sound to google for recognition
    except:
        print("Sorry bro,couldn't recognize. ")

    print("Your Command")
    print(command)  # Here it prints whatever we had said in the microphone


initSpeech()
