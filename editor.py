import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import re
import os
import subprocess

HTML_FILE = "index.html"

# Configuración de botones
BUTTONS = {
    "Sube tus datos legales aquí": "Sube tus datos legales aquí",
    "Confirma tu rol en el equipo": "Confirma tu rol en el equipo",
    "Ver plan financiero 2025": "Ver plan financiero 2025",
    "Ver borrador de convenio Unillanos": "Ver borrador de convenio Unillanos",
    "Únete al canal oficial del equipo": "Únete al canal oficial del equipo"
}

# Configuración de estados
ESTADOS = ["Pendiente", "En progreso", "Completado"]

# Configuración de personas
PERSONAS = ["Marvin", "Jaime", "Verónica", "Reece"]

# Configuración de estados de compra
ESTADOS_COMPRA = ["En cotización", "Pedido", "Entregado"]

# Configuración de la línea de tiempo
TIMELINE_TASKS = [
    "Grabación de videos para Moonshot",
    "Inscripción oficial a Moonshot",
    "Viaje a Villavicencio, firma con Unillanos",
    "Pruebas con 500 vacas",
    "Lanzamiento formal del producto"
]

# Configuración de acciones personalizadas
ACCIONES_PERSONALIZADAS = {
    "Jaime": "Graba video comercial esta semana",
    "Verónica": "Confirma tu rol y datos para correo oficial",
    "Reece": "Sube enlace a repositorio GitHub del backend"
}

# Funciones para actualizar botones
def actualizar_boton(nombre_visible, link, estado):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Buscar el bloque del botón
    pattern = rf'<button class="cta-button.*?">{re.escape(nombre_visible)}</button>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró el botón: {nombre_visible}")
        return

    clase_estado = "active-button" if link else "no-link"
    nuevo_boton = f'<button class="cta-button {clase_estado}">{nombre_visible}</button>'

    # Reemplazar botón
    html = re.sub(pattern, nuevo_boton, html)

    # Reemplazar link asociado
    link_pattern = rf'<a href="[^"]*"\s*target="_blank"\s*class="legal-docs-link">\s*{re.escape(match.group(0))}\s*</a>'
    if link:
        nuevo_link = f'<a href="{link}" target="_blank" class="legal-docs-link">\n        {nuevo_boton}\n      </a>'
        html = re.sub(link_pattern, nuevo_link, html)
    else:
        html = re.sub(link_pattern, nuevo_boton, html)

    # Guardar cambios
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def editar_boton(nombre_visible):
    nuevo_link = simpledialog.askstring("Nuevo Link", f"Inserta el nuevo link para:\n{nombre_visible}")
    if nuevo_link is None:
        return
    nuevo_estado = simpledialog.askstring("Nuevo Estado", f"Nuevo estado para:\n{nombre_visible}\n(Pendiente, En progreso, Completado)", initialvalue="Pendiente")
    if nuevo_estado not in ESTADOS:
        messagebox.showerror("Error", "Estado no válido.")
        return
    actualizar_boton(nombre_visible, nuevo_link, nuevo_estado)
    messagebox.showinfo("Éxito", f"{nombre_visible} actualizado.")

