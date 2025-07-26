#!/user/bin/python
from gtts import gTTS
import os

# German text to be spoken
text = "Ich heiße Mahmoud Reda und ich lerne Python."

# Create a gTTS object with the German language
tts = gTTS(text=text, lang='de')  # 'de' = Deutsch (German)

# Save the generated speech to an MP3 file
tts.save("german_intro.mp3")

# Play the MP3 file using the system's default player (Windows)
os.system("start german_intro.mp3")


