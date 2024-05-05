import tkinter as tk
from tkinter import ttk
import pyttsx3

# Function to convert text to speech
def convert_text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    engine = pyttsx3.init()
    selected_voice = voice_combo.get()
    rate = int(rate_scale.get())
    
    engine.setProperty('rate', rate)
    
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
    
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("800x600")

# Style settings
style = ttk.Style()
style.theme_use('clam')  # Using a different theme
style.configure("TButton", padding=6, relief="flat", background="#333333", foreground="white")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 16))
style.configure("TEntry", font=("Arial", 14), padding=6)
style.configure("TCombobox", font=("Arial", 14), padding=6)
style.configure("Horizontal.TScale", background="#333333")

# Create GUI components
title_label = ttk.Label(root, text="Text-to-Speech Converter", background="#f0f0f0", font=("Arial", 32, "bold"))
text_label = ttk.Label(root, text="Enter text:", background="#f0f0f0", font=("Arial", 16))
text_entry = tk.Text(root, height=10, width=60, font=("Arial", 14), bd=2, relief="solid", wrap="word")
convert_button = ttk.Button(root, text="Convert", command=convert_text_to_speech)

voice_label = ttk.Label(root, text="Select voice:", background="#f0f0f0", font=("Arial", 16))
voices = pyttsx3.init().getProperty('voices')
voice_options = [voice.name for voice in voices]
voice_combo = ttk.Combobox(root, values=voice_options)
voice_combo.current(0)

rate_label = ttk.Label(root, text="Adjust rate:", background="#f0f0f0", font=("Arial", 16))
rate_scale = ttk.Scale(root, from_=50, to=300, length=300, orient=tk.HORIZONTAL)

# Place GUI components on the window
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30))
text_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
text_entry.grid(row=1, column=1, padx=20, pady=5, rowspan=2, columnspan=2)
convert_button.grid(row=3, column=0, columnspan=2, pady=20, padx=(20, 10))

voice_label.grid(row=4, column=0, padx=20, pady=5, sticky="w")
voice_combo.grid(row=4, column=1, padx=20, pady=5, columnspan=2)

rate_label.grid(row=5, column=0, padx=20, pady=5, sticky="w")
rate_scale.grid(row=5, column=1, padx=20, pady=5, columnspan=2)

# Run the main event loop
root.mainloop()
