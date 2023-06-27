# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, ttk

def show_text_to_morse():
    pass

def show_morse_code_to_text():
    pass

#Create the main window

window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x400")
style = Style(theme="flatly")

#Create home screen

home_frame = ttk.Frame(window, padding="20")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Select Translation Type: ",
                       font=("tk.DefaultFont", 20))

home_label.pack(pady=10)

#Text-> Morse Code Button

text_to_morse_btn = ttk.Button(home_frame, text="Text to Morse Code",
                               command=show_text_to_morse)

text_to_morse_btn.pack(pady=5)

# Morse Code -> text button

morse_to_text_btn = ttk.Button(home_frame, text="Morse Code to Text",
                               command=show_morse_code_to_text)

morse_to_text_btn.pack(pady=5)

# Create translation screen

translation_frame = ttk.Frame(window, padding="20")

# Create label for input text
translation_label = ttk.Label(translation_frame, text="Input Text: ",
                              font=('tk.DefaultFont', 20))
translation_label.pack(pady=10)
input_text = tk.Text(translation_frame, height=5)
input_text.pack()

# Create label for output text