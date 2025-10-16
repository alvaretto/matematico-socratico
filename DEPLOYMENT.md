# 🚀 Guía Rápida de Despliegue en Streamlit Community Cloud

Esta guía te llevará paso a paso para desplegar MateTutor en Streamlit Community Cloud de forma **100% gratuita**.

## ⏱️ Tiempo estimado: 10 minutos

---

## 📋 Requisitos Previos

- ✅ Cuenta de GitHub (gratuita)
- ✅ Cuenta de Google (para obtener API key de Gemini)
- ✅ Tu código subido a un repositorio de GitHub

---

## 🔑 Paso 1: Obtener tu API Key de Google Gemini (3 minutos)

1. **Abre tu navegador** y ve a:
   ```
   https://aistudio.google.com/app/apikey
   ```

2. **Inicia sesión** con tu cuenta de Google

3. **Crea una API Key**:
   - Haz clic en el botón **"Create API Key"**
   - Selecciona **"Create API key in new project"** (o usa un proyecto existente)
   - Espera unos segundos mientras se crea

4. **Copia tu API Key**:
   - Verás algo como: `AIzaSyD...` (una cadena larga de caracteres)
   - Haz clic en el icono de **copiar** 📋
   - **¡GUÁRDALA EN UN LUGAR SEGURO!** La necesitarás en el Paso 3

> ⚠️ **IMPORTANTE**: Nunca compartas tu API key públicamente ni la subas a GitHub

---

## 📤 Paso 2: Subir tu Código a GitHub (2 minutos)

Si aún no has subido tu código:

```bash
# Inicializa Git (si no lo has hecho)
git init

# Agrega todos los archivos
git add .

# Haz tu primer commit
git commit -m "Aplicación MateTutor lista para despliegue"

# Conecta con tu repositorio de GitHub
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git

# Sube el código
git push -u origin main
```

