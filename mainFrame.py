from controller.CRUD.proveedoresCRUD import ProveedoresCRUD
from model.pdvModels import Proveedor
import datetime

dbCRUD= ProveedoresCRUD()
data=dbCRUD.getProveedorByNIT('P0001')
print(data)
nombre=Proveedor()
nombre.set(data)
print (nombre)
