import subprocess
import pyperclip
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import psutil
from ecapture import ecapture as ec
from playsound import playsound
from modules import brightness, check_connection, OCR, news, make_a_note, ip_address, gender, read_from_clipboard, \
    speakingFile, search_wiki, send_sms, weather, volume_control, toss, play_song, aman_calander, adnan_calander
import screen_brightness_control as sbc
from face_recognition import face_recognizer_test
import pyjokes
import PyPDF2

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
WAKE = ["wake up buddy", "wake up", "buddy", "hey buddy"]
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
          "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENSIONS = ["rd", "th", "st", "nd"]
CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy", "events on monday"]
NOTE_STRS = ["make a note", "write this down", "remember this"]
GOODBYE_STRS = ["goodbye", "bye buddy", "bye"]
TIME_STRS = ["what is the time", "current time", "what time is it now", "time now"]
DATE_STRS = ["today's date", "current date", "date today"]
GREET_STRS = ["hello", "good morning", "good afternoon", "good evening"]
# SONG_STRS=["play song","play me a song","play a song","song","play music","music"]
SONG_STRS = ["song", "music"]
NEWS_STRS = ["Today's news", "Current news", "news", "news for today"]
COIN_STRS = ["flip a coin", "toss a coin ", "heads or tails"]


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speakingFile.speak("Good morning")
    elif hour >= 12 and hour < 18:
        speakingFile.speak("Good Afternoon")
    else:
        speakingFile.speak("Good night")


# what can the assistant do
def what_can_i_do():
    speakingFile.speak("It's written on the screen")
    print("It's written on the screen")


# tells the current time in hh:mm AM/PM format
def current_time():
    t = time.localtime()
    currentTime = time.strftime("%I:%M %p", t)
    speakingFile.speak("the current time is" + currentTime)


# speaks out current date in month,date,year
def current_date():
    today = datetime.date.today()
    today_date = today.strftime("%B %d, %Y")
    speakingFile.speak("Today's date is" + today_date)


