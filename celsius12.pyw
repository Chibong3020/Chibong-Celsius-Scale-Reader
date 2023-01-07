from tkinter import *
from PIL import ImageTk,Image

def scaler():
    a =scale.get()
    print(f"Your temperature is {a} degree celsius")
    label.config(text=f"Your temperature is {a} degree celsius")


window = Tk()
window.geometry =("420x420")
window.title("Chibong celsius scale reader")
window.config(background="#05f287")

kabel = Label(window,
text="Chibong Celsius Scale Reader",
font=("Arial",25),
bg="yellow",
fg="Purple",
padx= 10,
pady= 10,
relief = RAISED,
bd=10)

scale=Scale(window,
from_=100,
to=0,
bg="black",
fg="#FF1C00",
width= 10,
length=500,
font=("consolas",20),
tickinterval=10,
showvalue=0,
troughcolor="#69EAFF")


button = Button(window,
font=("Arial",25),
bg="yellow",
fg="purple",
padx= 10,
pady= 10,
command=scaler,
text = "Temperature reader",
relief= RAISED,
bd=10
)

label = Label(window,
text="",
font=("Arial",25),
bg="purple",
fg="yellow",
padx= 10,
pady= 10,
relief = RAISED,
bd=10)



window.attributes('-topmost',True)



scale.pack()
button.pack(side ="bottom")
label.pack(side="bottom")
kabel.pack(side="top")
window.mainloop()