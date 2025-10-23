import streamlit as st
from PIL import Image
st.title("Portafolio Multimodales")

with st.sidebar:
  st.subheader("Portafolio Multimodales - Camila Vergara")
  parrafo = (
    "Aqui podremos ver los diferentes codigos trabajados en el semestre "
  )
  st.write(parrafo)

url_ia = "https://sites.google.com/view/interfacesmultimodales/página-principalo"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# Primera fila de columnas
col1, col2, col3 = st.columns(3)

with col1:
 st.subheader("Intro")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlase se vera la primera pagina") 
 url = "https://primerpaginacami.streamlit.app"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Texto a Voz")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera la creacion de texto a voz") 
 url = "https://cuentodelgato.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Traductors")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera como traduce un audio.") 
 url = "https://traductoridioma.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductor-ab0sp9f6fi.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres OCR")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://audio-ocr.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Analisis de texto - Español")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://txespanol.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")

with col3: 
 st.subheader("Analisis de texto - Ingles")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://txingles.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Objetos en imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://yolocami.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Reconocimiento de gestos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://tmcami.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

col4, col5 = st.columns(2)

with col4:
 st.subheader("Chad PDF")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlase se vera la primera pagina") 
 url = "https://un-pdfchat.streamlit.app"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Interpretacíon de imagen")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera la creacion de texto a voz") 
 url = "https://renocimientoimagenes.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Tablero personalizado")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera como traduce un audio.") 
 url = "https://tablerodibujoo.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col5: 
 st.subheader("Tablero Inteligente")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://bocetostablero.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Lector de Sensor MQTT")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://recepprocess.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("CONTROL POR VOZ")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://controlador-voz.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")
