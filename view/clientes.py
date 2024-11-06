import tkinter as tk
from tkinter import ttk, messagebox, Frame
from model.pdvModels import Cliente  # Importa la clase Cliente
from controller.CRUD.clientesCRUD import ClientesCRUD  # Importa el CRUD de Clientes

class ClientesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.clientes_crud = ClientesCRUD()
        
        # Elementos de la interfaz para CRUD de clientes
        self.crear_interfaz()
        
        # Cargar clientes en la tabla
        self.cargar_clientes()

    def crear_interfaz(self):
        # Campos para entrada de datos
        tk.Label(self, text="NIT Cliente").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.nitCliente_entry = tk.Entry(self)
        self.nitCliente_entry.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Nombres").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.nombres_entry = tk.Entry(self)
        self.nombres_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Apellidos").grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.apellidos_entry = tk.Entry(self)
        self.apellidos_entry.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Dirección").grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self, text="Teléfono").grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        tk.Label(self, text="Saldo por Pagar").grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.saldoPorPagar_entry = tk.Entry(self)
        self.saldoPorPagar_entry.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        # Botones para CRUD
        tk.Button(self, text="Agregar", command=self.agregar_cliente).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        tk.Button(self, text="Actualizar", command=self.actualizar_cliente).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        tk.Button(self, text="Eliminar", command=self.eliminar_cliente).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        
        # Tabla para mostrar clientes
        self.datos_frame = Frame(self)
        self.datos_frame.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.tabla_clientes = ttk.Treeview(self.datos_frame, columns=("NIT", "Nombres", "Apellidos", "Dirección", "Teléfono", "Saldo"), show="headings")
        self.tabla_clientes.heading("NIT", text="NIT")
        self.tabla_clientes.heading("Nombres", text="Nombres")
        self.tabla_clientes.heading("Apellidos", text="Apellidos")
        self.tabla_clientes.heading("Dirección", text="Dirección")
        self.tabla_clientes.heading("Teléfono", text="Teléfono")
        self.tabla_clientes.heading("Saldo", text="Saldo por Pagar")
        
        for i in range(6):
            self.tabla_clientes.column(i, width=0, stretch=True)
            
        self.tabla_clientes.bind("<<TreeviewSelect>>", self.seleccionar_cliente)
        self.tabla_clientes.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.datos_frame.grid_rowconfigure(0, weight=1)
        self.datos_frame.grid_columnconfigure(0, weight=1)
        
        max_column = max(widget.grid_info()["column"] for widget in self.grid_slaves())
        for j in range(max_column + 1):
            self.grid_columnconfigure(j, weight=1)
        
        self.grid_rowconfigure(5, weight=1)
    
    
    def cargar_clientes(self):
        # Limpiar la tabla
        for row in self.tabla_clientes.get_children():
            self.tabla_clientes.delete(row)
        
        # Obtener clientes y agregarlos a la tabla
        clientes = list()
        tuplacliente = self.clientes_crud.getAllClientes()        
        for tupla in tuplacliente:      
            clienteauxiliar = Cliente()      
            clienteauxiliar.set(tupla)
            clientes.append(clienteauxiliar)
          
        for cliente in clientes:
            self.tabla_clientes.insert("", "end", values=(cliente.nitCliente, cliente.nombres, cliente.apellidos, cliente.direccion, cliente.telefono, cliente.saldoPorPagar))

    def seleccionar_cliente(self, event):
    # Verificar si hay elementos seleccionados
        selected_items = self.tabla_clientes.selection()
        
        if selected_items:  # Si la lista no está vacía
            item = selected_items[0]
            cliente_seleccionado = self.tabla_clientes.item(item, "values")
            
            # Llenar los campos de entrada con los datos del cliente
            self.limpiar_entrys()
            self.nitCliente_entry.insert(tk.END, cliente_seleccionado[0])
            self.nombres_entry.insert(tk.END, cliente_seleccionado[1])
            self.apellidos_entry.insert(tk.END, cliente_seleccionado[2])
            self.direccion_entry.insert(tk.END, cliente_seleccionado[3])
            self.telefono_entry.insert(tk.END, cliente_seleccionado[4])
            self.saldoPorPagar_entry.insert(tk.END, cliente_seleccionado[5])

    def agregar_cliente(self):
        # Crear un objeto Cliente con los datos ingresados
        nuevo_cliente = Cliente(
            nitCliente=self.nitCliente_entry.get(),
            nombres=self.nombres_entry.get(),
            apellidos=self.apellidos_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            saldoPorPagar=float(self.saldoPorPagar_entry.get())
        )
        
        # Insertar en la base de datos y recargar la tabla
        self.clientes_crud.insertCliente(nuevo_cliente)        
        self.limpiar_entrys()
        self.deseleccionar_cliente()
        self.cargar_clientes()

    def actualizar_cliente(self):
        # Crear un objeto Cliente con los datos ingresados
        cliente_actualizado = Cliente(
            nitCliente=self.nitCliente_entry.get(),
            nombres=self.nombres_entry.get(),
            apellidos=self.apellidos_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            saldoPorPagar=float(self.saldoPorPagar_entry.get())
        )
        
        # Actualizar en la base de datos y recargar la tabla
        self.clientes_crud.updateCliente(cliente_actualizado)
        self.limpiar_entrys()
        self.deseleccionar_cliente()
        self.cargar_clientes()

    def eliminar_cliente(self):
        # Obtener NIT del cliente a eliminar
        cliente_eliminar = Cliente(
            nitCliente=self.nitCliente_entry.get(),
            nombres=self.nombres_entry.get(),
            apellidos=self.apellidos_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            saldoPorPagar=float(self.saldoPorPagar_entry.get())
        )
        # Eliminar en la base de datos y recargar la tabla
        self.clientes_crud.deleteCliente(cliente_eliminar)
        self.limpiar_entrys()
        self.deseleccionar_cliente()
        self.cargar_clientes()
        
    def limpiar_entrys(self):
        self.nitCliente_entry.delete(0, tk.END)
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.saldoPorPagar_entry.delete(0, tk.END)
        
    def deseleccionar_cliente(self):
        # Deselecciona todos los elementos de la tabla
        self.tabla_clientes.selection_remove(self.tabla_clientes.selection())
