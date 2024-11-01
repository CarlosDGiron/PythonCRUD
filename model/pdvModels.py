from dataclasses import dataclass
from datetime import datetime

@dataclass
class Categoria:
    idCategoria:int = 0
    categoria:str = ""
    descripcion:str = ""
    
    def set(self,list:tuple):
        self.idCategoria=list[0]
        self.categoria=list[1]
        self.descripcion=list[2]
        
@dataclass    
class Producto:
    idProducto:int = 0
    idCategoria:int = 0
    nombre:str = ""
    descripcion:str = ""
    precioVentaUnitario:float = 0.0
    existencias:int = 0
    
    def set(self,list:tuple):
        self.idProducto=list[0]
        self.idCategoria=list[1]
        self.nombre=list[2]
        self.descripcion=list[3]
        self.precioVentaUnitario=list[4]
        self.existencias=list[5]
            
@dataclass
class Estado_Transaccion:
    idEstado:int = 0
    estado:str = ""
    descripcion:str = ""
    
    def set(self,list:tuple):
        self.idEstado=list[0]
        self.estado=list[1]
        self.descripcion=list[2]
    
@dataclass    
class Cliente:
    nitCliente:str = ""
    nombres:str = ""
    apellidos:str = ""
    direccion:str = ""
    telefono:str = ""
    saldoPorPagar:float = 0.0
    
    def set(self,list:tuple):
        self.nitCliente=list[0]
        self.nombres=list[1]
        self.apellidos=list[2]
        self.direccion=list[3]
        self.telefono=list[4]
        self.saldoPorPagar=list[5]
    
@dataclass    
class Sucursal:
    idSucursal:int = 0
    idEmpleadoEncargado:int = 0
    nombre:str = ""
    direccion:str = ""
    
    def set(self,list:tuple):
        self.idSucursal=list[0]
        self.idEmpleadoEncargado=list[1]
        self.nombre=list[2]
        self.direccion=list[3]
        

@dataclass
class Forma_de_Pago:
    idFormaDePago:int = 0
    formaDePago:str = ""
    
    def set(self,list:tuple):
        self.idFormaDePago=list[0]
        self.formaDePago=list[1]
    
    
@dataclass
class Venta:
    idVenta: int = 0
    idSucursal: int = 0
    idEstado:int = 0
    idEmpleado:int = 0
    nitCliente: str = ""
    idFormaDePago:int = 0
    serie:str = ""
    factura:str = ""
    fechahora:str = ""
    anioventa:int = 0
    mesventa:int = 0
    documentoPago:str = ""
    totalVenta:float=0.0
    
    def getFormatedDate(self):    
        return self.fechahora.strftime("%d/%m/%Y %H:%M:%S")
    
    def set(self,list:tuple):
        self.idVenta=list[0]
        self.idSucursal=list[1]
        self.idEstado=list[2]
        self.idEmpleado=list[3]
        self.nitCliente=list[4]
        self.idFormaDePago=list[11]
        self.serie=list[5]
        self.factura=list[6]
        self.fechahora=list[7]
        self.anioventa=list[8]
        self.mesventa=list[9]
        self.documentoPago=list[10]
        self.totalVenta=list[11]
    
@dataclass
class Detalle_Venta:
    idDetalleVenta: int = 0
    idVenta: int = 0
    idProducto:int = 0
    cantidad:int = 0
    precioVentaUnitario:float = 0.0
    
    def set(self,list:tuple):
        self.idDetalleVenta=list[0]
        self.idVenta=list[1]
        self.idProducto=list[2]
        self.cantidad=list[3]
        self.precioVentaUnitario=list[4]

@dataclass    
class Proveedor:
    nit:str = ""
    nombreFiscal:str = ""
    direccion:str = ""
    telefono:str = ""
    saldoPorPagar:float = 0.0
    email:str = ""
    
    def set(self,list:tuple):
        self.nit=list[0]
        self.nombreFiscal=list[1]
        self.direccion=list[2]
        self.telefono=list[3]
        self.saldoPorPagar=list[4]
        self.email=list[5]

@dataclass
class Compra:
    idCompra: int = 0
    idSucursal: int = 0
    idEstado:int = 0
    nitProveedor: str = ""
    idFormaDePago:int = 0
    factura:str = ""
    fechahora:str = ""
    anioventa:int = 0
    mesventa:int = 0
    documentoPago:str = ""
    totalCompra:float = 0.0
    
    
    def getFormatedDate(self):    
        return self.fechahora.strftime("%d/%m/%Y %H:%M:%S")
    
    def set(self,list:tuple):
        self.idCompra=list[0]
        self.idSucursal=list[1]
        self.nitProveedor=list[2]
        self.idEstado=list[3]
        self.fechahora=list[4]
        self.anioventa=list[5]
        self.mesventa=list[6]
        self.factura=list[7]
        self.documentoPago=list[8]
        self.idFormaDePago=list[9]
        self.totalCompra=list[10]
    
@dataclass
class Detalle_Compra:
    idDetalleCompra: int = 0
    idCompra: int = 0
    idProducto:int = 0
    cantidad:int = 0
    precioCompraUnitario:float = 0.0
    
    def set(self,list:tuple):
        self.idDetalleCompra=list[0]
        self.idCompra=list[1]
        self.idProducto=list[2]
        self.cantidad=list[3]
        self.precioCompraUnitario=list[4]

@dataclass
class Modificacion_Compra:
    idModificacion: int = 0
    idCompra:int = 0
    idCompraNueva: int = 0
    idEstado:int = 0
    fechaHoraModificacion:str = ""
    anioModificacion:int = 0
    mesModificacion:int = 0
    
    def set(self,list:tuple):
        self.idModificacion=list[0]
        self.idCompra=list[1]
        self.idCompraNueva=list[2]
        self.idEstado=list[3]
        self.fechaHoraModificacion=list[4]
        self.anioModificacion=list[5]
        self.mesModificacion=list[6]
    
@dataclass
class Modificacion_Venta:
    idModificacion: int = 0
    idVenta: int = 0
    idVentaNueva:int = 0
    idEstado:int = 0
    fechaHoraModificacion:str = ""
    anioModificacion:int = 0
    mesModificacion:int = 0
    
    def set(self,list:tuple):
        self.idModificacion=list[0]
        self.idVenta=list[1]
        self.idVentaNueva=list[2]
        self.idEstado=list[3]
        self.fechaHoraModificacion=list[4]
        self.anioModificacion=list[5]
        self.mesModificacion=list[6]
