import openai
import pyttsx3
import sys
import time
import speech_recognition as sr
import threading
import tkinter as tk
from file import *
from PIL import Image, ImageTk


def gui():
    root = tk.Tk()
    root.title("Bruce - powered by Chat GPT")
    canvas = tk.Canvas(root, width=500, height=100)
    canvas.grid(columnspan=3, rowspan=3)

    logo = Image.open('images/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    button_img = Image.open('images/button.png')
    button_img = ImageTk.PhotoImage(button_img)

    instr_text = tk.Label(root, text="Press the microphone to activate Bruce")
    instr_text.grid(columnspan=3, column=0, row=1)

    button_text = tk.StringVar()
    button = tk.Button(root, textvariable=button_text,
                       image=button_img, command=lambda: threading.Thread(target=assistant(), args=()))
    root.update()

    button.grid(column=1, row=2)

    canvas = tk.Canvas(root, width=500, height=100)
    canvas.grid(columnspan=3)
    root.update()
    root.mainloop()


# thread_y = threading.Thread(target=gui, args=())
# thread_y.start()
gui()
