import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Cliente as Cliente

class ClientesCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getAllClientes(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT * 
            FROM PDV.CLIENTES
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getClienteByNIT(self, nit: str):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM PDV.CLIENTES
            WHERE NITCLIENTE = '{nit}'
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def insertCliente(self, cliente: Cliente):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO PDV.CLIENTES (NITCLIENTE, NOMBRES, APELLIDOS, DIRECCION, TELEFONO, SALDOPORPAGAR)
                VALUES ('{cliente.nitCliente}', '{cliente.nombres}', '{cliente.apellidos}', '{cliente.direccion}', '{cliente.telefono}', {cliente.saldoPorPagar})
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

    def deleteCliente(self, cliente: Cliente):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM PDV.CLIENTES WHERE NITCLIENTE = '{cliente.nitCliente}'
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

    def updateCliente(self, cliente: Cliente):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE PDV.CLIENTES 
                SET NOMBRES = '{cliente.nombres}', 
                    APELLIDOS = '{cliente.apellidos}', 
                    DIRECCION = '{cliente.direccion}', 
                    TELEFONO = '{cliente.telefono}', 
                    SALDOPORPAGAR = {cliente.saldoPorPagar} 
                WHERE NITCLIENTE = '{cliente.nitCliente}'
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
