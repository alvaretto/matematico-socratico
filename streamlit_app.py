"""
MateTutor - Tu Tutor de Matemáticas para el ICFES
Aplicación Streamlit que usa Groq + Llama 3.2 Vision para tutorías de matemáticas
"""

import streamlit as st
from groq import Groq
from PIL import Image
import base64
import io

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
    st.session_state.groq_client = None
    st.session_state.api_key_configured = False

# Configurar la API de Groq
def configure_groq():
    """Configura el cliente de Groq con la clave de Streamlit Secrets"""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        st.session_state.groq_client = Groq(api_key=api_key)
        st.session_state.api_key_configured = True
        return True
    except Exception as e:
        st.error(f"⚠️ Error al configurar la API de Groq: {str(e)}")
        st.info("💡 Asegúrate de configurar `GROQ_API_KEY` en los Secrets de Streamlit.")
        return False

# Convertir imagen a base64
def image_to_base64(image):
    """Convierte una imagen PIL a base64"""
    try:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        st.error(f"Error al convertir imagen: {str(e)}")
        return None

# Configurar Groq al inicio
if not st.session_state.api_key_configured:
    if not configure_groq():
        st.stop()

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

# Widget para subir imágenes
uploaded_file = st.file_uploader(
    "📎 Sube una imagen del problema (opcional)",
    type=["png", "jpg", "jpeg"],
    help="Sube una foto de la pregunta del ICFES"
)

# Si hay una imagen subida, mostrar preview y botón
if uploaded_file is not None:
    col1, col2 = st.columns([3, 1])

    with col1:
        st.image(uploaded_file, caption="Vista previa", width=300)

    with col2:
        st.write("")  # Espaciado
        st.write("")  # Espaciado
        if st.button("📤 Analizar Imagen", type="primary", use_container_width=True, key="analyze_btn"):
            # Procesar imagen
            try:
                image = Image.open(uploaded_file)
                image_base64 = image_to_base64(image)

                if not image_base64:
                    st.error("No se pudo procesar la imagen")
                    st.stop()

                # Agregar mensaje del usuario
                st.session_state.messages.append({
                    "role": "user",
                    "content": "📷 [Imagen del problema]",
                    "image": image
                })

                # Generar respuesta con Groq
                with st.spinner("🤔 Analizando la imagen con Llama Vision..."):
                    response = st.session_state.groq_client.chat.completions.create(
                        model="llama-3.2-90b-vision-preview",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": f"{MATE_TUTOR_PROMPT}\n\nAyúdame con este problema de matemáticas. Recuerda usar el método socrático y no dar la respuesta directa."
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": image_base64
                                        }
                                    }
                                ]
                            }
                        ],
                        temperature=0.7,
                        max_tokens=2048
                    )

                    if response.choices[0].message.content:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response.choices[0].message.content
                        })
                    else:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": "No pude analizar la imagen. ¿Puedes intentar con otra foto más clara?"
                        })

                st.rerun()

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Verifica tu API key de Groq o intenta con otra imagen.")

# Input del usuario (texto)
if prompt := st.chat_input("Escribe tu pregunta de matemáticas..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generar respuesta con Groq
    try:
        # Preparar historial de mensajes para Groq
        groq_messages = []

        # Agregar el prompt del sistema como primer mensaje del usuario si es el primero
        if len(st.session_state.messages) == 1:
            groq_messages.append({
                "role": "user",
                "content": f"{MATE_TUTOR_PROMPT}\n\n{prompt}"
            })
        else:
            # Agregar mensajes previos (solo texto, sin imágenes)
            for i, msg in enumerate(st.session_state.messages[:-1]):
                if "image" not in msg:
                    # Incluir el prompt del sistema en el primer mensaje
                    if i == 0 and msg["role"] == "user":
                        groq_messages.append({
                            "role": msg["role"],
                            "content": f"{MATE_TUTOR_PROMPT}\n\n{msg['content']}"
                        })
                    else:
                        groq_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })

            # Agregar el mensaje actual
            groq_messages.append({"role": "user", "content": prompt})

        # Llamar a Groq
        response = st.session_state.groq_client.chat.completions.create(
            model="llama-3.2-90b-text-preview",
            messages=groq_messages,
            temperature=0.7,
            max_tokens=2048
        )

        assistant_response = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"Lo siento, hubo un error: {str(e)}"
        })

    st.rerun()

# Botón para limpiar el chat (en la barra lateral)
with st.sidebar:
    st.markdown("### ⚙️ Opciones")
    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    # Modo debug
    debug_mode = st.checkbox("🐛 Modo Debug", value=False)
    if debug_mode:
        st.markdown("**Estado del Sistema:**")
        st.write(f"Groq Client: {st.session_state.groq_client is not None}")
        st.write(f"API configurada: {st.session_state.api_key_configured}")
        st.write(f"Mensajes: {len(st.session_state.messages)}")

    st.markdown("---")
    st.markdown("""
    ### 📚 Acerca de MateTutor

    MateTutor es un tutor de matemáticas que usa el método socrático para ayudarte a resolver problemas del ICFES.

    **No te dará las respuestas directamente**, sino que te guiará con preguntas para que descubras la solución por ti mismo.

    ¡Así aprenderás mejor! 🎓
    """)

    st.markdown("---")
    st.markdown("Desarrollado con ❤️ usando Streamlit y Groq (Llama 3.2 Vision)")

