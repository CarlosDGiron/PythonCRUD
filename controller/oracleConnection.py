import oracledb

def oracleSessionCursor():
    oracleConnection = oracledb.connect(
        user="PDV_CRUD",
        password="PDV_CRUD",
        dsn="localhost/xe"
    )

    cursor=oracleConnection.cursor()
    return cursor   