
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

st.title('Aufbau Versuchskoffer')

st.write('Auf dieser Seite soll der Aufbau des Versuchskoffers beschrieben werden.')

st.write('---')

st.write('Auf dem ersten Bild seht ihr den geöffneten Koffer mit Schaumstoff im Deckel')

st.image('page_11_pic_1.png')

st.write('---')

st.write('Im Deckel des Koffers ist die Grundplatte verstaut (siehe Bild unten). Nehmt diese aus dem Koffer und platziert sie auf dem Tisch. Richtet sie so aus, dass die Rundung nach links zeigt. So könnt ihr später einfacher die Winkelskala verwenden.')

st.image('page_11_pic_2.png')

st.write('---')

st.write('Im nächsten Bild seht ihr einmal alle Komponenten des Koffers. Das Poster an der Wand enthält eine beschriftete Version.')

st.image('page_11_pic_7.png')

st.write('---')

st.write('Auf dem nächsten Bild seht ihr die Grundplatte mit markierten Bohrungen. Die rot markierte Bohrung nimmt dabei wie man sieht den Lampenarm auf. Die blau markierten Bohrungen sind im nächsten Schritt zur Montage des Solarmoduls gedacht.')

st.image('page_11_pic_3.png')

st.write('---')

st.write('Im folgenden Bild seht ihr das fertig montierte Solarmodul. Achtet darauf, dass die Winkelskala zu euch zeigt. Die Rundung der Grundplatte sollte dafür nach links zeigen.')

st.image('page_11_pic_4.png')

st.write('---')

st.write('Hier seht ihr den fertigen Aufbau mit und ohne den Anschlüssen für das Stromkabel und das Solarmodul.')

col1, col2 = st.columns(2)

with col1:
    st.image('page_11_pic_5.png')
    
with col2:
    st.image('page_11_pic_6.png')
    
    