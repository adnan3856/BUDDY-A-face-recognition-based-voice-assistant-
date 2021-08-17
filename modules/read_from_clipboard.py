from tkinter import Tk

root = Tk()
root.withdraw()
def read_clipboard():
    result = root.selection_get(selection = "CLIPBOARD")
    root.destroy()
    return result

def clear_clipboard():
    root.clipboard_clear()
    root.destroy()

# clear_clipboard()