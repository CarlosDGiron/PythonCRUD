from controller.CRUD.estadosCRUD import EstadosCRUD
from controller.CRUD.categoriasCRUD import CategoriasCRUD
from controller.CRUD.formadepagoCRUD import FormaDePagoCRUD
from controller.CRUD.productosCRUD import ProductosCRUD     
from controller.CRUD.sucursalesCRUD import SucursalesCRUD
from controller.CRUD.clientesCRUD import ClientesCRUD

def obtener_diccionario_clientes():
    clientes_crud = ClientesCRUD()
    clientes = clientes_crud.getAllClientes()
    
    diccionario_clientes = {}
    for cliente in clientes:
        diccionario_clientes[cliente[0]] = {
            "nombres": cliente[1]+" "+cliente[2],            
            "direccion": cliente[3],
            "telefono": cliente[4],
            "saldoPorPagar": cliente[5]
        }
    
    return diccionario_clientes


def obtener_diccionario_sucursales():
    sucursales_crud = SucursalesCRUD()
    sucursales = sucursales_crud.getAllSucursales()
    
    diccionario_sucursales = {}
    for sucursal in sucursales:
        diccionario_sucursales[sucursal[0]] = {
            "idEmpleadoEncargado": sucursal[1],
            "nombre": sucursal[2],
            "direccion": sucursal[3]
        }
    
    return diccionario_sucursales


def obtener_diccionario_estados():
    estado_crud = EstadosCRUD()
    estados = estado_crud.getAllEstados()
    diccionario_estados = {}
    for estado in estados:
        diccionario_estados[estado[0]] = {
            "estado": estado[1],
            "descripcion": estado[2]
        }        
    return diccionario_estados

def obtener_diccionario_categorias():
    categorias_crud = CategoriasCRUD()
    categorias = categorias_crud.getAllCategorias()        
    diccionario_categorias = {}
    for categoria in categorias:
        diccionario_categorias[categoria[0]] = {
            "categoria": categoria[1],
            "descripcion": categoria[2]
        }        
    return diccionario_categorias

def obtener_diccionario_formas_de_pago():
    forma_de_pago_crud = FormaDePagoCRUD()
    formas_de_pago = forma_de_pago_crud.getAllFormasDePago()        
    diccionario_formas_de_pago = {}
    for forma in formas_de_pago:
        diccionario_formas_de_pago[forma[0]] = {
            "forma_de_pago": forma[1]
        }        
    return diccionario_formas_de_pago

def obtener_diccionario_productos():
    productos_crud = ProductosCRUD()
    productos = productos_crud.getAllProductos()        
    diccionario_productos = {}
    for producto in productos:
        diccionario_productos[producto[0]] = {
            "idCategoria": producto[1],
            "nombre": producto[2],
            "descripcion": producto[3],
            "precioVentaUnitario": producto[4],
            "existencias": producto[5]
        }        
    return diccionario_productos