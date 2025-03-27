from tkinter import *
THEME_COLOR = "#375362"
from morsecode import Morse_code

class MorseCodeUi():
    def __init__(self):

        self.window = Tk()
        self.window.title("Morse code")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.morse_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR,font=("Ariel", 20))
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)
        self.text_entry_label = Label(text="Convert into Morse:")
        self.text_entry_label.grid(row=1, column=0)
        self.text_entry = Entry(width=21)
        self.text_entry.grid(row=1, column=1)
        self.Morse_entry_label = Label(text="Convert Morse into English:")
        self.Morse_entry_label.grid(row=2, column=0)
        self.morse_entry = Entry(width=21)
        self.morse_entry.grid(row=2, column=1)
        self.Morse_btn = Button(text="Get English", width=13, command=self.decode_morse)
        self.Morse_btn.grid(row=2, column=2)
        self.translate_btn = Button(text="Get morse", width=13, command=self.find_morse)
        self.translate_btn.grid(row=1, column=2)
        self.window.mainloop()

    def find_morse(self):
        value_text = self.text_entry.get()
        morse = Morse_code()
        translated_value = morse.text_to_Morse(value_text)
        self.canvas.itemconfig(self.morse_text, text=f" {translated_value}")

    def decode_morse(self):
        morse_text = self.morse_entry.get()
        morse = Morse_code()
        translated_value = morse.Morse_to_text(morse_text)
        self.canvas.itemconfig(self.morse_text, text=f" {translated_value}")