import streamlit as st
import random
import time

st.title("Bot Musico 🎶")

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes previos en la aplicación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceptar la entrada del usuario
if prompt := st.chat_input("¿Cual es tu cantante favorita? 🎧"):
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Respuestas predefinidas relacionadas con la música
    responses = [
        "La música tiene el poder de mover nuestras emociones.",
        "¿Sabías que Beethoven compuso su novena sinfonía estando sordo?",
        "La música puede ayudar a reducir el estrés. ¿Te gustaría escuchar algo tranquilo?",
        "¿Tienes algún género musical favorito? ¡Puedo recomendarte algo!"
    ]

    # Seleccionar una respuesta aleatoria
    response = random.choice(responses)

    # Mostrar la respuesta del bot en el contenedor de mensajes
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Simulación de escritura gradual
        for word in response.split():
            full_response += word + " "
            message_placeholder.markdown(full_response)
            time.sleep(0.05)

    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": response})
