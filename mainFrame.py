from view.ventas import VentasVentana
from tkinter import *
from controller.sqlserverConnection import sqlserverSessionCursor
from controller.CRUD.clientesCRUD import ClientesCRUD

#root=Tk()
#productosVentana = VentasVentana(root)
#root.mainloop()
sql=sqlserverSessionCursor()
data=sql.execute("SELECT * FROM Usuarios")
print(data.fetchall())
