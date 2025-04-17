
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# Initializing text-to-speech engine "voice"
voice = pyttsx3.init()

# opening file menu
pdf = askopenfilename()

# Opening the PDF file
with open(pdf, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    # Looping through all pages and extracting the text
    for page in reader.pages:
        text = page.extract_text()

        # converting text to speech
        voice.say(text)
        voice.runAndWait()
