import tkinter as tk
from tkinter import ttk, scrolledtext
from deep_translator import GoogleTranslator

def translate_text():
    source_text = source_text_entry.get("1.0", tk.END).strip()
    if source_text:
        try:
            translated_text = GoogleTranslator(source=source_lang_combo.get().lower(), target=target_lang_combo.get().lower()).translate(source_text)
            target_text_entry.delete("1.0", tk.END)
            target_text_entry.insert(tk.END, translated_text)
        except Exception as e:
            target_text_entry.delete("1.0", tk.END)
            target_text_entry.insert(tk.END, f"Error: {e}")
    else:
        target_text_entry.delete("1.0", tk.END)
        target_text_entry.insert(tk.END, "Please enter text to translate.")

# Setting up the main window
root = tk.Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="Gray")

# Title label
label_title = tk.Label(root, text="Translator", font=("Time New Roman", 40, "bold"), bg="Gray")
label_title.place(x=100, y=40, height=50, width=300)

# Source text label and text entry
label_source_text = tk.Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg="Black", bg="Gray")
label_source_text.place(x=100, y=100, height=20, width=300)

source_text_entry = scrolledtext.ScrolledText(root, font=("Time New Roman", 20, "bold"), wrap=tk.WORD)
source_text_entry.place(x=10, y=130, height=150, width=480)

# Source and target language comboboxes
source_lang_combo = ttk.Combobox(root, values=["en", "fr", "de", "es", "tr", "zh"], font=("Time New Roman", 16))
source_lang_combo.place(x=10, y=300, height=40, width=150)
source_lang_combo.set("en")  # default source language

target_lang_combo = ttk.Combobox(root, values=["en", "fr", "de", "es", "tr", "zh"], font=("Time New Roman", 16))
target_lang_combo.place(x=330, y=300, height=40, width=150)
target_lang_combo.set("tr")  # default target language

# Translate button
button_translate = tk.Button(root, text="Translate", font=("Time New Roman", 16), relief=tk.RAISED, command=translate_text)
button_translate.place(x=170, y=300, height=40, width=150)

# Target text label and text entry
label_target_text = tk.Label(root, text="Dest Text", font=("Time New Roman", 20, "bold"), fg="Black", bg="Gray")
label_target_text.place(x=100, y=360, height=20, width=300)

target_text_entry = scrolledtext.ScrolledText(root, font=("Time New Roman", 20, "bold"), wrap=tk.WORD)
target_text_entry.place(x=10, y=400, height=150, width=480)

root.mainloop()
