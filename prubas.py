from productos import ProductosFrame
from controller.CRUD.productosCRUD import ProductosCRUD
from model.pdvModels import Producto
from view.ventas import VentasFrame
from login import *
from tkinter import *
from model.diccionarios import obtener_diccionario_formas_de_pago   

dic=obtener_diccionario_formas_de_pago()
print (dic.values())