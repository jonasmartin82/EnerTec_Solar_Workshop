
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

st.title('Einstellung Multimeter')

st.write('Da die Einstellung der Multimeter immer wieder zu Problemen führt sind hier sämtliche Einstellmöglichkeiten für beide Typen aufgelistet. Dabei wird unterschieden in Multimeter "Rot" und Multimeter "Schwarz".')

st.write('Zu beachten bei der Einstellung sind vier Dinge: die korrekte Auswahl des Multimeters (Schwarz oder Rot), die richtige Auswahl der Buchsen am Gerät, die Polung der Anschlüsse (also blau zu schwarz oder "COM" und rot zu rot bzw. der entsprechenden Buchse) und die korrekte Einstellung des Drehreglers.')

st.write('Wenn ihr die vier Schritte oben beachtet solltet ihr euer Multimeter nicht falsch einstellen können. Eine korrekte EInstellung ist wichtig: sonst könnte es sein, dass ihr eine falsche Größe misst (z.B. Spannung statt Stromstärke) oder ihr vom Messgerät aufgrund falscher Einstellung nicht korrekte Messwerte erhält (z.B. beim roten Multimeter zeigt euch das Gerät Werte bei mA an, die falsch sind, da die Stromstärke zu hoch ist).')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Schwarz 2000mV')

st.image('schwarz_2000mV.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Schwarz 20V')

st.image('schwarz_20V.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Schwarz 2000mA')

st.image('schwarz_2000mA.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Schwarz 10A')

st.image('schwarz_10A.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Rot mV')

st.image('rot_mV.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Rot V')

st.image('rot_V.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Rot mA')

st.image('rot_mA.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Rot A')

st.image('rot_A.png', width=500)

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

