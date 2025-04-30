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
        "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjA3YjgwYTM2NTQyODUyNWY4YmY3Y2QwODQ2ZDc0YThlZTRlZjM2MjUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA0MTMzMzIzMTQyODMyNTkyOTQ3IiwiaGQiOiJoYWJpLmNvIiwiZW1haWwiOiJqZWlubmVyYmFlekBoYWJpLmNvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJzcVM0RUxrbDdpY1A5QU1sTnM0NkxRIiwibmJmIjoxNzQ2MDIyNjUzLCJpYXQiOjE3NDYwMjI5NTMsImV4cCI6MTc0NjAyNjU1MywianRpIjoiNjg2NzE2ODgxNTFhNGQ0ODY0Zjc4MWJhYzg0MTI3OTExYzUxOWE4YSJ9.cl8EZzocHvRt1SNDfBWckmbKGQqKcBgp8EiYGOUz9Cqq6Vk0snd4zJH_xdd8Qnm8Qr3NYgaBHhZxvO6moVerz3fu5XmadIaE8UivDNwYxKexqFBbSV5q8NV4Rk2oHnwJOAlDtIFfILLYl4N8Gkbyfzm8Vkc8JVVcRKIG0lYgruAwjLTa31L6w_gAOgsgMs8zj3N3qNQqxXBUVrolvq6Lr6LKDO5zOCupxAjG_vGzoAG-3rselk5bQychGf6HmW4RcH_CCx0ZsVXxfbzrYv_MNOjS-iNmmW5YQvss8JSjK3uAS92eFxOPB1M7urp3jxPbNDxMRkX8fkWJtketdciUQw",
        "Content-Type": "application/json",
        "Origin": "https://mi-app.streamlit.app"
    }
    
    payload = json.dumps({
        "data": {"question": query}
    })

    responses = requests.post(f"https://endpoint-ai-agent-bi-mgdaz5l5xq-uc.a.run.app", headers=headers, data=payload,timeout=90) 
    return responses
    

# Usa st.form para agrupar el input y botón
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    response_api = connect_api(query)
    
    if response_api.status_code != 200:
        st.write("⚠️ No 'response' key found in JSON.", response_api)
    else:
        data = response_api.json()
        st.write(data)
        data = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        st.write(data)
