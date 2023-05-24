import openai
import pyttsx3
import sys
import time
import speech_recognition as sr
import threading

openai.api_key = ''
engine = pyttsx3.init()


def audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print("Unknown error")


def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,

    )
    return response["choices"][0]["text"]


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


def assistant():

    while True:
        print("Say 'Bruce' to ask your question...")

        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)

            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "bruce":
                    filename = "question.wav"
                    text_to_speech("Yes...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(
                            source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                    text = audio_to_text(filename)

                    if text == "goodbye bruce":
                        sys.exit()
                    if text == "what's your name":
                        assistant_name = "my name is Bruce Mclaren"
                        text_to_speech(assistant_name)

                    if text:
                        print(f'You said: {text}')

                        response = generate_response(text)
                        print(f'Bruce: {response}')

                        text_to_speech(response)
                if transcription.lower() == "what's your name":
                    name = "my name is Bruce Mclaren"
                    text_to_speech(name)
                if transcription.lower() == "goodbye bruce":
                    sys.exit()

            except Exception as e:
                print()
