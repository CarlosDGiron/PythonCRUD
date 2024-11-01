import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Estado_Transaccion as Estado

class EstadosCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
     
    def getMaxIdEstado(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql='''
            SELECT MAX(IDESTADO) 
            FROM ESTADOS_TRANSACCIONES
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllEstados(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql='''
            SELECT * 
            FROM ESTADOS_TRANSACCIONES
        '''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getEstadoByID(self, id:int):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql=f'''
            SELECT * 
            FROM ESTADOS_TRANSACCIONES
            WHERE IDESTADO={id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def insertEstado(self, estado:Estado):
        try:
            data=False
            id=self.getMaxIdEstado()+1
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                INSERT INTO ESTADOS_TRANSACCIONES (IDESTADO, ESTADO, DESCRIPCION)
                VALUES ({id},
                {estado.estado},
                '{estado.descripcion}')
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data
        
    def deleteEstado(self, estado:Estado):
        try:
            data=False
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                DELETE FROM ESTADOS_TRANSACCIONES WHERE IDESTADO={estado.idEstado}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data

    def updateEstado(self, estado:Estado):
        try:
            data=False
            if(self.db._verify_open):            
                self.db=self.connectSession()
            sql=f'''
                UPDATE FROM ESTADOS_TRANSACCIONES 
                SET  ESTADO='{estado.estado}', 
                DESCRIPCION='{estado.descripcion}'
                WHERE IDESTADO={estado.idEstado}
            '''
            self.db.execute(sql)
            self.db.connection.commit()
        except Error as error:
            print(error)
        except Exception as exception:
            print(exception)
        else:            
            self.db.close
            data=True
        finally:
            return data
