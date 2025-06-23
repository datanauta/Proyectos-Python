from gtts import gTTS

# Abre el archivo de texto en modo lectura con codificación UTF-8
with open('libro.txt', 'r', encoding='utf-8') as file:
    textBook = file.read()

# Convierte el texto a audio (voz en español)
audio = gTTS(text=textBook, lang='es')

# Guarda el resultado como un archivo de audio MP3
audio.save('audioBook.mp3')
