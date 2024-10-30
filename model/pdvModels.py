from dataclasses import dataclass
@dataclass

class Categoria:
    idCategoria:int
    categoria:str
    descripcion:str
    
class Producto:
    idProductos:int
    idCategoria:int
    nombre:str
    descripcion:str
    precioVentaUnitario:float
    existencias:int

class Estado_Transaccion:
    idEstado:int
    estado:str
    descripcion:str
    
class Cliente:
    nitCliente:str
    nombres:str
    apellidos:str
    direccion:str
    telefono:str
    saldoPorPagar:float
    
class Sucursal:
    idSucursal:int
    idEmpleadoEncargado:int
    nombre:str
    direccion:str

class Venta:
    idVenta: int
    idSucursal: int
    idEstado:int
    idEmpleado:int
    nitCliente: str
    serie:str
    factura:str
    fechahora:str
    anioventa:int
    mesventa:int
    documentoPago:str
    