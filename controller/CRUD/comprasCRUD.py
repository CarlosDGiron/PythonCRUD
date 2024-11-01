import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Compra as Compras

class ComprasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdCompra(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT MAX(IDCOMPRA) 
            FROM COMPRAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllCompras(self):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = '''
            SELECT * 
            FROM COMPRAS
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getCompraByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM COMPRAS
            WHERE IDCOMPRA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertCompra(self, compra: Compras):
        try:
            data = False
            id = self.getMaxIdCompra() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO COMPRAS (IDCOMPRA, IDSUCURSAL, IDESTADO,  NITPROVEEDOR, IDFORMADEPAGO, FACTURA, FECHAHORA, ANIOVENTA, MESVENTA, DOCUMENTOPAGO)
                VALUES ({id}, {compra.idSucursal}, {compra.idEstado}, '{compra.nitProveedor}', {compra.idFormaDePago}, '{compra.factura}', '{compra.fechahora}', {compra.anioventa}, {compra.mesventa}, '{compra.documentoPago}')
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

    def deleteCompra(self, compra: Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM COMPRAS WHERE IDCOMPRA = {compra.idCompra}
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

    def updateCompra(self, compra: Compras):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE COMPRAS 
                SET IDSUCURSAL = {compra.idSucursal}, 
                    IDESTADO = {compra.idEstado},                     
                    NITPROVEEDOR = '{compra.nitProveedor}', 
                    IDFORMADEPAGO = {compra.idFormaDePago}, 
                    FACTURA = '{compra.factura}', 
                    FECHAHORA = '{compra.fechahora}', 
                    ANIOVENTA = {compra.anioventa}, 
                    MESVENTA = {compra.mesventa}, 
                    DOCUMENTOPAGO = '{compra.documentoPago}'
                WHERE IDCOMPRA = {compra.idCompra}
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
