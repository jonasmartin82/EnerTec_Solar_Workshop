
import streamlit as st

st.set_page_config(page_title = "EnerTec Solar Workshop", layout = "wide")

st.logo('Logo_EnerTec_ohne_Hintergrund.png')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('Logo_Stiftung_ohne_Hintergrund.png', width=250)
    
with col2:
    st.image('Logo_EnerTec_ohne_Hintergrund.png', width=250)
    
with col3:
    st.image('Logo_AES_ohne_Hintergrund.png', width=250)
    
# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Erklärung Solarenergie')

st.write('Auf dieser Seite soll die Solarenergie erklärt werden. Dabei beschäftigen wir uns mit der Quelle der Energie, ihrer Verbreitung und deren Nutzung.')

st.write('tbd')

st.write('---')