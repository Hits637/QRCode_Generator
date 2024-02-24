from tkinter import *
import qrcode

root = Tk()
root.title("QR generator")
root.geometry("1000x550")
root.config(bg="skyblue")
root.resizable(False,False)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("assets/Qrcode_Generator/"+str(name)+".png")

Label(root,text="Title",fg="black",bg="yellow",font=20).place(x=50,y=160)

title=Entry(root,width=15,font="arial 15")
title.place(x=50,y=200)

Label(root,text="link",fg="black",bg="yellow",font=20).place(x=50,y=240)
entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=280)

Button(root,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=330)



root.mainloop()