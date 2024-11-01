import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Sucursal as Sucursal

class SucursalesCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdSucursal(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT MAX(IDSUCURSAL) 
            FROM SUCURSALES
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllSucursales(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT * 
            FROM SUCURSALES
            ORDER BY IDSUCURSAL ASC
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getSucursalByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM SUCURSALES
            WHERE IDSUCURSAL = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def insertSucursal(self, sucursal: Sucursal):
        try:
            data = False
            id = self.getMaxIdSucursal() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO SUCURSALES (IDSUCURSAL, IDEMPLEADOENCARGADO, NOMBRE, DIRECCION)
                VALUES ({id}, {sucursal.idEmpleadoEncargado}, '{sucursal.nombre}', '{sucursal.direccion}')
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

    def deleteSucursal(self, sucursal: Sucursal):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM SUCURSALES WHERE IDSUCURSAL = {sucursal.idSucursal}
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

    def updateSucursal(self, sucursal: Sucursal):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE SUCURSALES 
                SET IDEMPLEADOENCARGADO = {sucursal.idEmpleadoEncargado}, 
                    NOMBRE = '{sucursal.nombre}', 
                    DIRECCION = '{sucursal.direccion}' 
                WHERE IDSUCURSAL = {sucursal.idSucursal}
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
