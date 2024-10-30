from controller.productosDBCRUD import ProductosCRUD

dbCRUD= ProductosCRUD()

print(dbCRUD.getProductoByID(1))
print(dbCRUD.getProductoByID(2))
