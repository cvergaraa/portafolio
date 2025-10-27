import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Portafolio Multimodales")

# --- Estilos generales ---
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #D8F3FF;
            color: #003366;
        }
        [data-testid="stHeader"] {background: none;}
        h1, h2, h3, h4, h5, h6, p, a {
            color: #003366 !important;
        }
        .main-container {
            display: flex;
            justify-content: center;
        }
        .tarjeta {
            background-color: white;
            border-radius: 15px;
            padding: 12px;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .tarjeta:hover {
            transform: translateY(-6px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }
        .tarjeta img {
            border-radius: 10px;
        }
        .titulo {
            font-weight: bold;
            font-style: italic;
            margin-top: 5px;
            font-size: 16px;
        }
        .descripcion {
            font-size: 14px;
            margin-bottom: 8px;
        }
        .enlace a {
            color: #00AEEF !important;
            font-style: italic;
            text-decoration: none;
            font-weight: bold;
        }
        .enlace a:hover { text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

# --- Título ---
st.markdown("""
    <h1 style='text-align:center;'>🌸 Portafolio Multimodales 🌸</h1>
    <p style='text-align:center; font-size:18px;'>Proyectos desarrollados durante el semestre</p>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.subheader("Portafolio Multimodales - Camila Vergara")
    st.write("Aquí podrás explorar los diferentes códigos trabajados durante el semestre.")

# --- Lista de los 14 proyectos ---
proyectos = [
    {"titulo": "Intro", "descripcion": "Primera página del portafolio.", "imagen": "image_2025-10-23_000052698.png", "url": "https://primerpaginacami.streamlit.app"},
    {"titulo": "Conversión voz a texto", "descripcion": "Convierte voz a texto en tiempo real.", "imagen": "image_2025-10-22_235920847.png", "url": "https://traductoridioma.streamlit.app"},
    {"titulo": "Texto a voz", "descripcion": "Convierte texto en audio natural.", "imagen": "image_2025-10-23_000022811.png", "url": "https://cuentodelgato.streamlit.app"},
    {"titulo": "Análisis texto inglés", "descripcion": "Analiza texto en inglés.", "imagen": "image_2025-10-22_235720040.png", "url": "https://txingles.streamlit.app"},
    {"titulo": "Reconocimiento OCR", "descripcion": "Detecta texto en imágenes con OCR.", "imagen": "image_2025-10-22_235834591.png", "url": "https://audio-ocr.streamlit.app"},
    {"titulo": "Objetos en imagen", "descripcion": "Reconoce objetos con inteligencia artificial.", "imagen": "image_2025-10-22_235633240.png", "url": "https://yolocami.streamlit.app"},
    {"titulo": "Reconocimiento de gestos", "descripcion": "Detecta gestos con cámara.", "imagen": "image_2025-10-22_235547846.png", "url": "https://tmcami.streamlit.app"},
    {"titulo": "Análisis texto español", "descripcion": "Analiza textos en español.", "imagen": "image_2025-10-22_235806012.png", "url": "https://txespanol.streamlit.app"},
    {"titulo": "Tablero inteligente", "descripcion": "Tablero de control activado por voz.", "imagen": "image_2025-10-22_235148140.png", "url": "https://bocetostablero.streamlit.app"},
    {"titulo": "Control por voz", "descripcion": "Control de voz con MQTT.", "imagen": "ctrlvoz.png", "url": "https://controlador-voz.streamlit.app"},
    {"titulo": "Análisis de imagen", "descripcion": "Procesamiento visual de imágenes.", "imagen": "81dad8c3-efd9-4981-853c-0cf216c0351c.png", "url": "https://analisis-imagen.streamlit.app"},
    {"titulo": "Traducción Multilenguaje", "descripcion": "Traduce entre varios idiomas.", "imagen": "7e01d942-1f89-4fa5-a7b8-d5e35944d5b1.png", "url": "https://multitraductor.streamlit.app"},
    {"titulo": "Audio Análisis", "descripcion": "Analiza y clasifica sonidos.", "imagen": "8cec6e73-f8bf-4ebe-b81a-242c979d8755.png", "url": "https://analisis-audio.streamlit.app"},
    {"titulo": "Visión Artificial", "descripcion": "Detección avanzada con visión computacional.", "imagen": "image_2025-10-23_000130444.png", "url": "https://visionia.streamlit.app"}
]

# --- Mostrar los proyectos en cuadrícula ---
num_cols = 5
cols = st.columns(num_cols)

for i, proyecto in enumerate(proyectos):
    col = cols[i % num_cols]
    with col:
        try:
            img = Image.open(proyecto["imagen"])
            st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
            st.markdown(f"<p class='titulo'>{proyecto['titulo']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='descripcion'>{proyecto['descripcion']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='enlace'><a href='{proyecto['url']}' target='_blank'>Enlace</a></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning(f"⚠️ No se encontró la imagen: {proyecto['imagen']}")

