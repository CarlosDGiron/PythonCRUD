import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Forma_de_Pago as Forma_de_Pago

class FormaDePagoCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdFormaDePago(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT MAX(IDFORMADEPAGO) 
            FROM PDV.FORMA_DE_PAGO
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllFormasDePago(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT * 
            FROM PDV.FORMA_DE_PAGO
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getFormaDePagoByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM PDV.FORMA_DE_PAGO
            WHERE IDFORMADEPAGO = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def insertFormaDePago(self, formaDePago: Forma_de_Pago):
        try:
            data = False
            id = self.getMaxIdFormaDePago() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO PDV.FORMA_DE_PAGO (IDFORMADEPAGO, FORMADEPAGO)
                VALUES ({id}, '{formaDePago.FormaDePago}')
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

    def deleteFormaDePago(self, formaDePago: Forma_de_Pago):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM PDV.FORMA_DE_PAGO WHERE IDFORMADEPAGO = {formaDePago.idFormaDePago}
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

    def updateFormaDePago(self, formaDePago: Forma_de_Pago):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE PDV.FORMA_DE_PAGO 
                SET FORMADEPAGO = '{formaDePago.FormaDePago}'
                WHERE IDFORMADEPAGO = {formaDePago.idFormaDePago}
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
