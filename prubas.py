from productos import ProductosFrame
from controller.CRUD.productosCRUD import ProductosCRUD
from model.pdvModels import Producto
from view.ventas import VentasVentana
from tkinter import *

root=Tk()
ventana=VentasVentana(root)
root.mainloop()
# root=Tk()
# root.title("SAE/SAP Login")
# root.resizable(False,False)
# root.config(bg="Gray")

# frame=ProductosFrame(root)
# frame.pack()

# root.mainloop()
