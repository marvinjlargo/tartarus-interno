# 🚀 Tartarus Interno

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=github&logoColor=white)](https://pages.github.com/)

## 📋 Descripción

Tartarus Interno es un sitio web estático creado para uso interno de la startup agrícola **Tartarus Dynamics**. El proyecto muestra una línea de tiempo editable con los hitos clave del proyecto entre abril y julio de 2025, permitiendo a los socios fundadores seguir el progreso y actualizar el estado de las tareas de forma sencilla.

## 🎯 Propósito

Este repositorio sirve como centro de información y seguimiento para los socios fundadores de Tartarus Dynamics, facilitando la visualización y gestión de tareas críticas durante el período de lanzamiento del producto.

## 👥 Usuarios

- **Marvin** - Fundador
- **Reece** - Fundador
- **Jaime** - Fundador
- **Verónica** - Fundadora

## 🛠️ Tecnologías

- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticación**: Sistema de login básico implementado en `main.js`
- **Edición**: Editor gráfico en Python (`editor.py`)
- **Hosting**: GitHub Pages
- **Documentación**: FPDF para generación de logs PDF

## 📦 Estructura del Repositorio

```
/nutag-timeline
├── index.html          # Página principal con la línea de tiempo
├── style.css           # Estilos CSS
├── main.js             # Lógica JavaScript y autenticación
├── tartarus-logo.png   # Logo de la empresa
├── editor.py           # Editor gráfico en Python
└── README.md           # Documentación
```

## 🔐 Acceso

**Credenciales por defecto:**
- **Usuario:** `tartarus`
- **Contraseña:** `nu2025start`

## 🚀 Funcionalidades Clave

- **Línea de tiempo interactiva** con tareas, fechas y responsables
- **Sistema de estados** para tareas: Pendiente / En progreso / Completado
- **Diseño responsivo** optimizado para dispositivos móviles
- **Editor gráfico** en Python para modificar contenido sin necesidad de codificar
- **Generación de historial** de cambios en formato PDF
- **Integración con servicios externos** (Google Drive, Discord) para comunicación y documentación legal

## 📖 Guía de Uso

### Visualización del Sitio

1. Clona este repositorio:
   ```bash
   git clone https://github.com/marvinjlargo/tartarus-interno.git
   cd tartarus-interno
   ```

2. Abre `index.html` en tu navegador o accede al sitio desplegado en GitHub Pages:
   ```
   https://marvinjlargo.github.io/tartarus-interno
   ```

3. Inicia sesión con las credenciales por defecto:
   - Usuario: `tartarus`
   - Contraseña: `nu2025start`

### Edición de Contenido

1. Asegúrate de tener Python instalado en tu sistema

2. Instala las dependencias necesarias:
   ```bash
   pip install fpdf
   ```

3. Ejecuta el editor gráfico:
   ```bash
   python editor.py
   ```

4. Utiliza la interfaz gráfica para modificar:
   - Botones y enlaces
   - Línea de tiempo y tareas
   - Estado de documentación legal
   - Acciones personalizadas
   - Plan de compra

5. Guarda los cambios y haz push al repositorio:
   - Utiliza el botón "Publicar cambios" en el editor
   - O ejecuta manualmente:
     ```bash
     git add .
     git commit -m "Actualización desde editor.py"
     git push origin main
     ```

## 📊 Historial de Cambios

El editor registra automáticamente todos los cambios realizados en un archivo `editor_log.txt`. Puedes:

- Ver el historial en la pestaña "Historial" del editor
- Exportar el historial a PDF con el botón "📄 Exportar historial a PDF"

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es privado y está destinado exclusivamente para uso interno de Tartarus Dynamics.

## ✍️ Autor

**Marvin Johared Largo Martínez** - [GitHub](https://github.com/marvinjlargo)

---

<p align="center">© 2025 Tartarus Dynamics. Todos los derechos reservados.</p> 