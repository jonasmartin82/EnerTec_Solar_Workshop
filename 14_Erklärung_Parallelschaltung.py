
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

st.subheader('Erklärung Parallelschaltung')

st.write('Auf dieser Seite wird die Parallelschaltung erklärt. Das Bild unten stellt Reihen- und Parallelschaltung gegenüber. Wie der Name vermuten lässt, werden elektrische Verbraucher (z.B. Widerstände, Glühbirnen, etc.) oder Quellen (z.B. Solarzellen, Spannungsquellen, etc.) parallel also nebeneinander geschaltet. Dies bedeutet, dass sich der Strom aufteilt und durch jedes Bauteil fließt.')

st.image('page_14_pic_1.png')

st.write('Quelle: https://kfz-schule.com/reihenschaltung-parallelschaltung/')

st.write('Die nachfolgenden Bilder zeigen jeweils wie eine Parallelschaltung für eine unterschiedliche Anzahl an Solarzellen (gekennzeichnet mit 2-fach z.B. für zwei Solarzellen) aussieht und aufgebaut wird. Das erste Bild zeigt die Beschaltung für eine Solarzelle und stellt in dem Sinne keine Parallelschaltung dar (da nur eine Solarzelle verwendet wird), sollte aber integriert werden, damit man das Muster nachvollziehen kann. Für die Verbindungen zwischen den Solarzellen könnt ihr blaue und rote Kabel verwenden. Zu Übersichtlichkeit wurden hier die Farben sortiert. Die Kabel in dem Versuchskoffer haben an jedem Stecker eine Buchse, in die ihr weitere Kabel einstecken könnt um so die Solarzellen miteinander zu verbinden.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Parallelschaltung (1-fach)')

st.image('Parallelschaltung_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Parallelschaltung (2-fach)')

st.image('Parallelschaltung_2.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Parallelschaltung (3-fach)')

st.image('Parallelschaltung_3.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Parallelschaltung (4-fach)')

st.image('Parallelschaltung_4.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #