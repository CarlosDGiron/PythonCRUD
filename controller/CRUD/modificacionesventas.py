import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Modificacion_Venta as Modificaciones_Ventas

class ModificacionesVentasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdModificacionVenta(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT MAX(IDMODIFICACION) 
            FROM MODIFICACIONES_VENTAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllModificacionesVentas(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM MODIFICACIONES_VENTAS
            ORDER BY IDMODIFICACION ASC
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getModificacionVentaByIDModificacion(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM MODIFICACIONES_VENTAS
            WHERE IDMODIFICACION = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def getModificacionVentaByIDVenta(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM MODIFICACIONES_VENTAS
            WHERE IDVENTA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertModificacionVenta(self, modificacionVenta: Modificaciones_Ventas):
        try:
            data = False
            id = self.getMaxIdModificacionVenta() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO MODIFICACIONES_VENTAS (IDMODIFICACION, IDCOMPRA, IDCOMPRANUEVA, IDESTADO, FECHAHORAMODIFICACION, ANIOMODIFICACION, MESMODIFICACION)
                VALUES ({id}, {modificacionVenta.idCompra}, {modificacionVenta.idCompraNueva}, {modificacionVenta.idEstado}, '{modificacionVenta.fechaHoraModificacion}', {modificacionVenta.anioModificacion}, {modificacionVenta.mesModificacion})
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

    def deleteModificacionVenta(self, modificacionVenta: Modificaciones_Ventas):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM MODIFICACIONES_VENTAS WHERE IDMODIFICACION = {modificacionVenta.idModificacion}
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

    def updateModificacionVenta(self, modificacionVenta: Modificaciones_Ventas):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE MODIFICACIONES_VENTAS 
                SET IDCOMPRA = {modificacionVenta.idCompra}, 
                    IDCOMPRANUEVA = {modificacionVenta.idCompraNueva}, 
                    IDESTADO = {modificacionVenta.idEstado}, 
                    FECHAHORAMODIFICACION = '{modificacionVenta.fechaHoraModificacion}', 
                    ANIOMODIFICACION = {modificacionVenta.anioModificacion}, 
                    MESMODIFICACION = {modificacionVenta.mesModificacion}
                WHERE IDMODIFICACION = {modificacionVenta.idModificacion}
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
