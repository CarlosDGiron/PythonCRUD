import pyodbc

def sqlserverSessionCursor():
    
    server = 'localhost\SQLEXPRESS'  # Ejemplo: 'localhost\SQLEXPRESS'
    database = 'db_pdv'
    username = 'Produccion_Oper'
    password = 'Produccion_Oper'
    
    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        print("Conexión exitosa")
        return connection
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return False
