from customtkinter import *

app = CTk()
app.geometry("400x400")

btn = CTkButton(master=app, text="Hola", corner_radius=10)

btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()