from modules import speakingFile
import datetime
#greeting hello
def greetings():
    greet =""
    now = datetime.now()  # current date and time
    day_time = int(now.strftime('%H'))
    if day_time < 12:
        speakingFile.speak('Hello' + greet + '. Good morning')
    elif 12 <= day_time < 18:
        speakingFile.speak('Hello' + greet + '. Good afternoon')
    else:
        speakingFile.speak('Hello' + greet + '. Good evening')