from modules import speakingFile
import random
from playsound import playsound

def flip():
    speakingFile.speak("Flipping a coin")
    playsound('flipACoin.mp3')
    coin = ['heads','tails']
    toss = random.choice(coin)
    speakingFile.speak("Its " + toss)
