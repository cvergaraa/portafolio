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
 image = Image.open('image_2025-10-23_000052698.png')
 st.image(image, width=190)
 st.write("En el siguiente enlase se vera la primera pagina") 
 url = "https://primerpaginacami.streamlit.app"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Texto a Voz")
 image = Image.open('image_2025-10-23_000022811.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera la creacion de texto a voz") 
 url = "https://cuentodelgato.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Traductors")
 image = Image.open('image_2025-10-22_235955063.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace se vera como traduce un audio.") 
 url = "https://traductoridioma.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('image_2025-10-22_235920847.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductor-ab0sp9f6fi.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres OCR")
 image = Image.open('image_2025-10-22_235834591.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace se vera el reconocimiento de caracteres en una foto.") 
 url = "https://audio-ocr.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Analisis de texto - Español")
 image = Image.open('image_2025-10-22_235806012.png')
 st.image(image, width=200)
 st.write("Aqui se vera el analisis de texto en español") 
 url = "https://txespanol.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")

with col3: 
 st.subheader("Analisis de texto - Ingles")
 image = Image.open('image_2025-10-22_235720040.png')
 st.image(image, width=190)
 st.write("Aqui se vera el analisis de texto en ingles") 
 url = "https://txingles.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Objetos en imagen")
 image = Image.open('image_2025-10-22_235633240.png')
 st.image(image, width=200)
 st.write("Reconocimiento de objetos en imagenes") 
 url = "https://yolocami.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Reconocimiento de gestos")
 image = Image.open('image_2025-10-22_235547846.png')
 st.image(image, width=200)
 st.write("Aqui hay reconocimiento de gestos") 
 url = "https://tmcami.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

col4, col5 = st.columns(2)

with col4:
 st.subheader("Chad PDF")
 image = Image.open('image_2025-10-22_235457515.png')
 st.image(image, width=190)
 st.write("Analisis de documentos PDF") 
 url = "https://un-pdfchat.streamlit.app"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Interpretacíon de imagen")
 image = Image.open('image_2025-10-22_235405838.png')
 st.image(image, width=200)
 st.write("Interpretac'ion de imagenes.") 
 url = "https://renocimientoimagenes.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Tablero personalizado")
 image = Image.open('image_2025-10-22_235245016.png')
 st.image(image, width=200)
 st.write("Tablero personalizado de Caracteres.") 
 url = "https://tablerodibujoo.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col5: 
 st.subheader("Tablero Inteligente")
 image = Image.open('image_2025-10-22_235148140.png')
 st.image(image, width=200)
 st.write("Tablero inteligente que te contara que puede analisar.") 
 url = "https://bocetostablero.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Lector de Sensor MQTT")
 image = Image.open('image_2025-10-22_235030401.png')
 st.image(image, width=190)
 st.write("Sensor de MQTT.") 
 url = "https://recepprocess.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("CONTROL POR VOZ")
 image = Image.open('ctrlvoz.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "Control de voz con el Broker."
 st.write(f"Transcriptor: [Enlace]({url})")
