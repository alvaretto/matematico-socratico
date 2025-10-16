<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# 🧠 MateTutor - Tu Tutor de Matemáticas para el ICFES

MateTutor es un tutor de matemáticas inteligente que utiliza **Google Gemini AI** y el **método socrático** para ayudar a estudiantes a resolver problemas de matemáticas del ICFES. En lugar de dar respuestas directas, MateTutor guía a los estudiantes con preguntas para que descubran las soluciones por sí mismos.

## ✨ Características

- 🤖 **IA Conversacional**: Usa Google Gemini 2.0 Flash para interacciones naturales
- 📸 **Análisis de Imágenes**: Sube fotos de problemas matemáticos
- 💬 **Chat Interactivo**: Interfaz de chat fluida con historial de conversación
- 🎓 **Método Socrático**: Aprende resolviendo, no memorizando
- 🎨 **Diseño Moderno**: Interfaz limpia y amigable
- ⚡ **Respuestas en Streaming**: Ve las respuestas generándose en tiempo real

## 🚀 Despliegue en Streamlit Community Cloud

### Paso 1: Preparar el Repositorio

1. **Sube tu código a GitHub**:
   ```bash
   git add .
   git commit -m "Migración a Streamlit"
   git push origin main
   ```

2. **Asegúrate de que estos archivos estén en tu repositorio**:
   - ✅ `streamlit_app.py` (archivo principal)
   - ✅ `requirements.txt` (dependencias)
   - ✅ `.streamlit/config.toml` (configuración)

### Paso 2: Obtener tu API Key de Google Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Get API Key"** o **"Create API Key"**
4. Copia tu API key (la necesitarás en el siguiente paso)

### Paso 3: Desplegar en Streamlit Cloud

1. **Ve a [Streamlit Community Cloud](https://share.streamlit.io/)**

2. **Inicia sesión** con tu cuenta de GitHub

3. **Haz clic en "New app"**

4. **Configura tu aplicación**:
   - **Repository**: Selecciona tu repositorio de GitHub
   - **Branch**: `main` (o la rama que uses)
   - **Main file path**: `streamlit_app.py`

5. **Configura los Secrets** (¡MUY IMPORTANTE!):
   - Haz clic en **"Advanced settings"**
   - En la sección **"Secrets"**, agrega:
     ```toml
     GEMINI_API_KEY = "tu-api-key-aquí"
     ```
   - Reemplaza `"tu-api-key-aquí"` con tu API key de Google Gemini

6. **Haz clic en "Deploy"**

7. **¡Listo!** Tu app estará disponible en unos minutos en una URL como:
   ```
   https://tu-usuario-matetutor.streamlit.app
   ```

### 🔐 Gestión de Secrets (Importante)

**NUNCA** subas tu API key al repositorio. Streamlit Cloud usa un sistema de secrets seguro:

- Los secrets se configuran en la interfaz web de Streamlit Cloud
- No se guardan en el código ni en GitHub
- Puedes editarlos en cualquier momento desde el dashboard de tu app

Para editar secrets después del despliegue:
1. Ve a tu app en Streamlit Cloud
2. Haz clic en **"⚙️ Settings"**
3. Selecciona **"Secrets"**
4. Edita y guarda

## 💻 Ejecutar Localmente

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/matetutor.git
   cd matetutor
   ```

2. **Crea un entorno virtual** (recomendado):
   ```bash
   python -m venv venv

   # En Windows:
   venv\Scripts\activate

   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu API Key**:

   Crea un archivo `.streamlit/secrets.toml` en la raíz del proyecto:
   ```toml
   GEMINI_API_KEY = "tu-api-key-aquí"
   ```

5. **Ejecuta la aplicación**:
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Abre tu navegador** en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
matetutor/
├── streamlit_app.py          # Aplicación principal de Streamlit
├── requirements.txt           # Dependencias de Python
├── .streamlit/
│   ├── config.toml           # Configuración de tema y servidor
│   └── secrets.toml          # API keys (NO subir a GitHub)
├── .gitignore                # Archivos a ignorar en Git
└── README.md                 # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para aplicaciones web de ML/AI
- **[Google Gemini AI](https://ai.google.dev/)**: Modelo de lenguaje multimodal
- **[Python](https://www.python.org/)**: Lenguaje de programación
- **[Pillow](https://python-pillow.org/)**: Procesamiento de imágenes

## 🎨 Personalización

### Cambiar el Tema

Edita `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#007bff"        # Color principal (azul)
backgroundColor = "#f0f4f8"     # Fondo de la app
secondaryBackgroundColor = "#ffffff"  # Fondo de widgets
textColor = "#333333"           # Color del texto
```

### Modificar el Prompt del Tutor

Edita la variable `MATE_TUTOR_PROMPT` en `streamlit_app.py` para cambiar el comportamiento del tutor.

## 🐛 Solución de Problemas

### Error: "GEMINI_API_KEY not found"

**Solución**: Asegúrate de haber configurado el secret en Streamlit Cloud o el archivo `secrets.toml` localmente.

### Error: "Module not found"

**Solución**: Instala las dependencias:
```bash
pip install -r requirements.txt
```

### La app no carga imágenes

**Solución**: Verifica que el formato de imagen sea PNG, JPG o JPEG.

### Error de cuota de API

**Solución**: Google Gemini tiene límites de uso gratuito. Verifica tu cuota en [Google AI Studio](https://aistudio.google.com/).

## 📝 Licencia

Este proyecto está bajo la Licencia Apache 2.0. Ver el archivo de licencia para más detalles.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar MateTutor:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en GitHub.

---

Desarrollado con ❤️ para ayudar a estudiantes a prepararse para el ICFES
