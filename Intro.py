import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# --- Título y descripción ---
st.markdown(
    """
    <h1 style='text-align:center;'>Portafolio Multimodales</h1>
    <p style='text-align:center; font-size:18px;'>Descripción de los trabajos</p>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
with st.sidebar:
    st.subheader("Portafolio Multimodales - Camila Vergara")
    st.write("Aquí podremos ver los diferentes códigos trabajados en el semestre.")

# --- Datos de los proyectos ---
proyectos = [
    {
        "titulo": "Intro",
        "descripcion": "Primera página del portafolio.",
        "imagen": "image_2025-10-23_000052698.png",
        "url": "https://primerpaginacami.streamlit.app"
    },
    {
        "titulo": "Conversión voz a texto",
        "descripcion": "Aplicación que convierte voz a texto.",
        "imagen": "image_2025-10-22_235920847.png",
        "url": "https://traductoridioma.streamlit.app"
    },
    {
        "titulo": "Texto a voz",
        "descripcion": "Conversión de texto a audio.",
        "imagen": "image_2025-10-23_000022811.png",
        "url": "https://cuentodelgato.streamlit.app/"
    },
    {
        "titulo": "Análisis texto inglés",
        "descripcion": "Análisis de texto en inglés.",
        "imagen": "image_2025-10-22_235720040.png",
        "url": "https://txingles.streamlit.app"
    },
    {
        "titulo": "Reconocimiento OCR",
        "descripcion": "Reconocimiento de caracteres en imagen.",
        "imagen": "image_2025-10-22_235834591.png",
        "url": "https://audio-ocr.streamlit.app"
    },
    {
        "titulo": "Objetos en imagen",
        "descripcion": "Reconocimiento de objetos.",
        "imagen": "image_2025-10-22_235633240.png",
        "url": "https://yolocami.streamlit.app"
    },
    {
        "titulo": "Reconocimiento de gestos",
        "descripcion": "Detección de gestos.",
        "imagen": "image_2025-10-22_235547846.png",
        "url": "https://tmcami.streamlit.app"
    },
    {
        "titulo": "Análisis texto español",
        "descripcion": "Análisis de texto en español.",
        "imagen": "image_2025-10-22_235806012.png",
        "url": "https://txespanol.streamlit.app"
    },
    {
        "titulo": "Tablero inteligente",
        "descripcion": "Interfaz de análisis con voz.",
        "imagen": "image_2025-10-22_235148140.png",
        "url": "https://bocetostablero.streamlit.app"
    },
    {
        "titulo": "Control por voz",
        "descripcion": "Control de voz con MQTT.",
        "imagen": "ctrlvoz.png",
        "url": "https://controlador-voz.streamlit.app"
    }
]

# --- Mostrar en cuadrícula ---
cols = st.columns(5)
for i, proyecto in enumerate(proyectos):
    with cols[i % 5]:
        st.image(Image.open(proyecto["imagen"]), use_container_width=True)
        st.markdown(
            f"<p style='text-align:center; font-weight:bold; font-style:italic;'>{proyecto['titulo']}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='text-align:center;'>{proyecto['descripcion']}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='text-align:center; color:#00AEEF; font-style:italic;'>[Enlace]({proyecto['url']})</p>",
            unsafe_allow_html=True
        )