class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()
        # self.query = ""  # self.get_audio()
        # self.text = ""  # self.get_audio()

    def run(self):
        self.BUDDY()

    def get_wake_up_audio(self):
        playsound('chime 1.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            said = r.recognize_google(audio, language='en-in')
            playsound('chime 2.mp3')
            print(">> ", said)
        except Exception:
            print("Say, Wake up BUDDY")
            speakingFile.speak("Say, Wake up BUDDY")
            return "None"
        return said.lower()

    def get_audio(self):
        playsound('chime 1.mp3')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            said = r.recognize_google(audio, language='en-in')
            playsound('chime 2.mp3')
            print(">> ", said)
        except Exception:
            print("Pardon me, please say that again")
            speakingFile.speak("Pardon me, please say that again")
            return "None"
        return said.lower()

    def reading(self):
        arr = os.listdir('/books')
        speakingFile.speak("which book do you want to read")
        speakingFile.speak("here are the list of books available")
        print(*arr, sep="\n")
        key = self.get_audio()
        print(key)
        for file_name in arr:
            if key in file_name:
                speakingFile.speak(file_name)
                absolute_path = os.path.abspath('books/' + file_name)
                book = open(str(absolute_path), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(book)
                pages = pdf_reader.numPages
                for num in range(int(pages)):
                    page = pdf_reader.getPage(num)
                    text = page.extractText()
                    speakingFile.speak(text)
            else:
                speakingFile.speak("book not found")
                # sys.exit()

    # greeting hello
    def greetings(self):
        now = datetime.datetime.now()  # current date and time
        day_time = int(now.strftime('%H'))
        if day_time < 12:
            speakingFile.speak('Hello' + self.greet + '. Good morning')
        elif 12 <= day_time < 18:
            speakingFile.speak('Hello' + self.greet + '. Good afternoon')
        else:
            speakingFile.speak('Hello' + self.greet + '. Good evening')

    def BUDDY(self):
        greet = "User"
        if gender.genderValue == "Male":
            greet = "Sir"
        if gender.genderValue == "Female":
            greet = "Mam"
        still_awake = False
        while True:
            print("Listening")
            text = self.get_wake_up_audio()
            for phrase in WAKE:
                if phrase in text:
                    # if text.count(WAKE[1]) > 0:
                    speakingFile.speak("YES,I am ready")
                    still_awake = True
                    break
            while still_awake:
                text = self.get_audio()

                if 'time' in text:
                    current_time()

                if 'date' in text:
                    current_date()

                if 'what can you do' in text:
                    what_can_i_do()

                if "who are you" in text:
                    speakingFile.speak("I am BUDDY, A personal voice assistant made by Adnan and Aaman. Currently I "
                                       "am programmed to do small tasks such as open websites, application, "
                                       "play music... Do you want me to do Something?")
                    text = self.get_audio()
                    if "yes" in text:
                        speakingFile.speak("Say wake up buddy")
                        break
                    elif "no" in text:
                        speakingFile.speak("Ok")
                        still_awake = False
                        break

                if 'thank you' in text:
                    speakingFile.speak("You are welcome")

                # if "play music" or "play song" in text:
                #     play_song.play_song()

                if 'search' in text:
                    statement = text.replace("search", "")
                    webbrowser.open("https://www.google.com/search?q=" + statement)
                    speakingFile.speak("Searching in google")

                if 'open' in text:
                    site = text.replace("open", '')
                    site_visit = "www." + site + ".com"
                    print(site_visit.replace(" ", ""))
                    webbrowser.open(site_visit.replace(" ", ""))
                    speakingFile.speak("opening " + site)

                if 'launch' in text:
                    app_name = text.replace("launch", "")
                    app_name = app_name.replace(" ", "")
                    print(app_name)
                    if app_name == 'notepad':
                        os.system("Notepad")

                    elif app_name == 'pythoneditor' or app_name == 'pycharm':
                        appPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe"
                        os.startfile(appPath)

                    elif app_name == 'javaeditor' or app_name == 'intellij':
                        appPath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.2.4\\bin\\idea64.exe"
                        os.startfile(appPath)

                    elif app_name == 'Ceditor' or app_name == 'codeblocks':
                        appPath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
                        os.startfile(appPath)

                    elif app_name == 'vscode':
                        appPath = "F:\\visual studio\\Microsoft VS Code\\Code.exe"
                        os.startfile(appPath)

                    elif app_name == 'eclipse':
                        appPath = "C:\\Users\\ADDY\\eclipse\\jee-2020-06\\\eclipse\\eclipse.exe"
                        os.startfile(appPath)

                    elif app_name == 'chrome' or app_name == "googlechrome":
                        appPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                        os.startfile(appPath)

                    elif app_name == 'vlc':
                        appPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                        os.startfile(appPath)

                    elif app_name == ' msedge' or app_name == "microsoftedge":
                        appPath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Applications\\msedge.exe"
                        os.startfile(appPath)

                    else:
                        speakingFile.speak("Cannot find the application")
                        print("Cannot find the application")

                if 'news' in text:
                    speakingFile.speak("Which topic do you want to hear?")
                    topic_item = self.get_audio()
                    news.todays_news(topic_item)

                if 'identify the image' in text:
                    speakingFile.speak("Select the image with text:")
                    OCR.identify_the_image()

                if 'joke' in text:
                    speakingFile.speak(pyjokes.get_joke())

                for phrase in COIN_STRS:
                    if phrase in text:
                        toss.flip()

                for phrase in NOTE_STRS:
                    if phrase in text:
                        speakingFile.speak("What would you like me to write down?")
                        note_text = self.get_audio()
                        make_a_note.note(note_text)
                        speakingFile.speak("I've made a note of that.")

                for phrase in CALENDAR_STRS:
                    if phrase in text:
                        authenticate_person = face_recognizer_test.authorized_name
                        if authenticate_person == 'Adnan':
                            SERVICE = adnan_calander.authenticate_google()
                            date = adnan_calander.get_date(text)
                            if date:
                                adnan_calander.get_events(date, SERVICE)
                            else:
                                speakingFile.speak("Oops! Didn't catch that")
                        elif authenticate_person == 'Aman':
                            SERVICE = aman_calander.authenticate_google()
                            date = aman_calander.get_date(text)
                            if date:
                                aman_calander.get_events(date, SERVICE)
                            else:
                                speakingFile.speak("Oops! Didn't catch that")
                        else:
                            speakingFile.speak("You are not an Authorized Person")
                            send_sms.send_sms()

                if "send a mail" in text:
                    speakingFile.speak("Sending mail.")

                if 'tell me about ' in text or 'what do you mean by ' in text:
                    speakingFile.speak('Searching Wikipedia...')
                    result = text.replace("tell me about", "")
                    search_wiki.search_wiki(result)

                if "camera" in text or "take a picture" in text:
                    ec.capture(0, "Device Camera", "img.jpg")
                    time.sleep(5)

                if "IP address" in text:
                    speakingFile.speak("Your IP address is " + ip_address.find_ip())

                if "read from clipboard" in text:
                    if pyperclip.paste() == "":
                        speakingFile.speak("Nothing in Clipboard.")
                    else:
                        speakingFile.speak(pyperclip.paste())

                if "clear clipboard" in text:
                    read_from_clipboard.clear_clipboard()
                    speakingFile.speak("Clipboard cleared.")

                if "brightness" in text:
                    speakingFile.speak("Current Brightness is at " + str(sbc.get_brightness()) + "%")
                    level = brightness.bright_control(text)
                    speakingFile.speak("Brightness set to " + level + "%")

                if "volume" in text:
                    volume_control.volume_control(text)

                if 'good night' in text:
                    speakingFile.speak("good night," + greet)
                    sys.exit()

                if 'good bye' in text:
                    speakingFile.speak("goodbye," + greet)
                    sys.exit()

                if "log off" in text or "sign out" in text:
                    speakingFile.speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])

                if "hibernate" in text or "sleep" in text:
                    speakingFile.speak("Hibernating the System")
                    subprocess.call("shutdown /i /h")


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi2.ui"))


