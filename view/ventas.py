import tkinter as tk
from tkinter import ttk, messagebox,Frame
from controller.CRUD.ventasCRUD import VentasCRUD  # Importa el CRUD de Ventas
from controller.CRUD.detallesventasCRUD import DetallesVentasCRUD  # Importa el CRUD de Detalles de Ventas
from model.diccionarios import *
from model.pdvModels import Venta, Detalle_Venta
from view.detalleventas import DetalleVentaVentana



class VentasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Instancias de los CRUDs de Ventas y Detalles de Ventas
        self.ventas_crud = VentasCRUD()
        self.detalles_ventas_crud = DetallesVentasCRUD()
        self.crear_interfaz()
        self.cargar_ventas()
        
        
    def crear_interfaz(self):
        # Labels y Entry para la entrada de datos en ventas, alineados en una cuadrícula
        tk.Label(self, text="ID Venta").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="ID Sucursal").grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        self.id_sucursal_entry = tk.Entry(self)
        self.id_sucursal_entry.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="ID Estado").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.id_estado_entry = tk.Entry(self)
        self.id_estado_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="ID Empleado").grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.id_empleado_entry = tk.Entry(self)
        self.id_empleado_entry.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="NIT Cliente").grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.nit_cliente_entry = tk.Entry(self)
        self.nit_cliente_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="ID Forma de Pago").grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.id_forma_pago_entry = tk.Entry(self)
        self.id_forma_pago_entry.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Serie").grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.serie_entry = tk.Entry(self)
        self.serie_entry.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Factura").grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        self.factura_entry = tk.Entry(self)
        self.factura_entry.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Fecha y Hora").grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.fecha_hora_entry = tk.Entry(self)
        self.fecha_hora_entry.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Año Venta").grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        self.anio_venta_entry = tk.Entry(self)
        self.anio_venta_entry.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Mes Venta").grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        self.mes_venta_entry = tk.Entry(self)
        self.mes_venta_entry.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Documento Pago").grid(row=5, column=2, padx=5, pady=5, sticky="snew")
        self.documento_pago_entry = tk.Entry(self)
        self.documento_pago_entry.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Total Venta").grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
        self.total_venta_entry = tk.Entry(self)
        self.total_venta_entry.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

        # Botones de CRUD para ventas
        self.btn_agregar_venta = ttk.Button(self, text="Agregar Venta", command=self.agregar_venta)
        self.btn_agregar_venta.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
        
        self.btn_actualizar_venta = ttk.Button(self, text="Actualizar Venta", command=self.actualizar_venta)
        self.btn_actualizar_venta.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
        
        self.btn_eliminar_venta = ttk.Button(self, text="Eliminar Venta", command=self.eliminar_venta)
        self.btn_eliminar_venta.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
        
        # Botón para ver detalles de la venta
        self.btn_ver_detalle = ttk.Button(self, text="Ver Detalle de Venta", command=self.ver_detalle_venta)
        self.btn_ver_detalle.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")
       
        # Configuración de la tabla de ventas
        self.datos_frame=Frame(self)
        self.datos_frame.grid(row=8, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.tabla_ventas = ttk.Treeview(self.datos_frame, columns=("ID Venta", "ID Sucursal", "ID Estado", "ID Empleado", "NIT Cliente", "ID Forma Pago", "Serie", "Factura", "Fecha y Hora", "Año Venta", "Mes Venta", "Documento Pago", "Total Venta"), show="headings")
        self.tabla_ventas.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        scrollbar = ttk.Scrollbar(self.datos_frame, orient="vertical", command=(self.tabla_ventas).yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tabla_ventas.configure(yscrollcommand=scrollbar.set)

        # Configurar el Frame interno para que el Treeview y la scrollbar se expandan
        self.datos_frame.grid_rowconfigure(0, weight=1)
        self.datos_frame.grid_columnconfigure(0, weight=1)
        headers = ["ID Venta", "ID Sucursal", "ID Estado", "ID Empleado", "NIT Cliente", "ID Forma Pago", "Serie", "Factura", "Fecha y Hora", "Año Venta", "Mes Venta", "Documento Pago", "Total Venta"]
        for i, header in enumerate(headers):
            self.tabla_ventas.heading(i, text=header)
            self.tabla_ventas.column(i, width=0, stretch=True)  # Ajusta automáticamente el tamaño de cada columna
        
        max_column = max(widget.grid_info()["column"] for widget in self.grid_slaves())
        for j in range(max_column + 1):
            self.grid_columnconfigure(j, weight=1)
        
        self.grid_rowconfigure(8, weight=1)
        

        # Asignar evento de selección en la tabla
        self.tabla_ventas.bind("<<TreeviewSelect>>", self.cargar_venta_seleccionada)
        
        
        # Cargar datos en la tabla de ventas

    def cargar_ventas(self):
        # Obtener todos los encabezados de ventas y llenar la tabla
        for row in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(row)
        
        ventas=list()
        tuplaventas= self.ventas_crud.getAllVentas()        
        for tupla in tuplaventas:      
            ventaauxiliar=Venta()      
            ventaauxiliar.set(tupla)
            ventas.append(ventaauxiliar)
        for venta in ventas:
            self.tabla_ventas.insert("", tk.END, values=(
                venta.idVenta, venta.idSucursal, venta.idEstado, venta.idEmpleado, venta.nitCliente,
                venta.idFormaDePago, venta.serie, venta.factura, venta.fechahora, venta.anioventa,
                venta.mesventa, venta.documentoPago, venta.totalVenta))

    def cargar_venta_seleccionada(self, event):
        # Obtener el elemento seleccionado
        seleccionado = self.tabla_ventas.focus()
        if not seleccionado:
            return
        
        valores = self.tabla_ventas.item(seleccionado, "values")
        
        # Cargar los valores en los Entry correspondientes
        entries = [
            self.id_venta_entry, self.id_sucursal_entry, self.id_estado_entry, self.id_empleado_entry,
            self.nit_cliente_entry, self.id_forma_pago_entry, self.serie_entry, self.factura_entry,
            self.fecha_hora_entry, self.anio_venta_entry, self.mes_venta_entry, self.documento_pago_entry,
            self.total_venta_entry
        ]
        
        for entry, valor in zip(entries, valores):
            entry.delete(0, tk.END)
            entry.insert(0, valor)

    def agregar_venta(self):
        self.ventas_crud.insertVenta(self.getVenta())
        self.cargar_ventas()
    
    def actualizar_venta(self):
        self.ventas_crud.updateVenta(self.getVenta())
        self.cargar_ventas()
    
    def eliminar_venta(self):
        self.ventas_crud.deleteVenta(self.getVenta())
        self.cargar_ventas()
        
    def getVenta(self):
        return Venta(idVenta=int(self.id_venta_entry.get()),
                     idSucursal=int(self.id_sucursal_entry.get()),
                     idEstado=int(self.id_estado_entry.get()),
                     idEmpleado=int(self.id_empleado_entry.get()),
                     nitCliente=self.nit_cliente_entry.get(),
                     idFormaDePago=int(self.id_forma_pago_entry.get()),
                     serie=self.serie_entry.get(),
                     factura=self.factura_entry.get(),
                     fechahora=self.fecha_hora_entry.get(),
                     anioventa=int(self.anio_venta_entry.get()),
                     mesventa=int(self.mes_venta_entry.get()),
                     documentoPago=self.documento_pago_entry.get(),
                     totalVenta=float(self.total_venta_entry.get()))
        
    def deseleccionar_venta(self):
        # Deselecciona todos los elementos de la tabla
        self.tabla_ventas.selection_remove(self.tabla_ventas.selection())

    def limpiar_entrys(self):
        # Limpia los Entry correspondientes
        self.anio_venta_entry.delete(0,tk.END)
        self.mes_venta_entry.delete(0,tk.END)
        self.documento_pago_entry.delete(0,tk.END)
        self.total_venta_entry.delete(0,tk.END)
        self.serie_entry.delete(0,tk.END)
        self.factura_entry.delete(0,tk.END)
        self.fecha_hora_entry.delete(0,tk.END)
        self.id_empleado_entry.delete(0,tk.END)
        self.id_estado_entry.delete(0,tk.END)
        self.id_sucursal_entry.delete(0,tk.END)
        self.id_venta_entry.delete(0,tk.END)
        self.nit_cliente_entry.delete(0,tk.END)
        self.id_forma_pago_entry.delete(0,tk.END)
            
    def ver_detalle_venta(self):
        seleccionado = self.tabla_ventas.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una venta para ver el detalle.")
            return
        
        valores = self.tabla_ventas.item(seleccionado, "values")
        venta_id = int(valores[0])
        DetalleVentaVentana(self, venta_id)
