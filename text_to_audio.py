from gtts import gTTS
import os

# Text to be converted to audio
text = "Hello, you've reached eunoia A I. WE'RE ON A MISSION TO REVOLUTIONIZE HOW BUSINESSES INNOVATE WITH THE POWER OF ARTIFICIAL INTELLIGENCE! To learn more or to  schedule a personalized demo, please visit us at eunoia A I dot co. Otherwise, leave a message and Renee will respond as soon as possible."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named "voicemail.mp3"
speech.save("voicemail.mp3")

# Playing the converted file
os.system("start voicemail.mp3")
