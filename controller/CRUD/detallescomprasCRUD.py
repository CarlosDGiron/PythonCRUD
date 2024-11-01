import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Detalle_Compra as Detalles_Compras

class DetallesComprasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdDetalleCompra(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT MAX(IDDETALLECOMPRA) 
            FROM DETALLES_COMPRAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllDetallesCompras(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM DETALLES_COMPRAS
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getDetalleCompraByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM DETALLES_COMPRAS
            WHERE IDDETALLECOMPRA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def getDetallesComprasByIDCompra(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM DETALLES_COMPRAS
            WHERE IDCOMPRA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data
        
    def getTotalCompraByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT SUM(CANTIDAD * PRECIOCOMPRAUNITARIO) AS TOTAL_COMPRA 
            FROM DETALLES_COMPRAS
            WHERE IDCOMPRA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertDetalleCompra(self, detalleCompra: Detalles_Compras):
        try:
            data = False
            id = self.getMaxIdDetalleCompra() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO DETALLES_COMPRAS (IDDETALLECOMPRA, IDCOMPRA, IDPRODUCTO, CANTIDAD, PRECIOCOMPRAUNITARIO)
                VALUES ({id}, {detalleCompra.idCompra}, {detalleCompra.idProducto}, {detalleCompra.cantidad}, {detalleCompra.precioCompraUnitario})
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close()
            data = True
        finally:
            return data

    def deleteDetalleCompra(self, detalleCompra: Detalles_Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM DETALLES_COMPRAS WHERE IDDETALLECOMPRA = {detalleCompra.idDetalleCompra}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close()
            data = True
        finally:
            return data

    def updateDetalleCompra(self, detalleCompra: Detalles_Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE DETALLES_COMPRAS 
                SET IDCOMPRA = {detalleCompra.idCompra}, 
                    IDPRODUCTO = {detalleCompra.idProducto}, 
                    CANTIDAD = {detalleCompra.cantidad}, 
                    PRECIOCOMPRAUNITARIO = {detalleCompra.precioCompraUnitario}
                WHERE IDDETALLECOMPRA = {detalleCompra.idDetalleCompra}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close()
            data = True
        finally:
            return data