class Main(QMainWindow, FROM_MAIN):
    # SETTING UP THE UI-TIME
    def showTime(self):
        label_time = time.strftime("%r")
        self.label_6.setText("<font size=20 color='white' align='center'>" + label_time + "</font>")
        self.label_6.setFont(QFont(QFont('Acens', 10)))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920, 1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        # if(gender.cap.isOpened() or face_recognizer_test.cam.isOpened()):
        #     imageValue = "./lib/face2.gif"
        # else:
        #     imageValue = "./lib/gifloader.gif"
        self.label_7 = QMovie("./lib/face2.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # SETTING UP THE UI-DATE
        self.ts = time.strftime("%A, %d %B")
        self.label_5.setText("<font size=20 color='white' align='center'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 10)))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        # SETTING UP UI MEMORY USAGE
        psutil.virtual_memory()
        dict(psutil.virtual_memory()._asdict())
        self.label_8.setText("<font size=20 color='white' align='center'>" + "Memory Usage:" + str(
            psutil.virtual_memory().percent) + " % " + "</font>")
        self.label_8.setFont(QFont(QFont('Acens', 8)))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)

        # SETTING UP UI CPU USAGE
        self.label_2.setText("<font size=20 color='white' align='center'>" + " CPU Usage: " + str(
            psutil.cpu_percent(2)) + "%" + "</font>")
        self.label_2.setFont(QFont(QFont('Acens', 8)))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        # SETTING UP GENDER VALUE IN UI
        self.gender_label_2.setText(
            "<font size=20 color='white' align='center'>" + " Gender: " + str(gender.genderValue) + "</font>")
        self.gender_label_2.setFont(QFont(QFont('Acens', 8)))
        self.gender_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gender_label.setText("<font size=20 color='white' align='center'>" + "Confidence: " + str(
            gender.genderConfidence) + "%" + "</font>")
        self.gender_label.setFont(QFont(QFont('Acens', 8)))
        self.gender_label.setAlignment(QtCore.Qt.AlignCenter)

        # SETTING UP Face VALUE IN UI
        self.face_label_2.setText(
            "<font size=20 color='white' align='center'>" + " Confidence: " + str(
                face_recognizer_test.authorized_confidence) + "%" + "</font>")
        self.face_label_2.setFont(QFont(QFont('Acens', 8)))
        self.face_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.face_label.setText(
            "<font size=20 color='white' align='center'>" + "Name: " + str(
                face_recognizer_test.authorized_name) + "</font>")
        self.face_label.setFont(QFont(QFont('Acens', 8)))
        self.face_label.setAlignment(QtCore.Qt.AlignCenter)

        # SETTING WEATHER VALUE IN UI
        self.label_3.setText(
            "<font size=20 color='white' align='center'>" + str(weather.current_temperature) + "°C," + str(
                weather.current_humidiy) + "%, " + str(weather.weather_description).capitalize() + "</font>")
        self.label_3.setFont(QFont(QFont('Acens', 8)))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        # CHECKING IF INTERNET IS CONNECTED
        self.label_12.setText(
            "<font size=20 color='white' align='center'>" + "Internet: " + check_connection.res + "</font>")
        self.label_12.setFont(QFont(QFont('Acens', 8)))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)

        # BATTERY PERCENTAGE
        battery = psutil.sensors_battery()
        self.label_13.setText(
            "<font size=20 color='white' align='center'>" + "Battery: " + str(battery.percent) + " % " + "</font>")
        self.label_13.setFont(QFont(QFont('Acens', 8)))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
