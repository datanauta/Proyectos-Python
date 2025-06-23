import tkinter as tk
from tkcalendar import Calendar

def print_date():
    print(cal.selection_get())

root = tk.Tk()

root.title('Calendario interactivo')

cal = Calendar(root, selectmode='day', year=2025, month= 5, day=16)
cal.pack(pady=20)
tk.Button(root,text='Seleccionar fecha',command=print_date).pack(pady=20)

root.mainloop()



