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

# --- Lista de proyectos ---
proyectos = [
    {
        "titulo": "Intro",
        "descripcion": "Primera página del portafolio.",
        "imagen": "image_2025-10-23_000052698.png",
        "url": "https://primerpaginacami.streamlit.app"
    },
    {
        "titulo": "Conversión de voz a texto - traductor",
        "descripcion": "Aplicación que convierte voz a texto.",
        "imagen": "image_2025-10-22_235920847.png",
        "url": "https://traductoridioma.streamlit.app"
    },
    {
        "titulo": "Análisis de texto - Inglés",
        "descripcion": "Análisis de texto en inglés.",
        "imagen": "image_2025-10-22_235720040.png",
        "url": "https://txingles.streamlit.app"
    },
    {
        "titulo": "Texto a Voz",
        "descripcion": "Conversión de texto a voz.",
        "imagen": "image_2025-10-23_000022811.png",
        "url": "https://cuentodelgato.streamlit.app/"
    },
    {
        "titulo": "Reconocimiento Óptico de Caracteres OCR",
        "descripcion": "Reconocimiento de caracteres en una imagen.",
        "imagen": "image_2025-10-22_235834591.png",
        "url": "https://audio-ocr.streamlit.app"
    },
    {
        "titulo": "Análisis de texto - Español",
        "descripcion": "Análisis semántico de texto en español.",
        "imagen": "image_2025-10-22_235806012.png",
        "url": "https://txespanol.streamlit.app"
    },
    {
        "titulo": "Objetos en imagen",
        "descripcion": "Reconocimiento de objetos mediante IA.",
        "imagen": "image_2025-10-22_235633240.png",
        "url": "https://yolocami.streamlit.app"
    },
    {
        "titulo": "Reconocimiento de gestos",
        "descripcion": "Modelo que detecta gestos en cámara.",
        "imagen": "image_2025-10-22_235547846.png",
        "url": "https://tmcami.streamlit.app"
    },
    {
        "titulo": "Chat PDF",
        "descripcion": "Analizador de documentos PDF.",
        "imagen": "image_2025-10-22_235457515.png",
        "url": "https://un-pdfchat.streamlit.app"
    },
    {
        "titulo": "Interpretación de imagen",
        "descripcion": "Aplicación de reconocimiento visual.",
        "imagen": "image_2025-10-22_235405838.png",
        "url": "https://renocimientoimagenes.streamlit.app"
    },
    {
        "titulo": "Tablero personalizado",
        "descripcion": "Tablero de caracteres personalizado.",
        "imagen": "image_2025-10-22_235245016.png",
        "url": "https://tablerodibujoo.streamlit.app"
    },
    {
        "titulo": "Tablero Inteligente",
        "descripcion": "Tablero que analiza comandos por voz.",
        "imagen": "image_2025-10-22_235148140.png",
        "url": "https://bocetostablero.streamlit.app"
    },
    {
        "titulo": "Lector de Sensor MQTT",
        "descripcion": "Lectura y análisis de datos vía MQTT.",
        "imagen": "image_2025-10-22_235030401.png",
        "url": "https://recepprocess.streamlit.app"
    },
    {
        "titulo": "Control por Voz",
        "descripcion": "Control de sistemas mediante comandos de voz.",
        "imagen": "ctrlvoz.png",
        "url": "https://controlador-voz.streamlit.app"
    }
]

# --- Mostrar en cuadrícula ---
num_cols = 5
cols = st.columns(num_cols)

for i, proyecto in enumerate(proyectos):
    with cols[i % num_cols]:
        # Imagen
        st.image(Image.open(proyecto["imagen"]), use_container_width=True)
        # Título
        st.markdown(
            f"<p style='text-align:center; font-weight:bold; font-style:italic;'>{proyecto['titulo']}</p>",
            unsafe_allow_html=True
        )
        # Descripción
        st.markdown(
            f"<p style='text-align:center;'>{proyecto['descripcion']}</p>",
            unsafe_allow_html=True
        )
        # Enlace
        st.markdown(
            f"<p style='text-align:center; color:#00AEEF; font-style:italic;'>[Enlace]({proyecto['url']})</p>",
            unsafe_allow_html=True
        )
    # Cambiar de fila cada 5 columnas
    if (i + 1) % num_cols == 0:
        cols = st.columns(num_cols)