# Funciones para actualizar línea de tiempo
def actualizar_timeline(fecha, tarea, responsable, estado, link):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Buscar la fila de la tabla que contiene la tarea
    pattern = rf'<tr>\s*<td>{re.escape(fecha)}</td>\s*<td>{re.escape(tarea)}</td>\s*<td>{re.escape(responsable)}</td>\s*<td>.*?</td>\s*<td><a href="[^"]*">.*?</a></td>\s*</tr>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la tarea: {tarea}")
        return

    # Crear la nueva fila con los datos actualizados
    nuevo_link = link if link else "#"
    nueva_fila = f'<tr>\n            <td>{fecha}</td>\n            <td>{tarea}</td>\n            <td>{responsable}</td>\n            <td>{estado}</td>\n            <td><a href="{nuevo_link}">{tarea}</a></td>\n          </tr>'

    # Reemplazar la fila en el HTML
    html = re.sub(pattern, nueva_fila, html)

    # Guardar cambios
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def editar_timeline(tarea):
    # Extraer la información actual de la tarea
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = rf'<tr>\s*<td>(.*?)</td>\s*<td>{re.escape(tarea)}</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td><a href="([^"]*)">.*?</a></td>\s*</tr>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la tarea: {tarea}")
        return

    fecha_actual = match.group(1)
    responsable_actual = match.group(2)
    estado_actual = match.group(3)
    link_actual = match.group(4)

    # Solicitar nuevos valores
    nueva_fecha = simpledialog.askstring("Nueva Fecha", f"Nueva fecha para:\n{tarea}", initialvalue=fecha_actual)
    if nueva_fecha is None:
        return

    nuevo_responsable = simpledialog.askstring("Nuevo Responsable", f"Nuevo responsable para:\n{tarea}", initialvalue=responsable_actual)
    if nuevo_responsable is None:
        return

    nuevo_estado = simpledialog.askstring("Nuevo Estado", f"Nuevo estado para:\n{tarea}\n(Pendiente, En progreso, Completado)", initialvalue=estado_actual)
    if nuevo_estado not in ESTADOS:
        messagebox.showerror("Error", "Estado no válido.")
        return

    nuevo_link = simpledialog.askstring("Nuevo Link", f"Nuevo link para:\n{tarea}", initialvalue=link_actual)
    if nuevo_link is None:
        return

    # Actualizar la línea de tiempo
    actualizar_timeline(nueva_fecha, tarea, nuevo_responsable, nuevo_estado, nuevo_link)
    messagebox.showinfo("Éxito", f"Tarea '{tarea}' actualizada.")

# Funciones para actualizar estado de documentación legal
def actualizar_documentacion(nombre, estado):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Buscar el bloque de documentación para la persona
    pattern = rf'<div class="status-item">\s*<h3>{re.escape(nombre)}</h3>\s*<div class="status-indicator (completed|pending)">(Completado|Pendiente)</div>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la documentación para: {nombre}")
        return

    # Crear el nuevo bloque con el estado actualizado
    nuevo_estado_clase = "completed" if estado == "Completado" else "pending"
    nuevo_bloque = f'<div class="status-item">\n          <h3>{nombre}</h3>\n          <div class="status-indicator {nuevo_estado_clase}">{estado}</div>'

    # Reemplazar el bloque en el HTML
    html = re.sub(pattern, nuevo_bloque, html)

    # Guardar cambios
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def editar_documentacion(nombre):
    # Extraer el estado actual
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = rf'<div class="status-item">\s*<h3>{re.escape(nombre)}</h3>\s*<div class="status-indicator (completed|pending)">(Completado|Pendiente)</div>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la documentación para: {nombre}")
        return

    estado_actual = match.group(2)

    # Solicitar nuevo estado
    nuevo_estado = simpledialog.askstring("Nuevo Estado", f"Nuevo estado para:\n{nombre}\n(Completado, Pendiente)", initialvalue=estado_actual)
    if nuevo_estado not in ["Completado", "Pendiente"]:
        messagebox.showerror("Error", "Estado no válido.")
        return

    # Actualizar la documentación
    actualizar_documentacion(nombre, nuevo_estado)
    messagebox.showinfo("Éxito", f"Documentación de {nombre} actualizada.")

