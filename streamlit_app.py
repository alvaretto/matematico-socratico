"""
MateTutor - Tu Tutor de Matemáticas para el ICFES
Aplicación Streamlit que usa Google Gemini AI para tutorías de matemáticas
"""

import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import base64

# Configuración de la página
st.set_page_config(
    page_title="MateTutor - Tu Tutor de ICFES",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Prompt del tutor (mismo que en la versión original)
MATE_TUTOR_PROMPT = """Eres "MateTutor", un tutor de matemáticas amigable y paciente. Un estudiante te va a mostrar una pregunta de la prueba ICFES en la que está atascado.

Tu objetivo NO es darle la respuesta. Tu objetivo es guiarlo para que la descubra por sí mismo. Sigue estos pasos rigurosamente:
1.  Saluda al estudiante amablemente y pídele que te explique qué ha intentado hasta ahora y dónde cree que está el problema. NO resuelvas ni expliques el problema en tu primer mensaje. Solo pregunta.
2.  Basado en su respuesta, hazle preguntas socráticas para que identifique los datos clave del problema. (Ej: "¿Qué información te da el gráfico?", "¿Qué significa 'promedio'?", "¿Qué fórmula crees que podría ser útil aquí?").
3.  Si está completamente perdido, dale una pequeña pista o un ejemplo más sencillo del mismo concepto. No le des la respuesta directamente.
4.  ¡Sé siempre positivo y anímalo a seguir intentando! Usa emojis para hacer la conversación más amigable. 😃👍🎉"""

# CSS personalizado para mantener el diseño similar al original
st.markdown("""
<style>
    /* Importar fuente Lexend */
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600&display=swap');
    
    /* Aplicar fuente a toda la app */
    html, body, [class*="css"] {
        font-family: 'Lexend', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo del contenedor principal */
    .stApp {
        background-color: #f0f4f8;
    }
    
    /* Estilo del header */
    .main-header {
        text-align: center;
        padding: 1.5rem;
        background-color: white;
        border-bottom: 1px solid #dee2e6;
        border-radius: 10px 10px 0 0;
        margin-bottom: 1rem;
    }
    
    .main-header h1 {
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        margin: 0;
    }
    
    .main-header p {
        color: #667;
        font-size: 0.95rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Estilo de los mensajes del chat */
    .stChatMessage {
        background-color: transparent !important;
    }
    
    /* Mensajes del usuario */
    [data-testid="stChatMessageContent"] {
        background-color: #007bff;
        color: white;
        border-radius: 18px;
        padding: 0.75rem 1rem;
        max-width: 80%;
    }
    
    /* Mensajes del asistente */
    .stChatMessage[data-testid="chat-message-assistant"] [data-testid="stChatMessageContent"] {
        background-color: #e9ecef;
        color: #212529;
    }
    
    /* Área de input */
    .stChatInputContainer {
        border-top: 1px solid #dee2e6;
        background-color: #f0f4f8;
        padding: 1rem;
    }
    
    /* Botón de enviar */
    .stChatInputContainer button {
        background-color: #007bff !important;
        color: white !important;
        border-radius: 50% !important;
    }
    
    .stChatInputContainer button:hover {
        background-color: #0056b3 !important;
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid #dee2e6;
    }
    
    /* Imágenes en mensajes */
    .stChatMessage img {
        border-radius: 10px;
        max-width: 100%;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="main-header">
    <h1>¡Hola! Soy MateTutor 🧠</h1>
    <p>Tu tutor de matemáticas para el ICFES.</p>
</div>
""", unsafe_allow_html=True)

# Inicializar el estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat = None
    st.session_state.api_key_configured = False

# Configurar la API de Gemini
def configure_gemini():
    """Configura la API de Gemini con la clave de Streamlit Secrets"""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        st.session_state.api_key_configured = True
        return True
    except Exception as e:
        st.error(f"⚠️ Error al configurar la API de Gemini: {str(e)}")
        st.info("💡 Asegúrate de configurar `GEMINI_API_KEY` en los Secrets de Streamlit.")
        return False

# Inicializar el chat de Gemini
def initialize_chat():
    """Inicializa el chat de Gemini con el prompt del sistema"""
    if st.session_state.chat is None:
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            system_instruction=MATE_TUTOR_PROMPT
        )
        st.session_state.chat = model.start_chat(history=[])

# Convertir imagen a formato compatible con Gemini
def process_image(uploaded_file):
    """Procesa la imagen subida y la convierte al formato de Gemini"""
    try:
        image = Image.open(uploaded_file)
        return image
    except Exception as e:
        st.error(f"Error al procesar la imagen: {str(e)}")
        return None

# Configurar Gemini al inicio
if not st.session_state.api_key_configured:
    if not configure_gemini():
        st.stop()

# Inicializar el chat
initialize_chat()

# Mostrar mensaje de bienvenida si no hay mensajes
if len(st.session_state.messages) == 0:
    welcome_message = "¡Hola! Soy MateTutor 😃. Muéstrame esa pregunta de matemáticas en la que necesitas ayuda. ¡Puedes escribirla o subir una imagen y juntos la resolveremos paso a paso!"
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})

# Mostrar historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Mostrar imagen si existe
        if "image" in message:
            st.image(message["image"], use_container_width=True)

# Widget para subir imágenes (fuera del chat input)
uploaded_file = st.file_uploader(
    "📎 Adjuntar imagen de la pregunta (opcional)",
    type=["png", "jpg", "jpeg"],
    help="Sube una imagen de la pregunta del ICFES"
)

# Input del usuario
if prompt := st.chat_input("Escribe tu pregunta o describe la imagen..."):
    # Preparar el contenido del mensaje
    message_content = prompt
    message_parts = [prompt]
    
    # Procesar imagen si fue subida
    image_to_display = None
    if uploaded_file is not None:
        image = process_image(uploaded_file)
        if image:
            image_to_display = image
            message_parts.append(image)
    
    # Agregar mensaje del usuario al historial
    user_message = {"role": "user", "content": message_content}
    if image_to_display:
        user_message["image"] = image_to_display
    st.session_state.messages.append(user_message)
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(message_content)
        if image_to_display:
            st.image(image_to_display, use_container_width=True)
    
    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Enviar mensaje a Gemini con streaming
            response = st.session_state.chat.send_message(message_parts, stream=True)
            
            # Mostrar respuesta en streaming
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
            
            # Mostrar respuesta final
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            error_message = "Lo siento, algo salió mal. Por favor, intenta de nuevo. 😔"
            message_placeholder.markdown(error_message)
            full_response = error_message
            st.error(f"Error: {str(e)}")
    
    # Agregar respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # Limpiar el file uploader después de enviar (rerun)
    st.rerun()

# Botón para limpiar el chat (en la barra lateral)
with st.sidebar:
    st.markdown("### ⚙️ Opciones")
    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = None
        initialize_chat()
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
    ### 📚 Acerca de MateTutor
    
    MateTutor es un tutor de matemáticas que usa el método socrático para ayudarte a resolver problemas del ICFES.
    
    **No te dará las respuestas directamente**, sino que te guiará con preguntas para que descubras la solución por ti mismo.
    
    ¡Así aprenderás mejor! 🎓
    """)
    
    st.markdown("---")
    st.markdown("Desarrollado con ❤️ usando Streamlit y Google Gemini AI")

