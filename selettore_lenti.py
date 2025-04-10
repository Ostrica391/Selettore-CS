import streamlit as st
from PIL import Image, ImageOps

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

# Mostra le immagini
st.markdown("---")
st.subheader("Set di Lenti")
cols = st.columns(7)

for i in range(7):
    col = cols[i % 7]  # Riempie le colonne a gruppi di 7
    img = Image.open(paths[i])
    if i == indice:
        # Applica bordo rosso per evidenziare
        img_highlight = ImageOps.expand(img, border=10, fill='red')
        col.markdown("<div style='text-align: center; font-size: 32px;'>🔻</div>", unsafe_allow_html=True)
        col.image(img_highlight, caption=f"Lente {i+1} (SELEZIONATA)", use_container_width=True)
    else:
        col.image(img, caption=f"Lente {i+1}", use_container_width=True)