# Funciones para actualizar acciones personalizadas
def actualizar_accion_personalizada(nombre, tarea, link=None):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Buscar el bloque de acción personalizada para la persona
    pattern = rf'<div class="action-card">\s*<h3>{re.escape(nombre)}</h3>\s*<p>.*?</p>\s*<button class="action-button">.*?</button>\s*</div>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la acción personalizada para: {nombre}")
        return

    # Crear el nuevo bloque con la tarea actualizada
    nuevo_boton = f'<button class="action-button">Confirmar</button>'
    if link:
        nuevo_boton = f'<a href="{link}" target="_blank"><button class="action-button">Confirmar</button></a>'
    
    nuevo_bloque = f'<div class="action-card">\n          <h3>{nombre}</h3>\n          <p>{tarea}</p>\n          {nuevo_boton}\n        </div>'

    # Reemplazar el bloque en el HTML
    html = re.sub(pattern, nuevo_bloque, html)

    # Guardar cambios
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def editar_accion_personalizada(nombre):
    # Extraer la tarea actual
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = rf'<div class="action-card">\s*<h3>{re.escape(nombre)}</h3>\s*<p>(.*?)</p>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", f"No se encontró la acción personalizada para: {nombre}")
        return

    tarea_actual = match.group(1)

    # Solicitar nueva tarea
    nueva_tarea = simpledialog.askstring("Nueva Tarea", f"Nueva tarea para:\n{nombre}", initialvalue=tarea_actual)
    if nueva_tarea is None:
        return

    # Solicitar link opcional
    nuevo_link = simpledialog.askstring("Nuevo Link (Opcional)", f"Nuevo link para:\n{nombre}\n(Dejar vacío si no hay link)")
    if nuevo_link is None:
        return

    # Actualizar la acción personalizada
    actualizar_accion_personalizada(nombre, nueva_tarea, nuevo_link if nuevo_link else None)
    messagebox.showinfo("Éxito", f"Acción personalizada de {nombre} actualizada.")

# Funciones para actualizar plan de compra
def actualizar_plan_compra(estado, responsable, link):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Buscar el bloque de plan de compra
    pattern = r'<div class="purchase-status">\s*<p><strong>Estado:</strong> <span class="status-text">.*?</span></p>\s*<p><strong>Responsable:</strong> .*?</p>\s*<p><strong>Links de cotización:</strong> <a href="[^"]*">Ver cotizaciones</a></p>\s*</div>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", "No se encontró el plan de compra")
        return

    # Crear el nuevo bloque con los datos actualizados
    nuevo_bloque = f'<div class="purchase-status">\n          <p><strong>Estado:</strong> <span class="status-text">{estado}</span></p>\n          <p><strong>Responsable:</strong> {responsable}</p>\n          <p><strong>Links de cotización:</strong> <a href="{link}">Ver cotizaciones</a></p>\n        </div>'

    # Reemplazar el bloque en el HTML
    html = re.sub(pattern, nuevo_bloque, html)

    # Guardar cambios
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def editar_plan_compra():
    # Extraer la información actual
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = r'<div class="purchase-status">\s*<p><strong>Estado:</strong> <span class="status-text">(.*?)</span></p>\s*<p><strong>Responsable:</strong> (.*?)</p>\s*<p><strong>Links de cotización:</strong> <a href="([^"]*)">Ver cotizaciones</a></p>\s*</div>'
    match = re.search(pattern, html)
    if not match:
        messagebox.showerror("Error", "No se encontró el plan de compra")
        return

    estado_actual = match.group(1)
    responsable_actual = match.group(2)
    link_actual = match.group(3)

    # Solicitar nuevos valores
    nuevo_estado = simpledialog.askstring("Nuevo Estado", f"Nuevo estado para el plan de compra\n({', '.join(ESTADOS_COMPRA)})", initialvalue=estado_actual)
    if nuevo_estado not in ESTADOS_COMPRA:
        messagebox.showerror("Error", "Estado no válido.")
        return

    nuevo_responsable = simpledialog.askstring("Nuevo Responsable", f"Nuevo responsable para el plan de compra", initialvalue=responsable_actual)
    if nuevo_responsable is None:
        return

    nuevo_link = simpledialog.askstring("Nuevo Link", f"Nuevo link para cotizaciones", initialvalue=link_actual)
    if nuevo_link is None:
        return

    # Actualizar el plan de compra
    actualizar_plan_compra(nuevo_estado, nuevo_responsable, nuevo_link)
    messagebox.showinfo("Éxito", "Plan de compra actualizado.")

