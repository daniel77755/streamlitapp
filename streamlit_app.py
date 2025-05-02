import streamlit as st
import requests
import json

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
    #BASE_API_URL = "https://api.langflow.astra.datastax.com"
    #LANGFLOW_ID = "40e98986-3486-471e-8c5d-6a27d01f3d78"
    #FLOW_ID = "a4bb8b81-8469-4cd6-8898-d31597bed217"
    #APPLICATION_TOKEN = "AstraCS:zwxnTFZtyOUjGKTsnljsrSZc:72bb72b2f2e9336a259fc81e62b194201f59959dc6cf38a766e0af0f9b9a5eb2"
    headers = {
        "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjA3YjgwYTM2NTQyODUyNWY4YmY3Y2QwODQ2ZDc0YThlZTRlZjM2MjUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA0MTMzMzIzMTQyODMyNTkyOTQ3IiwiaGQiOiJoYWJpLmNvIiwiZW1haWwiOiJqZWlubmVyYmFlekBoYWJpLmNvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJNZVY2NVJsLTZRblRweDgwb2F2bnd3IiwibmJmIjoxNzQ2MjAxNjUxLCJpYXQiOjE3NDYyMDE5NTEsImV4cCI6MTc0NjIwNTU1MSwianRpIjoiNWNmZDEyMmU5OGUxM2U3OTE0OTYyMjY3ZmQ5MjMxMzQyMjBiMjUwNCJ9.PcjzdJvJ9bPDXL6G8OFttLr2cAadQ1-lcJ8R48Wp25Ip5CCzpyNB3cQjqjc6K3TADe367REH2kfssYHrtleuzO-zyTkB2exF-ANf8vF25ccvn2ObMZEhbcHTAhsLOVYhA-XAwq0-GtdGyPgAYfqEcNij2sGr6P2-QYqDMj7Sd3s7_wfN7uFEw20VeHziy7F5H5tiHDs-aY6-R6nJvMt_PrTZPBbXNXwEvFbvU1lFCLPktdJp0AOh3O2WmHWdbyF5aFbzZYgy8NMAbeROp_Ili-6Pxvy4BB0wCO-Hs7LYUt5gP9V3SJRnybbxneoEVBaA30Q3i46QCWJ286KQlpCpmA",
        "Content-Type": "application/json",
        "Origin": "https://mi-app.streamlit.app"
    }
    
    payload = json.dumps({
        "data": {"question": query}
    })

    responses = requests.post("https://endpoint-ai-agent-bi-827673120223.us-central1.run.app", headers=headers, data=payload) 
    return responses
    

# Usa st.form para agrupar el input y botón
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    response_api = connect_api(query)
    st.write(response_api)
    if response_api.status_code != 200:
        st.write("⚠️ Error HTTP:", response_api.status_code)
        st.write("Texto de respuesta:", response_api.text)
        st.write("⚠️ No 'response' key found in JSON.", response_api)
    else:
        data = response_api.text
        st.write(data)
        #data = response_api.json()
        #st.write(data)
        #data = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        #st.write(data)
