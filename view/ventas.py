import tkinter as tk
from tkinter import ttk, messagebox
from controller.CRUD.ventasCRUD import VentasCRUD  # Importa el CRUD de Ventas
from controller.CRUD.detallesventasCRUD import DetallesVentasCRUD  # Importa el CRUD de Detalles de Ventas
from model.diccionarios import *

class VentasVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Ventas")
        
        # Instancias de los CRUDs de Ventas y Detalles de Ventas
        self.ventas_crud = VentasCRUD()
        self.detalles_ventas_crud = DetallesVentasCRUD()
        
        # Frame para la tabla de ventas
        self.frame_ventas = ttk.Frame(self.root)
        self.frame_ventas.pack(fill=tk.BOTH, expand=True)
        
        # Configuración de la tabla de ventas
        self.tabla_ventas = ttk.Treeview(self.frame_ventas, columns=("ID Venta", "Serie", "Factura", "NITCliente", "Cliente", "Fecha", "Total"), show="headings")
        self.tabla_ventas.heading("ID Venta", text="ID Venta")
        self.tabla_ventas.heading("Serie", text="Serie")
        self.tabla_ventas.heading("Factura", text="Factura")
        self.tabla_ventas.heading("NITCliente", text="NIT del Cliente")
        self.tabla_ventas.heading("Cliente", text="NIT del Cliente")
        self.tabla_ventas.heading("Fecha", text="Fecha y Hora")
        self.tabla_ventas.heading("Total", text="Total Venta")
        
        # Colocar la tabla y agregar scrollbar
        self.tabla_ventas.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame_ventas, orient=tk.VERTICAL, command=self.tabla_ventas.yview)
        self.tabla_ventas.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botón para seleccionar y ver detalles de la venta
        self.btn_ver_detalle = ttk.Button(self.root, text="Ver Detalle de Venta", command=self.ver_detalle_venta)
        self.btn_ver_detalle.pack(pady=10)
        
        # Cargar datos en la tabla de ventas
        self.cargar_ventas()
    
    def cargar_ventas(self):
        # Obtener todos los encabezados de ventas y llenar la tabla
        ventas = self.ventas_crud.getAllVentas()
        dicClientes=obtener_diccionario_clientes()
        for venta in ventas:
            # Suponiendo que el total de la venta es un campo calculado o agregado a la tabla de Ventas
            self.tabla_ventas.insert("", tk.END, values=(venta[0], venta[5], venta[6], venta[4], dicClientes.get(venta[4])['nombres'], venta[7], venta[12]))
    
    def ver_detalle_venta(self):
        # Obtener la venta seleccionada
        seleccionado = self.tabla_ventas.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una venta para ver el detalle.")
            return
        
        # Obtener el ID de la venta seleccionada
        valores = self.tabla_ventas.item(seleccionado, "values")
        venta_id = int(valores[0])
        
        # Crear ventana de detalle de la venta
        DetalleVentaVentana(self.root, self.detalles_ventas_crud, venta_id)
            
class DetalleVentaVentana:
    def __init__(self, parent, detalles_ventas_crud, venta_id):
        self.detalles_ventas_crud = detalles_ventas_crud
        self.venta_id = venta_id
        self.window = tk.Toplevel(parent)
        self.window.title(f"Detalle de Venta ID {venta_id}")
        
        # Frame para la tabla de detalle de venta
        self.frame_detalle = ttk.Frame(self.window)
        self.frame_detalle.pack(fill=tk.BOTH, expand=True)
        
        # Configuración de la tabla de detalles de venta
        self.tabla_detalle = ttk.Treeview(self.frame_detalle, columns=("ID Producto", "Producto", "Cantidad", "Precio Unitario", "Subtotal"), show="headings")
        self.tabla_detalle.heading("ID Producto", text="ID Producto")
        self.tabla_detalle.heading("Producto", text="Producto")
        self.tabla_detalle.heading("Cantidad", text="Cantidad")
        self.tabla_detalle.heading("Precio Unitario", text="Precio Unitario")
        self.tabla_detalle.heading("Subtotal", text="Subtotal")
        
        # Colocar la tabla y agregar scrollbar
        self.tabla_detalle.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame_detalle, orient=tk.VERTICAL, command=self.tabla_detalle.yview)
        self.tabla_detalle.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cargar datos del detalle de la venta
        self.cargar_detalle_venta()
    
    def cargar_detalle_venta(self):
        # Obtener el detalle de la venta usando el ID de la venta
        detalles = self.detalles_ventas_crud.getDetallesVentasByIDVenta(self.venta_id)
        dicProductos=obtener_diccionario_productos()
        
        for detalle in detalles:
            subtotal = detalle[3] * detalle[4]  # Cantidad * Precio Unitario
            self.tabla_detalle.insert("", tk.END, values=(detalle[2], dicProductos.get(detalle[2])['nombre'], detalle[3], detalle[4], subtotal))

