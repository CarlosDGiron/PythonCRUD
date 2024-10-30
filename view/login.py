from tkinter import *

root=Tk()
root.title("SAE/SAP Login")
root.resizable(False,False)
root.config(bg="Gray")

frame=Frame(root, width=800, height=480)
frame.pack()

userEntry=Entry(frame)
userEntry.config(justify="center")
userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

passEntry=Entry(frame)
passEntry.config(show="·",justify="center")
passEntry.grid(row=2,column=1, padx=10, pady=10, sticky="E")

titleLabel=Label(frame,text="SAE/SAP Login")
titleLabel.config(justify="center",font=("Helvetica", 12, "bold"), anchor="center")
titleLabel.grid(row=0, column=0, columnspan=2, sticky="NSEW")

userLabel=Label(frame,text="Usuario:")
userLabel.config(justify="left")
userLabel.grid(row=1,column=0, padx=10, pady=10, sticky="W")

passLabel=Label(frame,text="Password:")
passLabel.config(justify="left")
passLabel.grid(row=2,column=0, padx=10, pady=10, sticky="W")

loginButton=Button(frame,text="Loguearse")
loginButton.grid(row=3,column=1, padx=10, pady=10, sticky="EW")

closeButton=Button(frame,text="Cerrar")
closeButton.grid(row=3,column=0, padx=10, pady=10, sticky="EW")

root.mainloop()