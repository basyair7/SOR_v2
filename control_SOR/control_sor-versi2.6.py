from tkinter import *
from tkinter import messagebox
import serial
import time
import sqlite3

# create a database to store devices
conn = sqlite3.connect("board_arduino.db")
c = conn.cursor()

# Create table device
c.execute("""CREATE TABLE IF NOT EXISTS arduinoData(
        id_dev INTEGER PRIMARY KEY
        )""")

# Input port arduino in database
def con_device():
    try:
        id_drive = id_dev.get()

        # Open database
        conn = sqlite3.connect("board_arduino.db")
        c = conn.cursor()
        c.execute("SELECT * FROM arduinoData")

        alright = 0
        for row in c.fetchall():
            if int(row[0]) == int(id_drive):
                alright = 1
        if alright == 0:
            delete()
            id_drive = id_dev.get()
            # Insert data in device
            c.execute("INSERT INTO arduinoData VALUES (:id_dev)",
            {
                'id_dev': id_drive
            })

            # Show port driver
            c.execute("SELECT *, oid FROM arduinoData")
            driver_port = c.fetchall()
            print_device= ""
            for record in driver_port:
                print_device += f"COM{record[0]}"

            id_connect.insert(END, f"Connect : {print_device}")

        elif alright == 1:
            messagebox.showwarning('Informasi', 'No. ID Device sudah ada')
            id_connect.delete(0,END)
            # Show port driver
            c.execute("SELECT *, oid FROM arduinoData")
            driver_port = c.fetchall()
            print_device= ""
            for record in driver_port:
                print_device += f"COM{record[0]}"

            id_connect.insert(END, f"Connect : {print_device}")
    except:
        messagebox.showerror("Terjadi kesalahan", "1. Serial Port tidak boleh kosong!\n2. Isi angka saja!")

    conn.commit()
    conn.close()

    id_dev.delete(0, END)

def opsi():
    try:
        # open database
        conn = sqlite3.connect("board_arduino.db")
        # Create cursor
        c = conn.cursor()
        c.execute("SELECT *, oid FROM arduinoData")
        driver_port = c.fetchall()
        print_device = ""
        for record in driver_port:
            print_device += f"COM{record[0]}"

        board = serial.Serial(print_device, 9600) # see in device manager or port in tool arduino

        conn. commit()
        conn.close()
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

        global home_opsi
        home_opsi = Tk()
        home_opsi.title("Tombol Opsi")
        home_opsi.geometry("400x200")


        # Create label for saklar 1
        lbl_saklar_1 = Label(home_opsi, text="Saklar 1")
        lbl_saklar_1.grid(row=0, column=1, columnspan=2, pady=(10,0), padx=12)

        # Create button for saklar 1
        # ON
        btn_saklar_1_on = Button(home_opsi, text="Saklar 1 ON", command=saklar_1_on)
        btn_saklar_1_on.grid(row=1, column=1, columnspan=2, pady=10, padx=10, ipadx=15)
        # OFF
        btn_saklar_1_off = Button(home_opsi, text="Saklar 1 OFF", command=saklar_1_off)
        btn_saklar_1_off.grid(row=3, column=1, columnspan=2, ipadx=13)

        # Create label for saklar 2
        lbl_saklar_2 = Label(home_opsi, text="Saklar 2")
        lbl_saklar_2.grid(row=0, column=3, columnspan=2, pady=(10,0), padx=13)

        # Create button for saklar 2
        # ON
        btn_saklar_2_on = Button(home_opsi, text="Saklar 2 ON", command=saklar_2_on)
        btn_saklar_2_on.grid(row=1, column=3, columnspan=2, ipadx=15)
        # OFF
        btn_saklar_2_off = Button(home_opsi, text="Saklar 2 OFF", command=saklar_2_off)
        btn_saklar_2_off.grid(row=3, column=3, columnspan=2, ipadx=13)

        # Create label for saklar 3
        lbl_saklar_3 = Label(home_opsi, text="Saklar 3", )
        lbl_saklar_3.grid(row=0, column=5, columnspan=2, pady=(10,0), padx=11)

        # Create button for saklar 3
        # ON
        btn_saklar_3_on = Button(home_opsi, text="Saklar 3 ON", command=saklar_3_on)
        btn_saklar_3_on.grid(row=1, column=5, columnspan=2, padx=10, pady=10, ipadx=15)
        # OFF
        btn_saklar_3_off = Button(home_opsi, text="Saklar 3 OFF", command=saklar_3_off)
        btn_saklar_3_off.grid(row=3, column=5, columnspan=2, ipadx=13)

        # Create label all saklar on
        lbl_saklar_on = Label(home_opsi, text="Hidup Semua", )
        lbl_saklar_on.grid(row=6, column=1, columnspan=2, pady=(13,0), padx=11)

        # Create on all saklar button
        btn_on = Button(home_opsi, text="ON All Saklar", command=all_on)
        btn_on.grid(row=7, column=1, columnspan=2, pady=10, padx=10, ipadx=15)

        # Create label all saklar off
        lbl_saklar_off = Label(home_opsi, text="Mati Semua")
        lbl_saklar_off.grid(row=6, column=5, columnspan=2, pady=(13,0), padx=11)

        # Create off all saklar button
        btn_off = Button(home_opsi, text="OFF All Saklar", command=all_off)
        btn_off.grid(row=7, column=5, columnspan=2, pady=10, padx=10, ipadx=13)

        home_opsi.mainloop()
    except:
        messagebox.showerror("Terjadi kesalahan", "1. Pastikan Serial Port sudah diisi\n2. Pastikan serial port sama di arduino ide... \n3. Pastikan board sudah diupload program utamanya dan tidak terputus kabel datanya")

