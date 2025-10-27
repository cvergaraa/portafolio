import streamlit as st
from PIL import Image

# --- Configuración general ---
st.set_page_config(layout="wide")

# --- Estilos globales (CSS) ---
st.markdown("""
    <style>
        /* Fondo general */
        .stApp {
            background-color: #CDEDFD;
            color: #0A2342;
        }

        /* Título principal */
        h1 {
            text-align: center;
            color: #0A2342;
        }

        /* Subtítulos y párrafos */
        p {
            text-align: center;
            color: #0A2342;
        }

        /* Tarjetas */
        .card {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            padding: 15px;
            margin: 10px;
        }

        /* Imagen centrada */
        .card img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 10px;
        }

        /* Texto de título de cada tarjeta */
        .titulo {
            text-align: center;
            font-weight: bold;
            font-style: italic;
            color: #0A2342;
            margin-top: 8px;
        }

        /* Descripción */
        .desc {
            text-align: center;
            color: #0A2342;
            font-size: 15px;
        }

        /* Enlace estilizado */
        .link {
            text-align: center;
            color: #00AEEF !important;
            font-style: italic;
            font-weight: bold;
            text-decoration: none;
        }

        .link a {
            color: #00AEEF !important;
            text-decoration: none;
        }

        .link a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# --- Título principal ---
st.markdown("<h1>🌸 Portafolio Multimodales 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p>Proyectos desarrollados durante el semestre</p>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.subheader("Portafolio Multimodales - Camila Vergara")
    st.write("Aquí podremos ver los diferentes códigos trabajados en el semestre.")

# --- Lista de proyectos ---
proyectos = [
    {"titulo": "Intro", "descripcion": "Primera página del portafolio.", "imagen": "image_2025-10-23_000052698.png", "url": "https://primerpaginacami.streamlit.app"},
    {"titulo": "Conversión de voz a texto - traductor", "descripcion": "Aplicación que convierte voz a texto.", "imagen": "image_2025-10-22_235920847.png", "url": "https://traductoridioma.streamlit.app"},
    {"titulo": "Análisis de texto - Inglés", "descripcion": "Análisis de texto en inglés.", "imagen": "image_2025-10-22_235720040.png", "url": "https://txingles.streamlit.app"},
    {"titulo": "Texto a Voz", "descripcion": "Conversión de texto a voz.", "imagen": "image_2025-10-23_000022811.png", "url": "https://cuentodelgato.streamlit.app/"},
    {"titulo": "Reconocimiento Óptico de Caracteres OCR", "descripcion": "Reconocimiento de caracteres en una imagen.", "imagen": "image_2025-10-22_235834591.png", "url": "https://audio-ocr.streamlit.app"},
    {"titulo": "Análisis de texto - Español", "descripcion": "Análisis semántico de texto en español.", "imagen": "image_2025-10-22_235806012.png", "url": "https://txespanol.streamlit.app"},
    {"titulo": "Objetos en imagen", "descripcion": "Reconocimiento de objetos mediante IA.", "imagen": "image_2025-10-22_235633240.png", "url": "https://yolocami.streamlit.app"},
    {"titulo": "Reconocimiento de gestos", "descripcion": "Modelo que detecta gestos en cámara.", "imagen": "image_2025-10-22_235547846.png", "url": "https://tmcami.streamlit.app"},
    {"titulo": "Chat PDF", "descripcion": "Analizador de documentos PDF.", "imagen": "image_2025-10-22_235457515.png", "url": "https://un-pdfchat.streamlit.app"},
    {"titulo": "Interpretación de imagen", "descripcion": "Aplicación de reconocimiento visual.", "imagen": "image_2025-10-22_235405838.png", "url": "https://renocimientoimagenes.streamlit.app"},
    {"titulo": "Tablero personalizado", "descripcion": "Tablero de caracteres personalizado.", "imagen": "image_2025-10-22_235245016.png", "url": "https://tablerodibujoo.streamlit.app"},
    {"titulo": "Tablero Inteligente", "descripcion": "Tablero que analiza comandos por voz.", "imagen": "image_2025-10-22_235148140.png", "url": "https://bocetostablero.streamlit.app"},
    {"titulo": "Lector de Sensor MQTT", "descripcion": "Lectura y análisis de datos vía MQTT.", "imagen": "image_2025-10-22_235030401.png", "url": "https://recepprocess.streamlit.app"},
    {"titulo": "Control por Voz", "descripcion": "Control de sistemas mediante comandos de voz.", "imagen": "ctrlvoz.png", "url": "https://controlador-voz.streamlit.app"}
]

# --- Mostrar en cuadrícula ---
num_cols = 5
cols = st.columns(num_cols)

for i, proyecto in enumerate(proyectos):
    with cols[i % num_cols]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image(Image.open(proyecto["imagen"]), use_container_width=True)
        st.markdown(f"<div class='titulo'>{proyecto['titulo']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{proyecto['descripcion']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p class='link'><a href='{proyecto['url']}' target='_blank'>Enlace</a></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if (i + 1) % num_cols == 0:
        cols = st.columns(num_cols)
