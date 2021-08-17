import os
import random
import sys
from modules import speakingFile

def play_song():
            music_dir="F:\\voice assistant\\music"
            song = random.choice(os.listdir(music_dir))
            print("Playing..."+song)
            speakingFile.speak("Playing..."+song)
            os.startfile(os.path.join(music_dir, song))
            sys.exit()
