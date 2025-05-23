import streamlit as st
from PIL import Image, ImageOps
import base64
import io

# Sfondo gradiente più marcato: bianco -> blu profondo + larghezza massima container
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffffff, #ffffff);
        background-attachment: fixed;
    }
    .block-container {
        max-width: 90% !important;
        padding: 2rem 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Menu link in alto a sinistra
st.markdown("""
    <style>
    .top-menu {
        position: absolute;
        top: 60px;
        left: 0px;
        z-index: 1;
    }
    .top-menu a {
        display: block;
        background-color: #004890;
        color: white;
        padding: 8px 16px;
        margin-bottom: 8px;
        text-decoration: none;
        border-radius: 6px;
        font-size: 14px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: background 0.3s;
    }
    .top-menu a:hover {
        background-color: #0060b0;
    }
    </style>
    <div class="top-menu">
        <a href="https://selettore-cs.streamlit.app/" target="_blank">Calcolatore CS</a>
        <a href="https://selettore-scl-adv.streamlit.app/" target="_blank">Calcolatore SCL-ADV</a>
        <a href="https://selettoretslac.streamlit.app/">Calcolatore Sag Soft</a>
        <a href="https://www.tslac.it/">Work in progress</a>
    </div>
""", unsafe_allow_html=True)

# Logo centrato
st.markdown("""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,""" + base64.b64encode(open("TSLAC.png", "rb").read()).decode() + """' style='width: 400px; margin-bottom: 10px;'>
    </div>
""", unsafe_allow_html=True)

# Titolo
st.title("Selettore CS - TS LAC")

# Input
val1 = st.number_input("Inserisci SAG 5.00mm 0°", value=1700, step=10)
val2 = st.number_input("Inserisci SAG 5.00mm 180°", value=1700, step=10)
val3 = st.number_input("Central Clearance", value=250, step=5)

# Calcolo
risultato = (val1 + val2) / 2 + 1080 + val3
st.markdown(f"### SAG Lente: {int(risultato)} µm")

# Determina quale immagine evidenziare
indice = None
if 2080 <= risultato <= 3050:
    indice = 0
elif 3051 <= risultato <= 3200:
    indice = 1
elif 3201 <= risultato <= 3300:
    indice = 2
elif 3301 <= risultato <= 3400:
    indice = 3
elif 3401 <= risultato <= 3500:
    indice = 4
elif 3501 <= risultato <= 3650:
    indice = 5
elif 3651 <= risultato <= 3900:
    indice = 6

# Percorsi immagini
paths = [
    "cs1.png", "cs2.png", "cs3.png", "cs4.png", "cs5.png", "cs6.png", "cs7.png"
]

# Etichette personalizzate sotto ogni lente
sag_labels = ["SAG 3000µm", "SAG 3150µm", "SAG 3250µm", "SAG 3350µm", "SAG 3450µm", "SAG 3600µm", "SAG 3850µm"]

# Funzione per convertire immagine in base64
def pil_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return encoded

# CSS + HTML layout
st.markdown("""
    <style>
    .cassette {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 30px;
        display: flex;
        justify-content: center;
        gap: 25px;
        flex-wrap: nowrap;
        align-items: flex-end;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin: 30px auto;
        border: 2px solid #ccc;
        width: 100%;
        max-width: 100%;
        overflow-x: auto;
    }
    .lens {
        text-align: center;
        margin: 0 5px;
    }
    .selected {
        border: 5px solid red;
        padding: 5px;
        border-radius: 12px;
    }
    .arrow {
        font-size: 30px;
        margin-bottom: 5px;
        color: red;
    }
    </style>
""", unsafe_allow_html=True)

# Titolo cassetta
st.markdown("## Lenti di prova CS")

# Costruiamo tutto l'HTML in un unico blocco
cassette_html = "<div class='cassette'>"

for i in range(7):
    img = Image.open(paths[i])
    img_html = f"<img src='data:image/png;base64,{pil_to_base64(img)}' style='width: 190px; border-radius: 10px;' class='{'selected' if i == indice else ''}'>"
    arrow_html = "<div class='arrow'>⬇️</div>" if i == indice else ""
    label = f"{sag_labels[i]}{' (Lente ideale)' if i == indice else ''}"
    lens_html = f"<div class='lens'>{arrow_html}{img_html}<div>{label}</div></div>"
    cassette_html += lens_html

cassette_html += "</div>"

# Mostriamo tutto
st.markdown(cassette_html, unsafe_allow_html=True)

# Carica due immagini diverse
with open("totalsag.png", "rb") as img_file_a:
    encoded_a = base64.b64encode(img_file_a.read()).decode()

with open("totalsagb.png", "rb") as img_file_b:
    encoded_b = base64.b64encode(img_file_b.read()).decode()

# Mostra affiancate le due immagini
st.markdown(f"""
    <div style='margin-top: 30px; display: flex; justify-content: center; gap: 40px;'>
        <img src='data:image/png;base64,{encoded_a}' style='width: 500px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
        <img src='data:image/png;base64,{encoded_b}' style='width: 500px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
    </div>
""", unsafe_allow_html=True)

# Carica immagine finale
with open("totalsagc.png", "rb") as img_file_c:
    encoded_c = base64.b64encode(img_file_c.read()).decode()

# Mostra immagine finale centrata
st.markdown(f"""
    <div style='margin-top: 40px; text-align: center;'>
        <img src='data:image/png;base64,{encoded_c}' style='width: 700px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='position: relative; bottom: 0; width: 100%; text-align: center; font-size: 10px; color: gray; margin-top: 50px;'>
        TSLAC stc-030 rev. 01-25
    </div>
""", unsafe_allow_html=True)


