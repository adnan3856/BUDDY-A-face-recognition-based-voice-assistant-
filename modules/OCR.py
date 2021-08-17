import cv2
import pytesseract as py
import tkinter as tk
from tkinter import filedialog
from modules import speakingFile

root = tk.Tk()
root.withdraw()
tessdata_dir_config = '--tessdata-dir "<C:/Program Files (x86)/Tesseract-OCR/tessdata>"'
py.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def identify_the_image():
    file_path = filedialog.askopenfilename()
    print(file_path)
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(py.image_to_string(img))
    text = py.image_to_string(img)
    speakingFile.speak(text)
    cv2.waitKey(0)


# identify_the_image()
root.destroy()