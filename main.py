import tkinter
import pyautogui
from tkinter import *
import random as r
import winsound
import os
from Qmanager import question_manager



#setgame
FontSizeOffset = 30
count = 0
a, b = 0, 0
n = 1
Hint1 = 0
Hint = 1

os.system('chcp 65001')

Qmaker = question_manager()


ScreenW, ScreenH = pyautogui.size()
size = str(ScreenW) + "x" + str(ScreenH)


text = '? ■ ? = ?'
A = r.randrange(10, 100)
while True:
    B = r.randrange(10, 100)
    if A != B:
        break
X = Qmaker.answer(A, B)
print(f"a = {A}, b = {B}, answer = {X}")
print(Qmaker.explain.decode('utf-8'))


def ShowAnswer():
    q = pyautogui.confirm("Show The Answer?", buttons=['YES', 'NO'])
    if q == 'YES':
        labelR.config(text=X)
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)


def WriteAnswer():
    ipt = int(pyautogui.prompt("Put The Answer"))
    if ipt == X:
        winsound.PlaySound("Correct.wav", winsound.SND_ASYNC)
        pyautogui.alert("Correct!")
        labelR.config(text=X)
    else:
        winsound.PlaySound("Wrong.wav", winsound.SND_ASYNC)
        pyautogui.alert("Wrong!")


def ChangeFontSize(text):
    n = len(text)
    temp = 400 / n
    FontSize = round(temp * 1.1)
    y = round(temp)
    x = 200
    return x, y, FontSize


def btnpress():
    global a, b
    global Hint
    if Hint == 1:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint1.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint1.place(x=(445 - x), y=(690 - y))
        labelHint1.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint1.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint1.place(x=(445 - x), y=(690 - y))
        labelHint1.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint1.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint1.place(x=(445 - x), y=(690 - y))
        labelHint1.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 2

    elif Hint == 2:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint2.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint2.place(x=(955 - x), y=(690 - y))
        labelHint2.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint2.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint2.place(x=(955 - x), y=(690 - y))
        labelHint2.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint2.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint2.place(x=(955 - x), y=(690 - y))
        labelHint2.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 3

    elif Hint == 3:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint3.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint3.place(x=(1475 - x), y=(690 - y))
        labelHint3.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint3.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint3.place(x=(1475 - x), y=(690 - y))
        labelHint3.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint3.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint3.place(x=(1475 - x), y=(690 - y))
        labelHint3.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 4

    elif Hint == 4:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint4.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint4.place(x=(445 - x), y=(810 - y))
        labelHint4.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint4.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint4.place(x=(445 - x), y=(810 - y))
        labelHint4.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint4.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint4.place(x=(445 - x), y=(810 - y))
        labelHint4.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 5

    elif Hint == 5:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint5.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint5.place(x=(955 - x), y=(810 - y))
        labelHint5.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint5.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint5.place(x=(955 - x), y=(810 - y))
        labelHint5.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint5.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint5.place(x=(955 - x), y=(810 - y))
        labelHint5.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 6

    elif Hint == 6:
        a = pyautogui.prompt('Input First Num')
        text = a + ' ■ ? = ?'
        labelHint6.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint6.place(x=(1475 - x), y=(810 - y))
        labelHint6.config(font=('Arial', FontSize))

        b = pyautogui.prompt('Input Second Num')
        text = a + ' ■ ' + b + ' = ?'
        labelHint6.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint6.place(x=(1475 - x), y=(810 - y))
        labelHint6.config(font=('Arial', FontSize))

        pyautogui.confirm("Show The Result!", buttons=['YES', 'NO'])
        text = a + ' ■ ' + b + ' = ' + str(Qmaker.answer(int(a), int(b)))
        labelHint6.config(text=text)
        x, y, FontSize = ChangeFontSize(text)
        labelHint6.place(x=(1475 - x), y=(810 - y))
        labelHint6.config(font=('Arial', FontSize))
        winsound.PlaySound("Kung.wav", winsound.SND_ASYNC)
        Hint = 7
    else:
        pyautogui.alert("          힌트 개수 초과!          ")




root = Tk()
root.title("LIMES")
root.geometry(size)

wall = PhotoImage(file="wall.png")
wall_label = Label(image=wall)
wall_label.place(x=-2, y=-2)

labelQ1 = tkinter.Label(root, font=('Arial', FontSizeOffset * 2), background="#2D775C")
labelQ1.config(text=A)
labelQ1.place(x=570, y=450)

labelQ2 = tkinter.Label(root, font=('Arial', FontSizeOffset * 2), background="#2C785C")
labelQ2.config(text=B)
labelQ2.place(x=870, y=450)

labelR = tkinter.Label(root, font=('Arial', FontSizeOffset * 2), background="#2B775B")
labelR.config(text='?')
labelR.place(x=1180, y=450)

labelHint1 = tkinter.Label(root, background="#88A77E")
labelHint1.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint1.place(x=(445 - x), y=(690 - y))
labelHint1.config(font=('Arial', FontSize))

labelHint2 = tkinter.Label(root, background="#88A77E")
labelHint2.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint2.place(x=(955 - x), y=(690 - y))
labelHint2.config(font=('Arial', FontSize))

labelHint3 = tkinter.Label(root, background="#88A77E")
labelHint3.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint3.place(x=(1475 - x), y=(690 - y))
labelHint3.config(font=('Arial', FontSize))

labelHint4 = tkinter.Label(root, background="#88A77E")
labelHint4.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint4.place(x=(445 - x), y=(810 - y))
labelHint4.config(font=('Arial', FontSize))

labelHint5 = tkinter.Label(root, background="#88A77E")
labelHint5.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint5.place(x=(955 - x), y=(810 - y))
labelHint5.config(font=('Arial', FontSize))

labelHint6 = tkinter.Label(root, background="#88A77E")
labelHint6.config(text=text)
x, y, FontSize = ChangeFontSize(text)
labelHint6.place(x=(1475 - x), y=(810 - y))
labelHint6.config(font=('Arial', FontSize))

btn = tkinter.Button(root)
btn.config(text="Input Hint", width=15, font=('Arial', 15), background="#603606")
btn.config(command=btnpress)
btn.pack()

Sansbtn = tkinter.Button(root)
Sansbtn.config(text="Show Answer", width=15, font=('Arial', 15), background="#603606")
Sansbtn.config(command=ShowAnswer)
Sansbtn.pack(side='bottom')

Wansbtn = tkinter.Button(root)
Wansbtn.config(text="Write Answer", width=15, font=('Arial', 15), background="#603606")
Wansbtn.config(command=WriteAnswer)
Wansbtn.pack(side='bottom')
root.mainloop()