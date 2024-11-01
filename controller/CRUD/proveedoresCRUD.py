import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Proveedor as Proveedores

class ProveedoresCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getAllProveedores(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM PROVEEDORES
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def getProveedorByNIT(self, nit: str):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM PROVEEDORES
            WHERE NIT = '{nit}'
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertProveedor(self, proveedor: Proveedores):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO PROVEEDORES (NIT, NOMBREFISCAL, DIRECCION, TELEFONO, SALDOPORPAGAR, EMAIL)
                VALUES ('{proveedor.nit}', '{proveedor.nombreFiscal}', '{proveedor.direccion}', '{proveedor.telefono}', {proveedor.saldoPorPagar}, '{proveedor.email}')
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

    def deleteProveedor(self, proveedor: Proveedores):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM PROVEEDORES WHERE NIT = '{proveedor.nit}'
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

    def updateProveedor(self, proveedor: Proveedores):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE PROVEEDORES 
                SET NOMBREFISCAL = '{proveedor.nombreFiscal}', 
                    DIRECCION = '{proveedor.direccion}', 
                    TELEFONO = '{proveedor.telefono}', 
                    SALDOPORPAGAR = {proveedor.saldoPorPagar}, 
                    EMAIL = '{proveedor.email}' 
                WHERE NIT = '{proveedor.nit}'
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
