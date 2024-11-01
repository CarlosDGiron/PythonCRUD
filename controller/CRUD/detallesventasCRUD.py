import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Detalle_Venta as Detalle_Venta

class DetallesVentasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdDetalleVenta(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT MAX(IDDETALLEVENTA) 
            FROM DETALLES_VENTAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllDetallesVentas(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM DETALLES_VENTAS
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getDetalleVentaByIDDetalleVenta(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM DETALLES_VENTAS
            WHERE IDDETALLEVENTA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def getDetallesVentasByIDVenta(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM DETALLES_VENTAS
            WHERE IDVENTA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data
    
    def getTotalVentaByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT SUM(CANTIDAD * PRECIOVENTAUNITARIO) AS TOTAL_VENTA 
            FROM DETALLES_VENTAS
            WHERE IDVENTA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertDetalleVenta(self, detalleVenta: Detalle_Venta):
        try:
            data = False
            id = self.getMaxIdDetalleVenta() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO DETALLES_VENTAS (IDDETALLEVENTA, IDVENTA, IDPRODUCTO, CANTIDAD, PRECIOVENTAUNITARIO)
                VALUES ({id}, {detalleVenta.idVenta}, {detalleVenta.idProducto}, {detalleVenta.cantidad}, {detalleVenta.precioVentaUnitario})
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

    def deleteDetalleVenta(self, detalleVenta: Detalle_Venta):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM DETALLES_VENTAS WHERE IDDETALLEVENTA = {detalleVenta.idDetalleVenta}
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

    def updateDetalleVenta(self, detalleVenta: Detalle_Venta):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE DETALLES_VENTAS 
                SET IDVENTA = {detalleVenta.idVenta}, 
                    IDPRODUCTO = {detalleVenta.idProducto}, 
                    CANTIDAD = {detalleVenta.cantidad}, 
                    PRECIOVENTAUNITARIO = {detalleVenta.precioVentaUnitario}
                WHERE IDDETALLEVENTA = {detalleVenta.idDetalleVenta}
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
