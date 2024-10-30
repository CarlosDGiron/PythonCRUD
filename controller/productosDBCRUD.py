import controller.oracleConnection as oracleConnection
from model.pdvModels import Producto as Producto

class ProductosCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def getAllProductos(self):
        sql='''
            SELECT * 
            FROM PDV.PRODUCTOS
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getProductoByID(self, id:int):
        sql=f'''
            SELECT * 
            FROM PDV.PRODUCTOS
            WHERE IDPRODUCTO={id}
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data
    
    def inserProducto(self, producto:Producto):
        sql=f'''
            INSERT INTO PDV.PRODUCTOS (IDCATEGORIA,NOMBRE,DESCRIPCION,PRECIOVENTAUNITARIO,EXISTENCIAS)
            VALUES ({producto.idCategoria}, '{producto.nombre}', '{producto.descripcion}', {producto.precioVentaUnitario}, {producto.existencias})
        '''
        self.db.execute(sql)
        data=self.db.fetchall
        self.db.close
        return data

