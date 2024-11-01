from view.ventas import VentasVentana
from tkinter import *
from controller.CRUD.clientesCRUD import ClientesCRUD

root=Tk()
productosVentana = VentasVentana(root)
root.mainloop()
