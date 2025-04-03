import streamlit as st
import requests

# API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

col1, col2 = st.columns([3,1])


with col1:
    st.markdown("")  # Espacio vacío para dejar la imagen sola en la fila

# Ahora crea otra fila para centrar el texto debajo
st.markdown("<h1 style='text-align: center; margin-top: 20px;'>Agente Habicredit</h1>", unsafe_allow_html=True)


st.markdown("""
    <style>
    .stform_submit_button>button:hover {
        background-color: #7cdb91; /* Green */
        color: #7cdb91;
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

def connect_api(query):
    BASE_API_URL = "https://api.langflow.astra.datastax.com"
    LANGFLOW_ID = "40e98986-3486-471e-8c5d-6a27d01f3d78"
    FLOW_ID = "a4bb8b81-8469-4cd6-8898-d31597bed217"
    APPLICATION_TOKEN = "AstraCS:zwxnTFZtyOUjGKTsnljsrSZc:72bb72b2f2e9336a259fc81e62b194201f59959dc6cf38a766e0af0f9b9a5eb2"
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "input_value": query,
        "output_type": "chat",
        "input_type": "chat"
    }

    responses = requests.post(f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}", json=payload, headers=headers, timeout=90) 
    return responses
    

# Usa st.form para agrupar el input y botón
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    response = connect_api(query)
    data = response.json()
    data = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    
    if response.status_code == 200:
        st.write("🔍 Respuesta:", data)
                 #response.json().get("response", "⚠️ No 'response' key found in JSON."))
    else:
        st.error(f"❌ API Error: {response.status_code}")
