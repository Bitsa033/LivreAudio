from tkinter import *
from index import ia

# initialisation de la fenetre
tk= Tk()
# configuration de la fenetre
tk.title("Convertir un texte en audio")
tk.iconbitmap("favicon.ico")
tk.geometry("700x400")
background="blueviolet"
tk.config(background=background)
frame_2=Frame(tk,bg='white')
entry=Entry(tk,font=('Helvetica',30),bg=background,fg="white").pack(pady=12)
buton_1=Button(frame_2,text='Choose file ...',bg='#41B77E',padx=40,pady=20).pack(side=LEFT)
buton_4=Button(frame_2,command=ia,text='Start',bg='#41B77E',padx=40,pady=20).pack(side=LEFT)
buton_5=Button(frame_2,text='Stop',bg='#41B77E',padx=40,pady=20).pack(side=LEFT)
frame_2.pack(side=TOP)

tk.mainloop()