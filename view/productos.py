import tkinter as tk
from tkinter import ttk, messagebox
from model.pdvModels import Producto
from controller.CRUD.productosCRUD import ProductosCRUD  # Importa el CRUD de Productos

class ProductosVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        
        # Instancia del CRUD de Productos
        self.productos_crud = ProductosCRUD()
        
        # Frame para la tabla de productos
        self.frame_tabla = ttk.Frame(self.root)
        self.frame_tabla.pack(fill=tk.BOTH, expand=True)
        
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Descripción", "Precio", "Existencias"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Descripción", text="Descripción")
        self.tabla.heading("Precio", text="Precio Unitario")
        self.tabla.heading("Existencias", text="Existencias")
        
        # Colocar la tabla y agregar scrollbar
        self.tabla.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botón para seleccionar y modificar
        self.btn_modificar = ttk.Button(self.root, text="Modificar Producto", command=self.modificar_producto)
        self.btn_modificar.pack(pady=10)
        
        # Cargar datos en la tabla
        self.cargar_productos()
    
    def cargar_productos(self):
        # Obtener todos los productos y llenar la tabla
        productos = self.productos_crud.getAllProductos()
        for producto in productos:
            self.tabla.insert("", tk.END, values=producto)
    
    def modificar_producto(self):
        # Obtener el producto seleccionado
        seleccionado = self.tabla.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar.")
            return
        
        # Obtener los valores del producto seleccionado
        valores = self.tabla.item(seleccionado, "values")
        producto_id = int(valores[0])
        
        # Crear ventana de modificación
        ModificarProductoVentana(self.root, self.productos_crud, producto_id)
        
class ModificarProductoVentana:
    def __init__(self, parent, productos_crud, producto_id):
        self.productos_crud = productos_crud
        self.producto_id = producto_id
        self.window = tk.Toplevel(parent)
        self.window.title("Modificar Producto")
        
        # Obtener datos actuales del producto
        producto = self.productos_crud.getProductoByID(self.producto_id)[0]
        
        # Campos de entrada
        tk.Label(self.window, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.window)
        self.entry_nombre.grid(row=0, column=1)
        self.entry_nombre.insert(0, producto[2])
        
        tk.Label(self.window, text="Descripción").grid(row=1, column=0, padx=10, pady=10)
        self.entry_descripcion = tk.Entry(self.window)
        self.entry_descripcion.grid(row=1, column=1)
        self.entry_descripcion.insert(0, producto[3])
        
        tk.Label(self.window, text="Precio Unitario").grid(row=2, column=0, padx=10, pady=10)
        self.entry_precio = tk.Entry(self.window)
        self.entry_precio.grid(row=2, column=1)
        self.entry_precio.insert(0, producto[4])
        
        tk.Label(self.window, text="Existencias").grid(row=3, column=0, padx=10, pady=10)
        self.entry_existencias = tk.Entry(self.window)
        self.entry_existencias.grid(row=3, column=1)
        self.entry_existencias.insert(0, producto[5])
        
        # Botón para guardar cambios
        self.btn_guardar = ttk.Button(self.window, text="Guardar Cambios", command=self.guardar_cambios)
        self.btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)
        
    def guardar_cambios(self):
        # Crear un objeto Producto con los nuevos valores
        producto_actualizado = Producto(
            idProducto=self.producto_id,
            idCategoria=1,  # Suponiendo que pertenece a la categoría 1
            nombre=self.entry_nombre.get(),
            descripcion=self.entry_descripcion.get(),
            precioVentaUnitario=float(self.entry_precio.get()),
            existencias=int(self.entry_existencias.get())
        )
        
        # Actualizar el producto
        if self.productos_crud.updateProducto(producto_actualizado):
            messagebox.showinfo("Éxito", "Producto actualizado exitosamente.")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto.")
