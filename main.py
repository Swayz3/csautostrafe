import multiprocessing
import keyboard as kb
import time
import pyautogui as pg
from tkinter import *
root = Tk()
screen_width = root.winfo_screenwidth()
global auto_strafe
auto_strafe = False
def overlay():
    labelvar = StringVar
    labelvar = "Auto strafe"
    label = Label(root, text=labelvar,bg=f"grey6", fg="green3")
    label.place(x=0, y=0)
    root.geometry("64x20")
    root.overrideredirect(True)
    root.update()
    root.deiconify()
    label.pack()
    global auto_strafe
    if auto_strafe == False:
        root.withdraw()
def Mousepos():
    pos = pg.position()
    if kb.is_pressed('left'):
        kb.release('a')
        kb.release('d')
    elif kb.is_pressed('w'):
        kb.release('a')
        kb.release('d')
        time.sleep(.1)
    elif pos.x > (screen_width // 2):
        kb.release('a')
        kb.press('d')
        time.sleep(.005)
    elif pos.x < (screen_width // 2):
        kb.release('d')
        kb.press('a')
        time.sleep(.005)
def start():
    global auto_strafe
    auto_strafe = not auto_strafe
    if auto_strafe == True:
        print("start")
    else:
        print("stop")
if __name__=="__main__":
  with multiprocessing.Pool(processes=10) as pool:
      pool.map(Mousepos)
kb.add_hotkey('left', start)
while True:
    if auto_strafe:
        overlay()
        Mousepos()
    else:
        overlay()
root.mainloop()
    