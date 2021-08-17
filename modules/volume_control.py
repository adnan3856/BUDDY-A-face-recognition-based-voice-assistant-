import pyautogui

VOLUME_STRS = ["max volume" , "maximum volume", "volume max", "volume maximum"]

def volume_control(text):
    if "volume up" in text:
        pyautogui.press("volumeup")
    elif "volume down" in text:
        pyautogui.press("volumedown")
    elif "mute" in text:
        pyautogui.press("volumemute")
    for phrase in VOLUME_STRS:
        if phrase in text:
            for i in range(0, 50):
                pyautogui.press("volumeup")

# volume_control("volume maximum")