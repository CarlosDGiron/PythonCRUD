from controller.productosDBCRUD import ProductosCRUD
from model.pdvModels import Producto

dbCRUD= ProductosCRUD()

producto=Producto(idProductos=0,idCategoria=1,nombre="Producto Prueba", descripcion="Producto de Prueba", precioVentaUnitario=10, existencias=110)

print(dbCRUD.insertProducto(producto=producto))