# delete record port
def delete():
    # Open Databases
    conn = sqlite3.connect("board_arduino.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS arduinoData;")
    c.execute("""CREATE TABLE IF NOT EXISTS arduinoData (
            id_dev INTEGER PRIMARY KEY
            )""")

    conn.commit()
    conn.close()

    # Clear listbox
    id_connect.delete(0, END)

# Exit program
def exit():
    pertanyaan = messagebox.askquestion('Keluar', 'Kamu yakin keluar dari aplikasi?')
    if pertanyaan == 'yes':
        quit()

#<----------------Main Menu-------------------->
# Create home App tkinter
home = Tk(); home.geometry('330x430')
home.title("Control SOR v2.6")

# Create frame layout
frm_port_board = Frame(home, relief=RIDGE, borderwidth=5)
frm_port_board.grid(row=0, column=0, columnspan=2, ipadx=1, padx=5, pady=10)
frm_info_note = Frame(home, relief=RIDGE, borderwidth=5)
frm_info_note.grid(row=1, column=0, columnspan=2, ipadx=1, pady=10)
frm_creator = Frame(home, relief=RIDGE, borderwidth=5)
frm_creator.grid(row=2, column=0, columnspan=2, ipadx=2, padx=10)


# Port board
lbl_input = Label(frm_port_board, text="Port COM\t: ")
lbl_input.grid(row=0, column=5, padx=10,pady=(10,0))
id_dev = Entry(frm_port_board, width=20)
id_dev.grid(row=0, column=6, padx=20, pady=(10,0))

# Create button connect device
btn_con = Button(frm_port_board, text="Connect", command=con_device)
btn_con.grid(row=1, column=5, columnspan=1, pady=10, padx=10, ipadx=23)

# Create option button
# Tombol opsi
btn_opsi = Button(frm_port_board, text="Tombol Opsi", command=opsi)
btn_opsi.grid(row=1, column=6, columnspan=1, padx=10, pady=10, ipadx=23)

# Create button delete device
btn_del = Button(frm_port_board, text="Delete Port", command=delete)
btn_del.grid(row=2, column=5, columnspan=1, ipadx=17, pady=5)

# Create button exit
btn_exit = Button(frm_port_board, text="Exit", command=exit)
btn_exit.grid(row=2, column=6, columnspan=1, ipadx=47)

# show note app
# create note
note = ["NOTE : ",
        "1. Isi Serial Port hanya angka saja", "    (Port COM Hanya sekali isi!)",
        " "]
id_connect = Listbox(frm_info_note)
id_connect.grid(row=0, column=1, columnspan=5, pady=10, padx=10, ipadx=73, ipady=1)
for list in note:
    id_connect.insert(END, list)
"""
id_connect = Listbox(frm_connect_creator)
id_connect.grid(row=5, column=8, columnspan=2, pady=10, padx=4, ipadx=1, ipady=1)
"""
# Create author app
author = Label(frm_creator, text="Creator\t:  @basyair7\n App ver\t:  v2.5\n@2020")
author.grid(row=4, column=5, columnspan=5, padx=10)

# Commit changes
conn.commit()
# Close connection
conn.close()
# home window mainloop
home.mainloop()
