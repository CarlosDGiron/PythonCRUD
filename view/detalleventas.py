import tkinter as tk
from tkinter import ttk, messagebox
from controller.CRUD.detallesventasCRUD import DetallesVentasCRUD  # Importa el CRUD de Detalles de Ventas
from model.diccionarios import *
from model.pdvModels import Detalle_Venta

class DetalleVentaVentana:
    def __init__(self, parent, idVenta):
        self.detalles_ventas_crud = DetallesVentasCRUD()
        self.idVenta = idVenta
        self.window = tk.Toplevel(parent)
        self.window.title(f"Detalle de Venta ID {idVenta}")
        
        # Frame para el formulario de detalle de venta
        self.frame_formulario_detalle = ttk.Frame(self.window)
        self.frame_formulario_detalle.pack(pady=10)
        
        # Labels y Entry para la entrada de datos en detalle de venta
        tk.Label(self.frame_formulario_detalle, text="ID Detalle Venta").grid(row=0, column=0, padx=5, pady=5)
        self.id_detalle_venta_entry = tk.Entry(self.frame_formulario_detalle)
        self.id_detalle_venta_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario_detalle, text="ID Venta").grid(row=0, column=2, padx=5, pady=5)
        self.id_venta_entry = tk.Entry(self.frame_formulario_detalle)
        self.id_venta_entry.grid(row=0, column=3, padx=5, pady=5)
        self.id_venta_entry.insert(0, idVenta)  # Establecer el ID de la venta automáticamente
        self.id_venta_entry.config(state="readonly")  # Hacer que el campo sea de solo lectura

        tk.Label(self.frame_formulario_detalle, text="ID Producto").grid(row=1, column=0, padx=5, pady=5)
        self.id_producto_entry = tk.Entry(self.frame_formulario_detalle)
        self.id_producto_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario_detalle, text="Cantidad").grid(row=1, column=2, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.frame_formulario_detalle)
        self.cantidad_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(self.frame_formulario_detalle, text="Precio Unitario").grid(row=2, column=0, padx=5, pady=5)
        self.precio_unitario_entry = tk.Entry(self.frame_formulario_detalle)
        self.precio_unitario_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario_detalle, text="Subtotal").grid(row=2, column=2, padx=5, pady=5)
        self.subtotal_entry = tk.Entry(self.frame_formulario_detalle)
        self.subtotal_entry.grid(row=2, column=3, padx=5, pady=5)
        self.subtotal_entry.config(state="readonly")  # Hacer que el campo sea de solo lectura

        # Botones de CRUD para detalle de venta
        self.btn_agregar_detalle = ttk.Button(self.frame_formulario_detalle, text="Agregar Detalle", command=self.agregar_detalle)
        self.btn_agregar_detalle.grid(row=3, column=0, padx=5, pady=5)
        
        self.btn_actualizar_detalle = ttk.Button(self.frame_formulario_detalle, text="Actualizar Detalle", command=self.actualizar_detalle)
        self.btn_actualizar_detalle.grid(row=3, column=1, padx=5, pady=5)
        
        self.btn_eliminar_detalle = ttk.Button(self.frame_formulario_detalle, text="Eliminar Detalle", command=self.eliminar_detalle)
        self.btn_eliminar_detalle.grid(row=3, column=2, padx=5, pady=5)

        # Frame para la tabla de detalles de venta
        self.frame_detalle = ttk.Frame(self.window)
        self.frame_detalle.pack(fill=tk.BOTH, expand=True)
        
        # Configuración de la tabla de detalles de venta
        self.tabla_detalle = ttk.Treeview(self.frame_detalle, columns=("ID Detalle Venta", "ID Producto", "Cantidad", "Precio Unitario", "Subtotal"), show="headings")
        self.tabla_detalle.heading("ID Detalle Venta", text="ID Detalle Venta")
        self.tabla_detalle.heading("ID Producto", text="ID Producto")
        self.tabla_detalle.heading("Cantidad", text="Cantidad")
        self.tabla_detalle.heading("Precio Unitario", text="Precio Unitario")
        self.tabla_detalle.heading("Subtotal", text="Subtotal")

        # Colocar la tabla y agregar scrollbar
        self.tabla_detalle.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame_detalle, orient=tk.VERTICAL, command=self.tabla_detalle.yview)
        self.tabla_detalle.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Asignar evento de selección en la tabla
        self.tabla_detalle.bind("<<TreeviewSelect>>", self.cargar_detalle_seleccionado)

        # Cargar datos del detalle de la venta
        self.cargar_detalle_venta()
    
    def cargar_detalle_venta(self):
        # Obtener el detalle de la venta usando el ID de la venta
        for row in self.tabla_detalle.get_children():
            self.tabla_detalle.delete(row)

        detalles=list()
        tupladetalles= self.detalles_ventas_crud.getDetallesVentasByIDVenta(self.idVenta)        
        for tupla in tupladetalles:      
            detallesauxiliar=Detalle_Venta()      
            detallesauxiliar.set(tupla)
            detalles.append(detallesauxiliar)
        for detalle in detalles:
            self.cargar_detalle_ventanas_con_Detalle_ventana(detalle)
            
    def cargar_detalle_ventanas_con_Detalle_ventana(self,detalle:Detalle_Venta):
        subtotal = detalle.cantidad * detalle.precioVentaUnitario  # Calcular subtotal        
        self.tabla_detalle.insert("", tk.END, values=(detalle.idDetalleVenta, detalle.idProducto,detalle.cantidad,detalle.precioVentaUnitario, subtotal))
        
    def cargar_detalle_seleccionado(self, event):
        # Obtener el elemento seleccionado
        seleccionado = self.tabla_detalle.focus()
        if not seleccionado:
            return
        
        valores = self.tabla_detalle.item(seleccionado, "values")
        
        # Cargar los valores en los Entry correspondientes
        self.id_detalle_venta_entry.delete(0, tk.END)
        self.id_detalle_venta_entry.insert(0, valores[0])

        self.id_producto_entry.delete(0, tk.END)
        self.id_producto_entry.insert(0, valores[1])

        self.cantidad_entry.delete(0, tk.END)
        self.cantidad_entry.insert(0, valores[2])

        self.precio_unitario_entry.delete(0, tk.END)
        self.precio_unitario_entry.insert(0, valores[3])

        self.subtotal_entry.config(state="normal")
        self.subtotal_entry.delete(0, tk.END)
        self.subtotal_entry.insert(0, valores[4])
        self.subtotal_entry.config(state="readonly")

    def agregar_detalle(self):
        # Lógica para agregar un nuevo detalle de venta
        self.detalles_ventas_crud.insertDetalleVenta(self.getDetalleVenta())
        self.cargar_detalle_venta()
    
    def actualizar_detalle(self):
        # Lógica para actualizar un detalle de venta seleccionado
        self.detalles_ventas_crud.updateDetalleVenta(self.getDetalleVenta())
        self.cargar_detalle_venta()
    
    def eliminar_detalle(self):
        # Lógica para eliminar un detalle de venta seleccionado
        self.detalles_ventas_crud.deleteDetalleVenta(self.getDetalleVenta())
        self.cargar_detalle_venta()
        
    def getDetalleVenta(self):
        return Detalle_Venta(idDetalleVenta=int(self.id_detalle_venta_entry.get()),
                                   idVenta=int(self.idVenta),
                                   idProducto=int(self.id_producto_entry.get()),
                                   cantidad=int(self.cantidad_entry.get()),
                                   precioVentaUnitario=float(self.precio_unitario_entry.get()))
