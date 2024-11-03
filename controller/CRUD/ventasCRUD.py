import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Venta as Venta
from  controller.CRUD.detallesventasCRUD import DetallesVentasCRUD

class VentasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdVenta(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT MAX(IDVENTA) 
            FROM VENTAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllVentas(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT * 
            FROM VENTAS
            ORDER BY IDVENTA ASC
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data
           
    def getVentaByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM VENTAS
            WHERE IDVENTA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data

    def insertVenta(self, venta: Venta):
        try:
            data = False
            id = self.getMaxIdVenta() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO VENTAS (IDVENTA, IDSUCURSAL, IDESTADO, IDEMPLEADO, NITCLIENTE, IDFORMADEPAGO, SERIE, FACTURA, FECHAHORA, ANIOVENTA, MESVENTA, DOCUMENTOPAGO)
                VALUES ({id}, {venta.idSucursal}, {venta.idEstado}, {venta.idEmpleado}, '{venta.nitCliente}', {venta.idFormaDePago}, '{venta.serie}', '{venta.factura}', TO_DATE('{venta.fechahora}', 'yyyy-mm-dd hh24:mi:ss'), {venta.anioventa}, {venta.mesventa}, '{venta.documentoPago}')
            '''
            print (sql)
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

    def deleteVenta(self, venta: Venta):
        try:
            data = False
            detalleVenta=DetallesVentasCRUD()
            data=detalleVenta.deleteDetalleVentaByIdVenta(venta.idVenta)
            if data:
                data=False
                if(self.db._verify_open):            
                    self.db = self.connectSession()
                sql = f'''
                    DELETE FROM VENTAS WHERE IDVENTA = {venta.idVenta}
                '''
                print (sql)
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

    def updateVenta(self, venta: Venta):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE VENTAS 
                SET IDSUCURSAL = {venta.idSucursal}, 
                    IDESTADO = {venta.idEstado}, 
                    IDEMPLEADO = {venta.idEmpleado}, 
                    NITCLIENTE = '{venta.nitCliente}', 
                    IDFORMADEPAGO = {venta.idFormaDePago}, 
                    SERIE = '{venta.serie}', 
                    FACTURA = '{venta.factura}', 
                    FECHAHORA = TO_DATE('{venta.fechahora}', 'yyyy-mm-dd hh24:mi:ss'), 
                    ANIOVENTA = {venta.anioventa}, 
                    MESVENTA = {venta.mesventa}, 
                    DOCUMENTOPAGO = '{venta.documentoPago}'
                WHERE IDVENTA = {venta.idVenta}
            '''
            print (sql)
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