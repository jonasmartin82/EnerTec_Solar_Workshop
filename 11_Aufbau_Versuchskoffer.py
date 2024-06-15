
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

st.subheader('Aufbau Versuchskoffer')

st.write('Auf dieser Seite soll der Aufbau des Versuchskoffers beschrieben werden.')

st.write('---')

st.write('Im Deckel des Koffers ist die Grundplatte verstaut (siehe Bild unten). Nehmt diese aus dem Koffer und platziert sie auf dem Tisch. Richtet sie so aus, dass die Rundung nach links zeigt. So könnt ihr später einfacher die Winkelskala verwenden.')

st.image('page_11_pic_1.png')

st.write('---')

st.write('Im nächsten Bild seht ihr einmal alle Komponenten des Koffers. Das Poster an der Wand enthält eine beschriftete Version.')

st.image('page_11_pic_2.png')

st.write('---')

st.write('Auf dem nächsten Bild seht ihr das Solarmodul. Die Anschlüsse der Solarzellen sind mit "A" markiert. Markierung "G" und "H" zeigen die Winkelskala an. Anschluss "D" ist für das Stromkabel, Anschluss "E" wird an die Lampe angeschlossen.')

st.image('page_11_pic_3.png')

st.write('---')

st.write('Das nächste Bild zeigt den Aufbau des Solarmoduls. Dazu wird die Lampe mit dem Lampenarm von unten in die Grundplatte eingeführt (Loch in der MItte). Das Solarmodul wird in die dafür vorgesehenen Löcher platziert. Den fertigen Aufbau seht ihr im nächsten Bild.')

st.image('page_11_pic_4.png')

st.write('---')

st.write('Hier seht ihr den fertigen Aufbau mit den Anschlüssen für das Stromkabel und das Solarmodul. Bei eurem Aufbau sollte der Lampenarm nach links zeigen.')

st.image('page_11_pic_5.png')