from dataclasses import dataclass
@dataclass
class Categoria:
    idCategoria:int
    categoria:str
    descripcion:str
    
@dataclass    
class Producto:
    idProducto:int
    idCategoria:int
    nombre:str
    descripcion:str
    precioVentaUnitario:float
    existencias:int
    
@dataclass
class Estado_Transaccion:
    idEstado:int
    estado:str
    descripcion:str
    
@dataclass    
class Cliente:
    nitCliente:str
    nombres:str
    apellidos:str
    direccion:str
    telefono:str
    saldoPorPagar:float
    
@dataclass    
class Sucursal:
    idSucursal:int
    idEmpleadoEncargado:int
    nombre:str
    direccion:str

@dataclass
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
    