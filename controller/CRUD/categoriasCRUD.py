import controller.oracleConnection as oracleConnection
from oracledb import *
from model.pdvModels import Categoria as Categoria

class CategoriasCRUD:
    
    def __init__(self):
        self.db = oracleConnection.oracleSessionCursor()
        
    def connectSession(self):
        return oracleConnection.oracleSessionCursor()
    
    def getMaxIdCategoria(self):
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''
            SELECT MAX(IDCATEGORIA) 
            FROM CATEGORIAS
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def getAllCategorias(self):
        print(self.db._verify_open)
        if(self.db._verify_open):            
            self.db=self.connectSession()
        sql = '''SELECT * FROM CATEGORIAS 
        ORDER BY IDCATEGORIA ASC'''
        self.db.execute(sql)
        data = self.db.fetchall()
        self.db.close()
        return data

    def getCategoriaByID(self, id: int):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT * 
            FROM CATEGORIAS
            WHERE IDCATEGORIA = {id}
        '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data
    
    def getIDByCategoria(self, categoria:str):
        if(self.db._verify_open):            
            self.db = self.connectSession()
        sql = f'''
            SELECT IDCATEGORIA 
            FROM CATEGORIAS
            WHERE CATEGORIA ='{categoria}'
            '''
        self.db.execute(sql)
        data = self.db.fetchone()
        self.db.close()
        return data[0]
    
    def insertCategoria(self, categoria: Categoria):
        try:
            data = False
            id = self.getMaxIdCategoria() + 1
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                INSERT INTO CATEGORIAS (IDCATEGORIA, CATEGORIA, DESCRIPCION)
                VALUES ({id}, '{categoria.categoria}', '{categoria.descripcion}')
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

    def deleteCategoria(self, categoria: Categoria):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                DELETE FROM CATEGORIAS WHERE IDCATEGORIA = {categoria.idCategoria}
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

    def updateCategoria(self, categoria: Categoria):
        try:
            data = False
            if(self.db._verify_open):            
                self.db = self.connectSession()
            sql = f'''
                UPDATE CATEGORIAS 
                SET CATEGORIA = '{categoria.categoria}', 
                DESCRIPCION = '{categoria.descripcion}' 
                WHERE IDCATEGORIA = {categoria.idCategoria}
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
