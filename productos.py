import tkinter as tk
from tkinter import ttk, messagebox, Frame
from model.pdvModels import Producto
from controller.CRUD.productosCRUD import ProductosCRUD  # Importa el CRUD de Productos

class ProductosFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.productos_crud = ProductosCRUD()
        
        # Elementos de la interfaz para CRUD de productos
        self.crear_interfaz()
        
        # Cargar productos en la tabla
        self.cargar_productos()

    def crear_interfaz(self):
        # Campos para entrada de datos
        tk.Label(self, text="ID Producto").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.idProducto_entry = tk.Entry(self)
        self.idProducto_entry.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="ID Categoría").grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        self.idCategoria_entry = tk.Entry(self)
        self.idCategoria_entry.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Nombre").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Descripción").grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Precio Venta Unitario").grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.precio_entry = tk.Entry(self)
        self.precio_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Existencias").grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.existencias_entry = tk.Entry(self)
        self.existencias_entry.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        # Botones para CRUD
        tk.Button(self, text="Agregar", command=self.agregar_producto).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(self, text="Actualizar", command=self.actualizar_producto).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(self, text="Eliminar", command=self.eliminar_producto).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        
        # Tabla para mostrar productos
        self.datos_frame=Frame(self)
        self.datos_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.tabla_productos = ttk.Treeview(self.datos_frame, columns=("ID", "Categoría", "Nombre", "Descripción", "Precio", "Existencias"), show="headings")
        self.tabla_productos.heading("ID", text="ID")
        self.tabla_productos.heading("Categoría", text="Categoría")
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Descripción", text="Descripción")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.heading("Existencias", text="Existencias")
        
        for i in range(6):
            self.tabla_productos.column(i, width=0, stretch=True)
            
        self.tabla_productos.bind("<<TreeviewSelect>>", self.seleccionar_producto)
        self.tabla_productos.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.datos_frame.grid_rowconfigure(0, weight=1)
        self.datos_frame.grid_columnconfigure(0, weight=1)
        
        max_column = max(widget.grid_info()["column"] for widget in self.grid_slaves())
        for j in range(max_column + 1):
            self.grid_columnconfigure(j, weight=1)
        
        self.grid_rowconfigure(4, weight=1)
    
    
    def cargar_productos(self):
        # Limpiar la tabla
        for row in self.tabla_productos.get_children():
            self.tabla_productos.delete(row)
        
        # Obtener productos y agregarlos a la tabla
        productos=list()
        tuplaproducto= self.productos_crud.getAllProductos()        
        for tupla in tuplaproducto:      
            productoauxiliar=Producto()      
            productoauxiliar.set(tupla)
            print(productoauxiliar)
            productos.append(productoauxiliar)
          
        for producto in productos:
            self.tabla_productos.insert("", "end", values=(producto.idProducto, producto.idCategoria, producto.nombre, producto.descripcion, producto.precioVentaUnitario, producto.existencias))

    def seleccionar_producto(self, event):
        # Obtener datos del producto seleccionado
        item = self.tabla_productos.selection()[0]
        producto_seleccionado = self.tabla_productos.item(item, "values")
        
        # Llenar campos de entrada con los datos del producto
        self.limpiar_entrys()
        self.idProducto_entry.insert(tk.END, producto_seleccionado[0])
        self.idCategoria_entry.insert(tk.END, producto_seleccionado[1])
        self.nombre_entry.insert(tk.END, producto_seleccionado[2])
        self.descripcion_entry.insert(tk.END, producto_seleccionado[3])
        self.precio_entry.insert(tk.END, producto_seleccionado[4])
        self.existencias_entry.insert(tk.END, producto_seleccionado[5])

    def agregar_producto(self):
        # Crear un objeto Producto con los datos ingresados
        nuevo_producto = Producto(
            idCategoria=int(self.idCategoria_entry.get()),
            nombre=self.nombre_entry.get(),
            descripcion=self.descripcion_entry.get(),
            precioVentaUnitario=float(self.precio_entry.get()),
            existencias=int(self.existencias_entry.get())
        )
        
        # Insertar en la base de datos y recargar la tabla
        self.productos_crud.insertProducto(nuevo_producto)
        self.cargar_productos()
        self.limpiar_entrys()

    def actualizar_producto(self):
        # Crear un objeto Producto con los datos ingresados
        producto_actualizado = Producto(
            idProducto=int(self.idProducto_entry.get()),
            idCategoria=int(self.idCategoria_entry.get()),
            nombre=self.nombre_entry.get(),
            descripcion=self.descripcion_entry.get(),
            precioVentaUnitario=float(self.precio_entry.get()),
            existencias=int(self.existencias_entry.get())
        )
        
        # Actualizar en la base de datos y recargar la tabla
        self.productos_crud.updateProducto(producto_actualizado)
        self.cargar_productos()
        self.limpiar_entrys()

    def eliminar_producto(self):
        # Obtener ID del producto a eliminar
        producto_eliminar = Producto(
            idProducto=int(self.idProducto_entry.get()),
            idCategoria=int(self.idCategoria_entry.get()),
            nombre=self.nombre_entry.get(),
            descripcion=self.descripcion_entry.get(),
            precioVentaUnitario=float(self.precio_entry.get()),
            existencias=int(self.existencias_entry.get())
        )
        # Eliminar en la base de datos y recargar la tabla
        self.productos_crud.deleteProducto(producto_eliminar)
        self.cargar_productos()
        self.limpiar_entrys()
        
    def limpiar_entrys(self):
        self.idProducto_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.existencias_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.idCategoria_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)