> 💡 **Tip**: Si no tienes un repositorio, créalo en [github.com/new](https://github.com/new)

---

## ☁️ Paso 3: Desplegar en Streamlit Cloud (5 minutos)

### 3.1 Acceder a Streamlit Cloud

1. **Ve a**: [share.streamlit.io](https://share.streamlit.io/)

2. **Inicia sesión** con tu cuenta de GitHub
   - Haz clic en **"Sign in"**
   - Selecciona **"Continue with GitHub"**
   - Autoriza a Streamlit Cloud

### 3.2 Crear una Nueva App

1. **Haz clic en** el botón **"New app"** (esquina superior derecha)

2. **Completa el formulario**:

   | Campo | Valor |
   |-------|-------|
   | **Repository** | Selecciona tu repositorio (ej: `tu-usuario/matetutor`) |
   | **Branch** | `main` (o la rama que uses) |
   | **Main file path** | `streamlit_app.py` |
   | **App URL** (opcional) | Personaliza la URL de tu app |

### 3.3 Configurar Secrets (¡MUY IMPORTANTE!)

1. **Antes de hacer clic en "Deploy"**, haz clic en **"Advanced settings"**

2. En la sección **"Secrets"**, pega lo siguiente:
   ```toml
   GEMINI_API_KEY = "AIzaSyD..."
   ```
   
   > ⚠️ Reemplaza `AIzaSyD...` con tu API key real que copiaste en el Paso 1

3. **Verifica** que:
   - No haya espacios extra
   - Las comillas estén correctas
   - La API key esté completa

### 3.4 Desplegar

1. **Haz clic en** el botón **"Deploy!"**

2. **Espera** entre 2-5 minutos mientras Streamlit:
   - Clona tu repositorio
   - Instala las dependencias
   - Inicia tu aplicación

3. **¡Listo!** 🎉 Tu app estará disponible en:
   ```
   https://tu-usuario-matetutor.streamlit.app
   ```

---

## ✅ Verificar que Todo Funciona

1. **Abre la URL** de tu app

2. **Verifica**:
   - ✅ Se muestra el mensaje de bienvenida de MateTutor
   - ✅ Puedes escribir un mensaje y recibir respuesta
   - ✅ Puedes subir una imagen
   - ✅ No hay errores de API key

3. **Prueba la funcionalidad**:
   - Escribe: "¿Cómo resuelvo ecuaciones de segundo grado?"
   - Sube una imagen de un problema matemático
   - Verifica que las respuestas sean coherentes

---

## 🔧 Configuración Adicional (Opcional)

### Personalizar la URL

Por defecto, tu app tendrá una URL como:
```
https://matetutor-tu-tutor-de-icfes-abc123.streamlit.app
```

Para personalizarla:
1. Ve a tu app en Streamlit Cloud
2. Haz clic en **"⚙️ Settings"**
3. En **"General"**, edita el **"App URL"**
4. Guarda los cambios

### Configurar Dominio Personalizado (Requiere plan Pro)

Si tienes un dominio propio, puedes configurarlo en la sección de Settings.

---

## 🐛 Solución de Problemas Comunes

### ❌ Error: "GEMINI_API_KEY not found"

**Causa**: No configuraste el secret correctamente

**Solución**:
1. Ve a tu app en Streamlit Cloud
2. Haz clic en **"⚙️ Settings"** → **"Secrets"**
3. Verifica que el formato sea exactamente:
   ```toml
   GEMINI_API_KEY = "tu-api-key"
   ```
4. Guarda y espera a que la app se reinicie

### ❌ Error: "Module not found"

**Causa**: Falta una dependencia en `requirements.txt`

**Solución**:
1. Verifica que `requirements.txt` contenga:
   ```
   streamlit>=1.31.0
   google-generativeai>=0.8.0
   Pillow>=10.0.0
   ```
2. Haz commit y push de los cambios
3. La app se redespliegará automáticamente

### ❌ Error: "API key invalid"

**Causa**: La API key es incorrecta o ha expirado

**Solución**:
1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Verifica que tu API key esté activa
3. Si es necesario, crea una nueva
4. Actualiza el secret en Streamlit Cloud

### ❌ La app está muy lenta

**Causa**: Límites de recursos en el plan gratuito

**Soluciones**:
- Espera unos segundos, la primera carga puede ser lenta
- Verifica tu cuota de API de Gemini
- Considera optimizar el código o actualizar al plan Pro

### ❌ Error: "Resource limits exceeded"

**Causa**: Demasiadas solicitudes o uso excesivo de memoria

**Solución**:
- Espera unos minutos y vuelve a intentar
- Limpia el historial del chat con el botón "Limpiar conversación"
- Verifica los límites del plan gratuito de Gemini

---

## 📊 Monitoreo de tu App

### Ver Logs

1. Ve a tu app en Streamlit Cloud
2. Haz clic en **"☰ Manage app"**
3. Selecciona **"Logs"**
4. Aquí verás todos los errores y mensajes de la app

### Ver Métricas

En el dashboard de Streamlit Cloud puedes ver:
- 📈 Número de visitantes
- ⏱️ Tiempo de actividad
- 🔄 Número de reinicios
- 💾 Uso de recursos

---

## 🔄 Actualizar tu App

Cada vez que hagas cambios en tu código:

```bash
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

**Streamlit Cloud detectará los cambios automáticamente** y redespliegará tu app en 1-2 minutos.

---

## 💰 Límites del Plan Gratuito

### Streamlit Community Cloud (Gratuito)
- ✅ 1 app privada
- ✅ Apps públicas ilimitadas
- ✅ 1 GB de RAM por app
- ✅ 1 CPU compartida
- ✅ Despliegues ilimitados

### Google Gemini API (Gratuito)
- ✅ 15 solicitudes por minuto
- ✅ 1,500 solicitudes por día
- ✅ 1 millón de tokens por mes

> 💡 **Tip**: Para la mayoría de los casos de uso educativo, estos límites son más que suficientes.

---

## 🎓 Próximos Pasos

Una vez que tu app esté desplegada:

1. **Comparte la URL** con tus estudiantes o amigos
2. **Recopila feedback** sobre la experiencia de usuario
3. **Itera y mejora** basándote en el uso real
4. **Considera agregar**:
   - Análisis de diferentes tipos de problemas
   - Soporte para más materias
   - Sistema de progreso del estudiante
   - Exportación de conversaciones

---

## 📚 Recursos Adicionales

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Documentación de Google Gemini](https://ai.google.dev/docs)
- [Comunidad de Streamlit](https://discuss.streamlit.io/)
- [Ejemplos de Apps Streamlit](https://streamlit.io/gallery)

---

## 🆘 ¿Necesitas Ayuda?

Si tienes problemas:

1. **Revisa los logs** en Streamlit Cloud
2. **Consulta esta guía** de solución de problemas
3. **Busca en la documentación** oficial
4. **Abre un issue** en el repositorio de GitHub
5. **Pregunta en la comunidad** de Streamlit

---

¡Felicidades! 🎉 Tu aplicación MateTutor ya está en la nube y lista para ayudar a estudiantes a prepararse para el ICFES.

**¡Comparte tu app y ayuda a más estudiantes a aprender matemáticas!** 🚀📚

