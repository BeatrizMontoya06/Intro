import streamlit as st
from PIL import Image

st.title("Hola mi nombres es Bea")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('mono.jpg')
st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)


st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoras la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta esl a segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Tactil'))
  if modo == 'Visual':
