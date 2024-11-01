import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Producto as Producto

class ProductosCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
     
    def getMaxIdProducto(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql='''
            SELECT MAX(IDPRODUCTO) 
            FROM PRODUCTOS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllProductos(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql='''
            SELECT * 
            FROM PRODUCTOS
            ORDER BY IDPRODUCTO ASC
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getProductoByID(self, id:int):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql=f'''
            SELECT * 
            FROM PRODUCTOS
            WHERE IDPRODUCTO={id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def insertProducto(self, producto:Producto):
        try:
            data=False
            id=self.getMaxIdProducto()+1
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                INSERT INTO PRODUCTOS (IDPRODUCTO, IDCATEGORIA, NOMBRE, DESCRIPCION, PRECIOVENTAUNITARIO, EXISTENCIAS)
                VALUES ({id}, {producto.idCategoria}, '{producto.nombre}', '{producto.descripcion}', {producto.precioVentaUnitario}, {producto.existencias})
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data
        
    def deleteProducto(self, producto:Producto):
        try:
            data=False
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                DELETE FROM PRODUCTOS WHERE IDPRODUCTO={producto.idProducto}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data

    def updateProducto(self, producto:Producto):
        try:
            data=False
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                UPDATE FROM PRODUCTOS 
                SET  IDCATEGORIA={producto.idCategoria}, 
                NOMBRE='{producto.nombre}', 
                DESCRIPCION='{producto.descripcion}', 
                PRECIOVENTAUNITARIO={producto.precioVentaUnitario}, 
                EXISTENCIAS={producto.existencias}, 
                WHERE IDPRODUCTO={producto.idProducto}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data
