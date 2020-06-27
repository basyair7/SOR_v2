from tkinter import *
from tkinter import font as tkfont
import serial

# create connect to serial
#board = serial.Serial('com3', 9600) # see in device manager or port in tool arduino

# create function saklar
# Saklar 1
# ON
def saklar_1_on():
    board.write(b'0')
# OFF
def saklar_1_off():
    board.write(b'1')

# Saklar 2
# ON
def saklar_2_on():
    board.write(b'2')
# OFF
def saklar_2_off():
    board.write(b'3')

# Saklar 3
# ON
def saklar_3_on():
    board.write(b'4')
# OFF
def saklar_3_off():
    board.write(b'5')

# Life all saklar
def all_on():
    board.write(b'6')
# Dead all saklar
def all_off():
    board.write(b'7')

# Create home App tkinter
home = Tk(); home.geometry('475x255')
home.title("Control SOR v2.5")

# Create label for saklar 1
lbl_saklar_1 = Label(home, text="Saklar 1", font="Purisa")
lbl_saklar_1.grid(row=0, column=1, columnspan=2, pady=(10,0), padx=12)

# Create button for saklar 1
# ON
btn_saklar_1_on = Button(home, text="Saklar 1 ON", font="chilanka", command=saklar_1_on)
btn_saklar_1_on.grid(row=1, column=1, columnspan=2, pady=10, padx=10, ipadx=15)
# OFF
btn_saklar_1_off = Button(home, text="Saklar 1 OFF", font="chilanka", command=saklar_1_off)
btn_saklar_1_off.grid(row=3, column=1, columnspan=2, ipadx=10)

# Create label for saklar 2
lbl_saklar_2 = Label(home, text="Saklar 2", font="Purisa")
lbl_saklar_2.grid(row=0, column=3, columnspan=2, pady=(10,0), padx=13)

# Create button for saklar 2
# ON
btn_saklar_2_on = Button(home, text="Saklar 2 ON", font="chilanka", command=saklar_2_on)
btn_saklar_2_on.grid(row=1, column=3, columnspan=2, ipadx=15)
# OFF
btn_saklar_2_off = Button(home, text="Saklar 2 OFF", font="chilanka", command=saklar_2_off)
btn_saklar_2_off.grid(row=3, column=3, columnspan=2, ipadx=10)

# Create label for saklar 3
lbl_saklar_3 = Label(home, text="Saklar 3", font="Purisa")
lbl_saklar_3.grid(row=0, column=5, columnspan=2, pady=(10,0), padx=11)

# Create button for saklar 3
# ON
btn_saklar_3_on = Button(home, text="Saklar 3 ON", font="chilanka", command=saklar_3_on)
btn_saklar_3_on.grid(row=1, column=5, columnspan=2, padx=10, pady=10, ipadx=15)
# OFF
btn_saklar_3_off = Button(home, text="Saklar 3 OFF", font="chilanka", command=saklar_3_off)
btn_saklar_3_off.grid(row=3, column=5, columnspan=2, ipadx=10)

# Create label all saklar on
lbl_saklar_on = Label(home, text="Hidup Semua", font="Purisa")
lbl_saklar_on.grid(row=6, column=1, columnspan=2, pady=(13,0), padx=11)

# Create on all saklar button
btn_on = Button(home, text="ON All Saklar", font="Purisa", command=all_on)
btn_on.grid(row=7, column=1, columnspan=2, pady=10, padx=10, ipadx=12)

# Create label all saklar off
lbl_saklar_off = Label(home, text="Mati Semua", font="Purisa")
lbl_saklar_off.grid(row=6, column=5, columnspan=2, pady=(13,0), padx=11)

# Create off all saklar button
btn_off = Button(home, text="OFF All Saklar", font="Purisa", command=all_off)
btn_off.grid(row=7, column=5, columnspan=2, pady=10, padx=10, ipadx=7)

# Create author app
author = Label(home, text="Creator : @basyair7", font="chilanka")
author.grid(row=8, column=3, columnspan=2, pady=12, padx=12)

# home window mainloop
home.mainloop()
