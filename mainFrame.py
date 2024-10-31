from controller.estadosCRUD import EstadosCRUD
from model.pdvModels import Categoria

dbCRUD= EstadosCRUD()
categoria=dbCRUD.getEstadoByID(1)
print(categoria)
nombre=categoria[1]
#print(dbCRUD.getIDByCategoria(nombre))