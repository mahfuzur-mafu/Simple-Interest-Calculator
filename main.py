from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

# GUI
window = tk.Tk()
window.title("Python Interest Calculator")
window.iconbitmap("logo2.png")
window.geometry("500x350")
window.eval('tk::PlaceWindow . center')
window.resizable(0, 0)
canvas=Canvas(window,width=500,height=350)
image = ImageTk.PhotoImage(Image.open("cover.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

footer = Label(window, text=f"© 2022 Md. Mahfuzur Rahman.All Rights Reserved", font="arial 8")
footer.place(x=115, y=330)


# Calculaton
def calculate():
    p = float(principal_box.get())
    r = float(int_box.get())
    t = float(time_box.get())
    total = (p * r * t) / 100
    w_t = total + p
    Label(text=f"{total}", font="arial 20 bold").place(x=200, y=220)
    Label(text=f"{w_t}", font="arial 20 bold").place(x=200, y=260)


# GUI Output

principal = Label(window, text="Principal Amount", font="arial 15")
int_rate = Label(window, text="Rate oF Interest", font="arial 15")
time_year = Label(window, text="Time(Year)", font="arial 15")

# GUI Output  row*col

principal.place(x=50, y=20)
int_rate.place(x=50, y=90)
time_year.place(x=50, y=160)

interest = Label(window, text="Interest:", font="arial 15")
interest.place(x=50, y=230)
with_interest = Label(window, text="Total Amount:", font="arial 15")
with_interest.place(x=50, y=270)
# variable
principal_val = StringVar()
int_val = StringVar()
time_val = StringVar()

# GUI input box
principal_box = Entry(window, textvariable=principal_val, font="arial 20", width=8)
int_box = Entry(window, textvariable=int_val, font="arial 20", width=8)
time_box = Entry(window, textvariable=time_val, font="arial 20", width=8)

# GUI input box row* col
principal_box.place(x=200, y=20)
int_box.place(x=200, y=90)
time_box.place(x=200, y=160)
# two buttons
Button(text="Calculate", font="arial 15", bg="yellow", fg="black", command=calculate).place(x=350, y=20)
Button(text="Exit", command=lambda: exit(), font="arial 15", width=8).place(x=350, y=90)

window.mainloop()
