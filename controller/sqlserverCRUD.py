import pyodbc
import hashlib
import controller.sqlserverConnection as sqlserverConnection

def validarCredenciales(username, password):
    try:
        connection=sqlserverConnection.sqlserverSessionCursor()    
        cursor=connection.cursor()
        sql=f'''SELECT idUsuarios FROM Usuarios WHERE usuario ='{username}' AND passwordHash=HASHBYTES('SHA2_512', '{password}')'''
        #print (sql)
        cursor.execute(sql)
        row = cursor.fetchone()
        
        if row is None:
            print("Credenciales invalidas")
            return -1

        else:
            print("Credenciales validas")
            return row[0]

    except pyodbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        return False
    finally:
        # Cerrar la conexión
        if not connection.closed:
            cursor.close()
            connection.close()

def getPermisos(idUsuario):
    try:
        connection=sqlserverConnection.sqlserverSessionCursor()    
        cursor=connection.cursor()
        sql = '''SELECT M.IDMENU,S.IDSUBMENU, M.NOMBRE, S.NOMBRE 
        FROM SUBMENUS S
        JOIN MENUS M ON S.IDMENU=M.IDMENU
        JOIN USUARIOS U ON U.IDUSUARIOS=?
        JOIN ROLES R ON R.IDROL=U.IDROL
        JOIN PERMISOS P ON P.IDROL=U.IDROL
        WHERE P.IDSUBMENU=S.IDSUBMENU
        '''
        #print (sql)
        cursor.execute(sql,(idUsuario,))
        row = cursor.fetchall()        
        return row

    except pyodbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        return False
    finally:
        if not connection.closed:
            cursor.close()
            connection.close()
