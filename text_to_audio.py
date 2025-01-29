from gtts import gTTS
import os

# Text to be converted to audio
text = Hello, you've reached eunoiaAI. WE'RE ON A MISSION TO REVOLUTIONIZE HOW BUSINESSES INNOVATE WITH THE POWER OF ARTIFICIAL INTELLIGENCE! To learn more and schedule a personalized demo, please visit us at eunoia-AI-dot-co. Otherwise, leave a message and Renee will respond ASAP.

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named "output.mp3"
speech.save("output.mp3")

# Playing the converted file
os.system("start output.mp3")
