import screen_brightness_control as sbc

def bright_control(text):
    if text.endswith("%"):
        text = text[:-(1)]
        for i in text.split():
            if i.isdigit():
                num = int(i)
        sbc.set_brightness(num)
    return num

# level = bright_control("brightness at 30%")
