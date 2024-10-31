from controller.detallesventasCRUD import DetallesVentasCRUD
from model.pdvModels import Categoria

dbCRUD= DetallesVentasCRUD()
categoria=dbCRUD.getDetallesVentasByIDVenta(23)
print(categoria)
nombre=categoria[1]
#print(dbCRUD.getIDByCategoria(nombre))