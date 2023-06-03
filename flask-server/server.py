from flask import Flask, request
from flask_cors import CORS
from file import VirtualAssistant
import openai
import pyttsx3
import sys
import time
import speech_recognition as sr
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Bruce Chat assistant - powered by Chat GPT"

@app.route('/record', methods=['POST'])
def recording():
    if request.method == 'POST':
        data = request.get_json()
        
    return 0


if __name__ == '__main__':
    app.run(debug=True)