# Función para hacer push a GitHub
def hacer_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Actualización desde editor.py"], check=True)
        subprocess.run(["git", "push"], check=True)
        messagebox.showinfo("Éxito", "Cambios enviados a GitHub.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al hacer push: {e}")

# GUI
class TartarusEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor - Tartarus Dynamics")
        self.root.geometry("900x700")
        
        # Configurar el tema oscuro
        self.setup_dark_theme()
        
        # Frame principal con padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título principal
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            title_frame, 
            text="Tartarus Dynamics - Editor", 
            font=("Segoe UI", 16, "bold")
        )
        title_label.pack(side=tk.LEFT)
        
        # Crear notebook para pestañas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Crear pestañas
        self.tab_botones = ttk.Frame(self.notebook)
        self.tab_timeline = ttk.Frame(self.notebook)
        self.tab_documentacion = ttk.Frame(self.notebook)
        self.tab_acciones = ttk.Frame(self.notebook)
        self.tab_proveedores = ttk.Frame(self.notebook)
        
        # Añadir pestañas al notebook
        self.notebook.add(self.tab_botones, text="Botones")
        self.notebook.add(self.tab_timeline, text="Línea de Tiempo")
        self.notebook.add(self.tab_documentacion, text="Documentación Legal")
        self.notebook.add(self.tab_acciones, text="Acciones Personalizadas")
        self.notebook.add(self.tab_proveedores, text="Proveedores")
        
        # Configurar pestaña de botones
        self.setup_botones_tab()
        
        # Configurar pestaña de línea de tiempo
        self.setup_timeline_tab()
        
        # Configurar pestaña de documentación legal
        self.setup_documentacion_tab()
        
        # Configurar pestaña de acciones personalizadas
        self.setup_acciones_tab()
        
        # Configurar pestaña de proveedores
        self.setup_proveedores_tab()
        
        # Frame para botones de acción
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Botón para hacer push
        btn_push = ttk.Button(
            action_frame, 
            text="Guardar y hacer Push", 
            command=hacer_push,
            style="Accent.TButton"
        )
        btn_push.pack(side=tk.RIGHT, padx=5)
    
    def setup_dark_theme(self):
        # Configurar el estilo ttk
        style = ttk.Style()
        
        # Configurar el tema
        style.theme_use('clam')
        
        # Colores
        bg_color = "#0c0f13"
        fg_color = "#ffffff"
        accent_color = "#00A676"
        accent_hover = "#00945E"
        select_bg = "#1a1f25"
        select_fg = "#ffffff"
        
        # Configurar estilos generales
        style.configure(".", 
                       background=bg_color, 
                       foreground=fg_color, 
                       font=("Segoe UI", 10),
                       borderwidth=0)
        
        # Configurar Notebook (pestañas)
        style.configure("TNotebook", background=bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", 
                       background=select_bg, 
                       foreground=fg_color, 
                       padding=[10, 5],
                       font=("Segoe UI", 10))
        style.map("TNotebook.Tab", 
                 background=[("selected", accent_color)],
                 foreground=[("selected", fg_color)])
        
        # Configurar Frame
        style.configure("TFrame", background=bg_color)
        
        # Configurar Label
        style.configure("TLabel", 
                       background=bg_color, 
                       foreground=fg_color,
                       font=("Segoe UI", 10))
        
        # Configurar Button
        style.configure("TButton", 
                       background=select_bg, 
                       foreground=fg_color,
                       padding=[10, 5],
                       font=("Segoe UI", 10))
        style.map("TButton", 
                 background=[("active", accent_hover)],
                 foreground=[("active", fg_color)])
        
        # Configurar Button de acento
        style.configure("Accent.TButton", 
                       background=accent_color, 
                       foreground=fg_color,
                       padding=[15, 8],
                       font=("Segoe UI", 10, "bold"))
        style.map("Accent.TButton", 
                 background=[("active", accent_hover)],
                 foreground=[("active", fg_color)])
        
        # Configurar Entry
        style.configure("TEntry", 
                       fieldbackground=select_bg, 
                       foreground=fg_color,
                       insertcolor=fg_color,
                       borderwidth=1)
        
        # Configurar Combobox
        style.configure("TCombobox", 
                       fieldbackground=select_bg, 
                       background=select_bg,
                       foreground=fg_color,
                       arrowcolor=fg_color,
                       borderwidth=1)
        style.map("TCombobox", 
                 fieldbackground=[("readonly", select_bg)],
                 selectbackground=[("readonly", accent_color)],
                 selectforeground=[("readonly", fg_color)])
        
        # Configurar el fondo de la ventana principal
        self.root.configure(bg=bg_color)
    
    def setup_botones_tab(self):
        # Frame para botones con padding
        frame = ttk.Frame(self.tab_botones, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(
            frame, 
            text="Editar Botones", 
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))
        
        # Frame para botones con scroll
        canvas = tk.Canvas(frame, bg="#0c0f13", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Botones
        for nombre in BUTTONS:
            btn = ttk.Button(
                scrollable_frame, 
                text=nombre, 
                command=lambda n=nombre: editar_boton(n),
                style="TButton"
            )
            btn.pack(fill=tk.X, pady=5)
        
        # Configurar scroll
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def setup_timeline_tab(self):
        # Frame para línea de tiempo con padding
        frame = ttk.Frame(self.tab_timeline, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(
            frame, 
            text="Editar Línea de Tiempo", 
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))
        
        # Frame para botones con scroll
        canvas = tk.Canvas(frame, bg="#0c0f13", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Botones para cada tarea
        for tarea in TIMELINE_TASKS:
            btn = ttk.Button(
                scrollable_frame, 
                text=tarea, 
                command=lambda t=tarea: editar_timeline(t),
                style="TButton"
            )
            btn.pack(fill=tk.X, pady=5)
        
        # Configurar scroll
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def setup_documentacion_tab(self):
        # Frame para documentación legal con padding
        frame = ttk.Frame(self.tab_documentacion, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(
            frame, 
            text="Editar Estado de Documentación Legal", 
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))
        
        # Frame para botones con scroll
        canvas = tk.Canvas(frame, bg="#0c0f13", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Botones para cada persona
        for persona in PERSONAS:
            btn = ttk.Button(
                scrollable_frame, 
                text=persona, 
                command=lambda p=persona: editar_documentacion(p),
                style="TButton"
            )
            btn.pack(fill=tk.X, pady=5)
        
        # Configurar scroll
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def setup_acciones_tab(self):
        # Frame para acciones personalizadas con padding
        frame = ttk.Frame(self.tab_acciones, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(
            frame, 
            text="Editar Acciones Personalizadas", 
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))
        
        # Frame para botones con scroll
        canvas = tk.Canvas(frame, bg="#0c0f13", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Botones para cada persona
        for persona in ACCIONES_PERSONALIZADAS.keys():
            btn = ttk.Button(
                scrollable_frame, 
                text=f"{persona}: {ACCIONES_PERSONALIZADAS[persona]}", 
                command=lambda p=persona: editar_accion_personalizada(p),
                style="TButton"
            )
            btn.pack(fill=tk.X, pady=5)
        
        # Configurar scroll
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def setup_proveedores_tab(self):
        # Frame para proveedores con padding
        frame = ttk.Frame(self.tab_proveedores, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(
            frame, 
            text="Editar Plan de Compra", 
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(0, 20))
        
        # Botón para editar plan de compra
        btn = ttk.Button(
            frame, 
            text="Editar Plan de Compra", 
            command=editar_plan_compra,
            style="TButton"
        )
        btn.pack(fill=tk.X, pady=5)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TartarusEditor(root)
    root.mainloop()
