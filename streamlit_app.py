import streamlit as st
import requests
import json

# API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL


# Inicializa variables de sesión
if "feedback" not in st.session_state:
    st.session_state.feedback = None
if "response_shown" not in st.session_state:
    st.session_state.response_shown = False
if "respuesta" not in st.session_state:
    st.session_state.respuesta = ""

col1, col2 = st.columns([3,1])

with col1:
    st.markdown("")  # Espacio vacío para dejar la imagen sola en la fila

with col2:
    st.image("logohabi.png", width=250)

    
# Ahora crea otra fila para centrar el texto debajo
st.markdown("<h1 style='text-align: center; margin-top: 20px;'>Agente Habicredit</h1>", unsafe_allow_html=True)


st.markdown("""
    <style>
    .stform_submit_button>button:hover {
        background-color: #7cdb91; /* Green */
        color: #7cdb91;
        #background-color: #B86FFF !important;
    }


/* New CSS for changing the shadow color of the text input when hovered */
.stTextInput>div>div>input:hover {
    box-shadow: 2px 2px 5px rgba(0,255,0,0.75); /* Green shadow when hovered */
}

    .stButton button:focus {
        border: 2px solid #7cdb91; /* Green border color when focused */
        color: #7cdb91; /* Green text color when focused */
    }

    /* CSS for changing the border color and shadow of the text input box */
    .stTextInput>div>div>input {
        border: 2px solid #7C01FF; /* Blue border color */
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Default shadow */
        #border: 2px solid #7C01FF !important;       /* Contorno morado */
        #box-shadow: 2px 2px 5px rgba(124,1,255,0.5);
    }

    /* New CSS for changing the shadow color of the text input when hovered */
    .stTextInput>div>div>input:hover {
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Red shadow when hovered */
    }

    /* CSS for changing the border color and shadow of the text input box when focused */
    .stTextInput>div>div>input:focus {
        border: 2px solid #7C01FF; /* Red border color when focused */
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Red shadow when focused */
    }
    </style>
    """, unsafe_allow_html=True)
def calification_user(query, answer, feedback):
    headers = {
        "x-api-key": "AIzaSyBb2222222-1111111111",
        "Content-Type": "application/json",
        "Origin": "https://mi-app.streamlit.app"
    }
    payload = json.dumps({
        "data": {
            "question": query,
            "response": answer,
            "feedback": feedback
        }
    })
    #responses = requests.post("https://agent-gateway-ak877eu7.uc.gateway.dev/streamlit/event", headers=headers, data=payload)
    return 200
    
    
def connect_api(query):
    #BASE_API_URL = "https://api.langflow.astra.datastax.com"
    #LANGFLOW_ID = "40e98986-3486-471e-8c5d-6a27d01f3d78"
    #FLOW_ID = "a4bb8b81-8469-4cd6-8898-d31597bed217"
    #APPLICATION_TOKEN = "AstraCS:zwxnTFZtyOUjGKTsnljsrSZc:72bb72b2f2e9336a259fc81e62b194201f59959dc6cf38a766e0af0f9b9a5eb2"
    
    headers = {
        "x-api-key": "AIzaSyBb2222222-1111111111",
        "Content-Type": "application/json",
        "Origin": "https://mi-app.streamlit.app"
    }
    
    payload = json.dumps({
        "data": {"question": query}
    })

    responses = requests.post("https://agent-gateway-ak877eu7.uc.gateway.dev/streamlit/event", headers=headers, data=payload)
    return responses
    

# Usa st.form para agrupar el input y botón 
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    #st.session_state.feedback = None
    #st.session_state.response_shown = False
    #st.session_state.respuesta = ""
    #st.session_state.last_rating = None  # Reinicia calificación
    #st.session_state.pop("last_rating", None)

    
    response_api = connect_api(query)
    st.session_state.rating = None
    st.session_state.feedback = None
    st.session_state.response_shown = False
    st.session_state.score_ready = False
    
    if response_api.status_code != 200:
        st.write("⚠️ Error HTTP:", response_api.status_code)
        st.write("Texto de respuesta:", response_api.text)
        st.write("⚠️ No 'response' key found in JSON.", response_api)
    else:
        st.session_state.respuesta = response_api.text
        st.session_state.response_shown = True
        #data = response_api.text
        #st.write(data)

# Mostrar respuesta y botones de calificación
if st.session_state.get("response_shown"):
    st.markdown(f"**💬 Respuesta:** {st.session_state.respuesta}")

    # Determinar si se debe deshabilitar el selector
    disabled = st.session_state.score_ready

    #col_like, col_dislike = st.columns([1, 1])
    #with col_like:
    #    if st.button("👍 Me gusta"):
    #        st.session_state.feedback = "like"
    #with col_dislike:
    #    if st.button("👎 No me gusta"):
    #        st.session_state.feedback = "dislike"

    # Mostrar selector de estrellas
    rating = st.radio(
        "⭐ ¿Qué tan buena fue la respuesta?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x, 
        horizontal=True,
        key="rating",
        disabled=disabled
    )
    
    
    # Mostrar estado de calificación
    #if st.session_state.feedback == "like":
    #    calification_user(query,st.session_state.respuesta,"1")
    #    st.success("Has calificado esta respuesta como: 👍 Me gusta")
    #elif st.session_state.feedback == "dislike":
    #    calification_user(query,st.session_state.respuesta,"0")
    #    st.warning("Has calificado esta respuesta como: 👎 No me gusta")

    # Guardar calificación automáticamente solo una vez
    if not disabled and rating:
        st.success(f"Has calificado esta respuesta con: {'⭐' * rating}")
        st.session_state.feedback = rating
        st.session_state.score_ready = True
        calification_user(query, st.session_state.respuesta, str(rating))
    
