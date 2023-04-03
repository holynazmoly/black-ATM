from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

window = ThemedTk(theme='equilux')
window.geometry("250x500")
window.title("ATM")
window.config(themebg="equilux")
ball=1000

file= open("../../TinkinerProjects/GeneralExercises/transactions.txt", "w")

file.close()

def bal():
    global ball #WE BALL
    for widget in window.winfo_children():
        widget.destroy()
    lbl = Label(window, text="Your balance is: "+ str(ball), font=(20))
    lbl.place(x=50, y=180)
    btn2 = ttk.Button(window, text="back", command=first_window)
    btn2.place(x=80, y=320)
    mytag = ttk.Label(window, text="black ATM© - made by holynazmoly")
    mytag.place(x=0, y=480)

def new_wd():
    global wd_entry
    global ball
    if int(wd_entry.get()) > ball:
        dumdumlbl = Label(window, text="Sorry but you dont have enough quids :( ")
        dumdumlbl.place(x=30, y=190)
    else:
        entrylbl = Label(window, text="you succesfully withdrawed " + wd_entry.get() + " quids")
        entrylbl.place(x=30, y=190)
        ball=ball - int(wd_entry.get())


def wd():
    global wd_entry
    for widget in window.winfo_children():
        widget.destroy()
    lbl = Label(window, text="how many quids will you withdraw?")
    lbl.place(x=20, y=60)
    wd_entry = Entry(window)
    wd_entry.place(x=50, y=90)
    btn1 = ttk.Button(window, text="Withdraw", command=new_wd)
    btn1.place(x=80, y=150)
    btn2 = ttk.Button(window, text="back", command=first_window)
    btn2.place(x=80, y=230)
    mytag = ttk.Label(window, text="black ATM© - made by holynazmoly")
    mytag.place(x=0, y=480)


def giftitgodamnit():
    global frien_entry
    global money_entry
    global ball
    if int(money_entry.get()) > ball:
        dumdumlbl = Label(window, text="Sorry but you dont have enough quids :( ")
        dumdumlbl.place(x=20, y=280)
    else:

        lbl = Label(window, text="You succesfully gifted " + money_entry.get() + " to " + frien_entry.get())
        lbl.place(x=20, y=280)
        ball = ball - int(money_entry.get())
        file = open("../../TinkinerProjects/GeneralExercises/transactions.txt", "a")
        file.write(str(money_entry.get()+"\n"))
        file.close()


def friendgift():
    global frien_entry
    lbl = Label(window, text="how many quids will you gift to " + frien_entry.get() + "?")
    lbl.place(x=20, y=150)
    file= open("../../TinkinerProjects/GeneralExercises/transactions.txt", "a")
    file.write(str(frien_entry.get()))
    file.close()
    global money_entry
    money_entry = Entry(window)
    money_entry.place(x=50, y=180)
    btn1 = ttk.Button(window, text="GIFT!!!",command=giftitgodamnit)
    btn1.place(x=80, y=240)



def gift():
    global frien_entry
    for widget in window.winfo_children():
        widget.destroy()
    lbl = Label(window, text="To who will you gift your quids?")
    lbl.place(x=50, y=60)
    frien_entry = Entry(window)
    frien_entry.place(x=50, y=90)
    btn_frein= ttk.Button(window, text="Enter",command=friendgift)
    btn_frein.place(x=180, y=85)
    btn2 = ttk.Button(window, text="back", command=first_window)
    btn2.place(x=80, y=320)
    mytag = ttk.Label(window, text="black ATM© - made by holynazmoly")
    mytag.place(x=0, y=480)


def new_depo():
    global password_entry
    global ball
    entrylbl = Label(window, text="you succesfully depositted " + password_entry.get() + " quids")
    entrylbl.place(x=30, y=190)
    ball = ball + int(password_entry.get())


def depo():
    global password_entry
    for widget in window.winfo_children():
        widget.destroy()
    lbl = Label(window, text="how many quids will you deposit?")
    lbl.place( x=50, y=60)
    password_entry = Entry(window)
    password_entry.place( x=50, y=90)
    btn1 = ttk.Button(window, text="Deposit", command=new_depo)
    btn1.place(x=80, y=150)
    btn2 = ttk.Button(window, text="back", command=first_window)
    btn2.place(x=80, y=230)
    mytag = ttk.Label(window, text="black ATM© - made by holynazmoly")
    mytag.place(x=0, y=480)

def EXIT():
    window.destroy()

def first_window():
    for widget in window.winfo_children():
        widget.destroy()
    btn1 = ttk.Button(window, text="Balance", command=bal)
    btn1.place(x=80, y=50)
    btn1= ttk.Button(window, text="Deposit",command=depo)
    btn1.place(x=80,y=90)
    btn2= ttk.Button(window, text="Withdraw",command=wd)
    btn2.place(x=80, y=130)
    btn3= ttk.Button(window, text="Send gift", command=gift)
    btn3.place(x=80,y=170)
    exitbtn= ttk.Button(window, text="EXIT",command=EXIT)
    exitbtn.place(x=80, y=210)
    mytag = ttk.Label(window, text="black ATM© - made by holynazmoly")
    mytag.place(x=0, y=480)

btn= ttk.Button(window, text="ENTER",command=first_window)
btn.place(x=80, y=200)
mytag= ttk.Label(window, text="black ATM© - made by holynazmoly")
mytag.place(x=0,y=480)
window.mainloop()
