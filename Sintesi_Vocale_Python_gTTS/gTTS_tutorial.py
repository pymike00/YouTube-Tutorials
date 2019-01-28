from gtts import gTTS
import subprocess

text = """ciao a tutti, questo è il primo test!"""

tts = gTTS(text=text, lang='it')
tts.save("tts_output_audio.mp3")

print("tutto fatto, file salvato!")

subprocess.run(["audacious", "tts_output_audio.mp3"])