# ✅ Checklist de Despliegue - MateTutor en Streamlit Cloud

Usa este checklist para asegurarte de que todo está listo antes de desplegar.

## 📋 Pre-Despliegue

### 1. Archivos Necesarios

- [ ] `streamlit_app.py` existe y está completo
- [ ] `requirements.txt` existe con todas las dependencias
- [ ] `.streamlit/config.toml` existe con la configuración del tema
- [ ] `README.md` está actualizado con instrucciones
- [ ] `.gitignore` incluye `.streamlit/secrets.toml`

### 2. Código

- [ ] El código no tiene errores de sintaxis
- [ ] No hay imports faltantes
- [ ] Las rutas de archivos son correctas
- [ ] El prompt del tutor está correctamente definido

### 3. API Key de Google Gemini

- [ ] Tienes una cuenta de Google
- [ ] Has obtenido tu API key de [Google AI Studio](https://aistudio.google.com/app/apikey)
- [ ] Has copiado y guardado tu API key en un lugar seguro
- [ ] **NO** has subido tu API key al repositorio

### 4. GitHub

- [ ] Tu código está en un repositorio de GitHub
- [ ] El repositorio es público (o tienes Streamlit Cloud Pro para repos privados)
- [ ] Has hecho push de todos los cambios recientes
- [ ] La rama principal se llama `main` o `master`

## 🚀 Durante el Despliegue

### 5. Streamlit Cloud

- [ ] Has creado una cuenta en [Streamlit Cloud](https://share.streamlit.io/)
- [ ] Has conectado tu cuenta de GitHub
- [ ] Has autorizado a Streamlit Cloud a acceder a tu repositorio

### 6. Configuración de la App

- [ ] Has seleccionado el repositorio correcto
- [ ] Has seleccionado la rama correcta (`main`)
- [ ] Has especificado `streamlit_app.py` como archivo principal
- [ ] Has configurado el secret `GEMINI_API_KEY` en Advanced Settings

### 7. Secrets

Verifica que el formato sea exactamente:
```toml
GEMINI_API_KEY = "tu-api-key-aquí"
```

- [ ] No hay espacios extra antes o después del `=`
- [ ] La API key está entre comillas dobles
- [ ] No hay saltos de línea extra
- [ ] Has reemplazado `"tu-api-key-aquí"` con tu API key real

## ✅ Post-Despliegue

### 8. Verificación Básica

- [ ] La app se desplegó sin errores
- [ ] La página carga correctamente
- [ ] Se muestra el mensaje de bienvenida de MateTutor
- [ ] No hay errores visibles en la interfaz

### 9. Pruebas Funcionales

- [ ] Puedes escribir un mensaje y recibir respuesta
- [ ] El streaming de respuestas funciona correctamente
- [ ] Puedes subir una imagen (PNG, JPG, JPEG)
- [ ] La imagen se procesa y el modelo responde sobre ella
- [ ] El botón "Limpiar conversación" funciona
- [ ] El historial del chat se mantiene durante la sesión

### 10. Pruebas de Contenido

Prueba con estos ejemplos:

- [ ] **Texto simple**: "¿Cómo resuelvo ecuaciones de segundo grado?"
  - ✅ Debe responder con preguntas socráticas, no dar la respuesta directa

- [ ] **Imagen**: Sube una foto de un problema matemático
  - ✅ Debe reconocer el problema y hacer preguntas guía

- [ ] **Texto + Imagen**: Escribe "Ayúdame con este problema" y sube una imagen
  - ✅ Debe combinar ambos inputs en su respuesta

### 11. Pruebas de Errores

- [ ] Enviar mensaje vacío (sin texto ni imagen)
  - ✅ No debe hacer nada o mostrar un mensaje apropiado

- [ ] Subir un archivo no válido (si es posible)
  - ✅ Debe mostrar un error claro

- [ ] Hacer muchas preguntas seguidas
  - ✅ El historial debe mantenerse coherente

### 12. Rendimiento

- [ ] La primera respuesta llega en menos de 10 segundos
- [ ] Las respuestas subsecuentes son más rápidas
- [ ] El streaming es fluido (no se congela)
- [ ] La app no se cae después de varias interacciones

### 13. Diseño y UX

- [ ] Los colores coinciden con el diseño esperado (azul #007bff)
- [ ] Los mensajes del usuario están alineados a la derecha (azul)
- [ ] Los mensajes del asistente están alineados a la izquierda (gris)
- [ ] Las imágenes se muestran correctamente en el chat
- [ ] La fuente Lexend se carga correctamente
- [ ] La app se ve bien en móvil (responsive)

### 14. Seguridad

- [ ] Tu API key NO está visible en el código fuente
- [ ] El archivo `secrets.toml` NO está en el repositorio
- [ ] El `.gitignore` incluye `secrets.toml`
- [ ] No hay información sensible en los logs públicos

## 🔧 Configuración Opcional

### 15. Personalización (Opcional)

- [ ] Has personalizado la URL de la app
- [ ] Has agregado un favicon personalizado
- [ ] Has modificado los colores del tema según tus preferencias
- [ ] Has actualizado el README con tu información

### 16. Monitoreo (Opcional)

- [ ] Has revisado los logs en Streamlit Cloud
- [ ] Has configurado notificaciones de errores
- [ ] Has verificado las métricas de uso

### 17. Documentación (Opcional)

- [ ] Has compartido la URL con tu equipo
- [ ] Has documentado cualquier cambio personalizado
- [ ] Has creado issues para mejoras futuras

## 🐛 Solución de Problemas

Si algo no funciona, verifica:

### Error: "GEMINI_API_KEY not found"
- [ ] Revisa que el secret esté configurado en Streamlit Cloud
- [ ] Verifica el formato del secret (sin espacios extra)
- [ ] Reinicia la app desde el dashboard

### Error: "Module not found"
- [ ] Verifica que `requirements.txt` esté completo
- [ ] Asegúrate de que las versiones sean compatibles
- [ ] Revisa los logs para ver qué módulo falta

### La app no responde
- [ ] Verifica los logs en Streamlit Cloud
- [ ] Comprueba tu cuota de API de Gemini
- [ ] Reinicia la app desde el dashboard

### Las imágenes no se procesan
- [ ] Verifica que el formato sea PNG, JPG o JPEG
- [ ] Comprueba que el tamaño no sea excesivo (< 10MB)
- [ ] Revisa los logs para errores específicos

## 📊 Métricas de Éxito

Tu despliegue es exitoso si:

- ✅ La app está accesible públicamente
- ✅ Todas las funcionalidades principales funcionan
- ✅ No hay errores críticos en los logs
- ✅ Los usuarios pueden interactuar sin problemas
- ✅ El tiempo de respuesta es aceptable (< 10s)

## 🎉 ¡Felicidades!

Si has completado todos los items del checklist, ¡tu app está lista para producción!

### Próximos Pasos:

1. **Comparte tu app** con estudiantes o colegas
2. **Recopila feedback** sobre la experiencia
3. **Itera y mejora** basándote en el uso real
4. **Monitorea** el uso y los errores regularmente

### Recursos Útiles:

- 📖 [README.md](README.md) - Documentación completa
- 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) - Guía detallada de despliegue
- 📝 [MIGRATION_NOTES.md](MIGRATION_NOTES.md) - Notas técnicas de migración

---

**¿Encontraste algún problema?** Abre un issue en GitHub o consulta la documentación.

**¿Todo funcionó perfecto?** ¡Comparte tu experiencia y ayuda a otros! 🌟

