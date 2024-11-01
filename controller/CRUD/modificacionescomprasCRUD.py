import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Modificacion_Compra as Modificaciones_Compras

class ModificacionesComprasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdModificacionCompra(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT MAX(IDMODIFICACION) 
            FROM MODIFICACIONES_COMPRAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllModificacionesCompras(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM MODIFICACIONES_COMPRAS
            ORDER BY IDMODIFICACION ASC
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getModificacionCompraByIDModificacion(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM MODIFICACIONES_COMPRAS
            WHERE IDMODIFICACION = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def getModificacionCompraByIDCompra(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM MODIFICACIONES_COMPRAS
            WHERE IDCOMPRA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertModificacionCompra(self, modificacionCompra: Modificaciones_Compras):
        try:
            data = False
            id = self.getMaxIdModificacionCompra() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO MODIFICACIONES_COMPRAS (IDMODIFICACION, IDCOMPRA, IDCOMPRANUEVA, IDESTADO, FECHAHORAMODIFICACION, ANIOMODIFICACION, MESMODIFICACION)
                VALUES ({id}, {modificacionCompra.idCompra}, {modificacionCompra.idCompraNueva}, {modificacionCompra.idEstado}, '{modificacionCompra.fechaHoraModificacion}', {modificacionCompra.anioModificacion}, {modificacionCompra.mesModificacion})
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

    def deleteModificacionCompra(self, modificacionCompra: Modificaciones_Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM MODIFICACIONES_COMPRAS WHERE IDMODIFICACION = {modificacionCompra.idModificacion}
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

    def updateModificacionCompra(self, modificacionCompra: Modificaciones_Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE MODIFICACIONES_COMPRAS 
                SET IDCOMPRA = {modificacionCompra.idCompra}, 
                    IDCOMPRANUEVA = {modificacionCompra.idCompraNueva}, 
                    IDESTADO = {modificacionCompra.idEstado}, 
                    FECHAHORAMODIFICACION = '{modificacionCompra.fechaHoraModificacion}', 
                    ANIOMODIFICACION = {modificacionCompra.anioModificacion}, 
                    MESMODIFICACION = {modificacionCompra.mesModificacion}
                WHERE IDMODIFICACION = {modificacionCompra.idModificacion}
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
