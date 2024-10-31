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
class Forma_de_Pago:
    idFormaDePago:int
    FormaDePago:str
    
@dataclass
class Venta:
    idVenta: int
    idSucursal: int
    idEstado:int
    idEmpleado:int
    nitCliente: str
    idFormaDePago:int
    serie:str
    factura:str
    fechahora:str
    anioventa:int
    mesventa:int
    documentoPago:str
    
@dataclass
class Detalle_Venta:
    idDetalleVenta: int
    idVenta: int
    idProducto:int
    cantidad:int
    precioVentaUnitario:float

@dataclass    
class Proveedor:
    nit:str
    nombreFiscal:str
    direccion:str
    telefono:str
    saldoPorPagar:float
    email:str

@dataclass
class Compra:
    idCompra: int
    idSucursal: int
    idEstado:int
    idEmpleado:int
    nitProveedor: str
    idFormaDePago:int
    factura:str
    fechahora:str
    anioventa:int
    mesventa:int
    documentoPago:str
    
@dataclass
class Detalle_Compra:
    idDetalleCompra: int
    idCompra: int
    idProducto:int
    cantidad:int
    precioCompraUnitario:float

@dataclass
class Modificacion_Compra:
    idModificacion: int
    idCompra:int
    idCompraNueva: int
    idEstado:int
    fechaHoraModificacion:str
    anioModificacion:int
    mesModificacion:int
    
@dataclass
class Modificacion_Venta:
    idModificacion: int
    idCompra: int
    idCompraNueva:int
    idEstado:int
    fechaHoraModificacion:str
    anioModificacion:int
    mesModificacion:int
