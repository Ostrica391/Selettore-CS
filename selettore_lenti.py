import streamlit as st
from PIL import Image, ImageOps
import base64
import io

# Titolo
st.title("Selettore Lenti a Contatto - TS LAC")

# Input
val1 = st.number_input("Inserisci il primo valore", value=0)
val2 = st.number_input("Inserisci il secondo valore", value=0)
val3 = st.number_input("Inserisci il valore della terza cella (K6)", value=0)

# Calcolo
risultato = (val1 + val2) / 2 + 1080 + val3
st.markdown(f"### Risultato formula: {risultato:.2f}")

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
    "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png"
]

# Funzione per convertire immagine in base64
def pil_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return encoded

# CSS per la "cassetta"
st.markdown("""
    <style>
    .cassette {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 25px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-top: 30px;
        border: 2px solid #ccc;
    }
    .lens {
        text-align: center;
    }
    .lens img {
        width: 100px;
        height: auto;
        border-radius: 10px;
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
st.markdown("## Cassetta di Lenti di Prova")

# Inizio cassetta
st.markdown('<div class="cassette">', unsafe_allow_html=True)

for i in range(7):
    img = Image.open(paths[i])
    if i == indice:
        img_html = f"<div class='lens'><div class='arrow'>⬇️</div><img class='selected' src='data:image/png;base64,{pil_to_base64(img)}'><div>Lente {i+1}</div></div>"
    else:
        img_html = f"<div class='lens'><img src='data:image/png;base64,{pil_to_base64(img)}'><div>Lente {i+1}</div></div>"

    st.markdown(img_html, unsafe_allow_html=True)

# Fine cassetta
st.markdown('</div>', unsafe_allow_html=True)
