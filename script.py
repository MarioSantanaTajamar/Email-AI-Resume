import streamlit as st
import os
import openai
from openai import AzureOpenAI
import tiktoken
from dotenv import load_dotenv
load_dotenv()

# para correr el programa
# streamlit run script.py        
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-02-15-preview"
)

st.title("App de Email :sunglasses:")

def resumir_email(email_texto):
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini", 
            messages = [
                {"role": "system", "content": "Resume el siguiente correo electrónico de manera concisa, pon autor:(el emisor), tema:(el tema del correo) y contenido:(contenido resumido) "},
                {"role": "user", "content": email_texto},
            ],
            temperature=0
        )
        resumen = response.choices[0].message.content
        return resumen
    except Exception as e:
        st.error(f"Error al generar el resumen: {e}")
        return None

# Interfaz de usuario con Streamlit
st.title('Resumen de Correos Electrónicos')

email_input = st.text_area('Introduce el contenido del correo electrónico:', height=200)

if st.button('Resumir'):
    if email_input:
        resumen = resumir_email(email_input)
        if resumen:
            st.subheader('Resumen:')
            st.write(resumen)
    else:
        st.error('Por favor, introduce el contenido del correo electrónico.')
