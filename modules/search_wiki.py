from modules import speakingFile
import wikipedia

def search_wiki(query):
    # speakingFile.speak('Searching Wikipedia...')
    results = wikipedia.summary(query , sentences=2)
    speakingFile.speak("According to Wikipedia")
    print(results)
    speakingFile.speak(results)


# search_wiki("corona virus")