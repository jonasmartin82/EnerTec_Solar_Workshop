
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

st.title('Erklärung Reihenschaltung')

st.write('Auf dieser Seite wird die Reihenschaltung erklärt. Das Bild unten stellt Reihen- und Parallelschaltung gegenüber. Wie der Name vermuten lässt, werden elektrische Verbraucher (z.B. Widerstände, Glühbirnen, etc.) oder Quellen (z.B. Solarzellen, Spannungsquellen, etc.) in Reihe also nacheinander (auch seriell genannt) geschaltet. Dies bedeutet, dass der Strom durch alle Bauteile fließt.')

st.image('page_13_pic_1.png')

st.write('Quelle: https://kfz-schule.com/reihenschaltung-parallelschaltung/')

st.write('Die nachfolgenden Bilder zeigen jeweils wie eine Reihenschaltung für eine unterschiedliche Anzahl an Solarzellen (gekennzeichnet mit 2-fach z.B. für zwei Solarzellen) aussieht und aufgebaut wird. Das erste Bild zeigt die Beschaltung für eine Solarzelle und stellt in dem Sinne keine Reihenschaltung dar (da nur eine Solarzelle verwendet wird), sollte aber integriert werden, damit man das Muster nachvollziehen kann. Für die Verbindungen zwischen den Solarzellen wurden nur blaue Kabel gewählt, aber für die Funktion spielt es keine Rolle welche Farbe ihr verwendet.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Reihenschaltung (1-fach)')

st.image('Reihenschaltung_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Reihenschaltung (2-fach)')

st.image('Reihenschaltung_2.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Reihenschaltung (3-fach)')

st.image('Reihenschaltung_3.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Reihenschaltung (4-fach)')

st.image('Reihenschaltung_4.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

