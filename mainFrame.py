import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self, submenus):
        super().__init__()
        
        self.title("Aplicación Dinámica con Menú")
        self.geometry("400x300")
        
        # Crear el menú superior
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        
        # Frame actual para mostrar el contenido
        self.frame_actual = None
        
        # Generar los menús y submenús dinámicamente usando el parámetro `submenus`
        self.generar_menu(submenus)

    def generar_menu(self, submenus):
        # Agrupar los submenús por idMenu y nombre de menú
        menus = {}
        for idMenu, idSubmenu, menu_nombre, submenu_nombre in submenus:
            if idMenu not in menus:
                menus[idMenu] = {"nombre": menu_nombre, "submenus": []}
            menus[idMenu]["submenus"].append((idSubmenu, submenu_nombre))
        
        # Crear los menús en la barra de menú
        for idMenu, menu_info in menus.items():
            menu_nombre = menu_info["nombre"]
            submenu_items = menu_info["submenus"]
            
            # Crear un menú desplegable
            menu_desplegable = tk.Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label=menu_nombre, menu=menu_desplegable)
            
            # Agregar los submenús
            for idSubmenu, submenu_nombre in submenu_items:
                # Asocia cada submenú con una función que cargará el frame correspondiente
                menu_desplegable.add_command(
                    label=submenu_nombre,
                    command=lambda idSubmenu=idSubmenu: self.cargar_frame(idSubmenu)
                )
                self.cargar_frame(submenus[0][1])
    
    def cargar_frame(self, idSubmenu):
        # Ocultar el frame actual si existe
        if self.frame_actual:
            self.frame_actual.pack_forget()
        
        # Crear una instancia de la clase del frame según el idSubmenu (podemos definir clases específicas más adelante)
        frame = FrameDinamico(self, idSubmenu)
        frame.pack(fill="both", expand=True)
        
        # Actualizar el frame actual
        self.frame_actual = frame

class FrameDinamico(tk.Frame):
    def __init__(self, parent, idSubmenu):
        super().__init__(parent)
        label = tk.Label(self, text=f"Contenido del Submenú {idSubmenu}", font=("Arial", 18))
        label.pack(pady=50)
