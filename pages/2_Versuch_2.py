
import streamlit as st
import matplotlib.pyplot as plt

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

st.title("Versuch 2")

st.write('In diesem Versuch messt ihr den Kurzschlussstrom einer Solarzelle bei verschiedenen Stufen der Abschattung. Kurzschlussstrom bedeutet in diesem Fall, dass ihr außer eurem Multimeter keine weiteren elektrischen Verbraucher wie z.B. eine Glühbirne oder einen Elektromotor in den Stromkreis integriert.')

st.write('Hinweis: wenn in eurem Versuchskoffer ein schwarzes Multimeter vorhanden ist stellt es bitte auf "DC A 2000m" ein. Falls ein rotes Multimeter vorhanden ist, steckt den schwarzen Adapter in die Buchse "CON" und den roten Adapter in die Buchse mit "10A". Stellt das Multimeter auf "A -" ein. In diesem Fall müsst ihr den Wert des Multimeters in mA umrechnen, indem ihr den Wert mit 1000 multipliziert bzw. das Komma drei Stellen nach rechts verschiebt.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_2_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Beginnt damit eine Tabelle auf einem Blatt anzulegen die wie folgt aussieht:')

st.image('page_2_pic_2.png')

st.write('Diese Tabelle dient euch als Hilfe beim ausfüllen bzw. während des Experiments. Beginnt mit einer bestrahlten Fläche von "0" (entspricht dem größten Blech) und fahrt so für die Werte "1/2" (mittleres Blech), "3/4" (kleines Blech) und "1" (kein Blech) fort und notiert jeweils den Kurzschlussstrom in mA.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Wenn ihr alle Werte nun bestimmt habt tragt diese entsprechend in die Kästchen unten ein. Mit einem Klick auf "Zeichnen" wird für euch ein Diagramm erstellt."')

st.write('')

col1, col2, col3, col4 = st.columns(4)

with col1:
    val_1 = st.number_input(label='Kurzschlussstrom "0" in mA', min_value=0, max_value=2000)
    
with col2:
    val_2 = st.number_input(label='Kurzschlussstrom "1/2" in mA', min_value=0, max_value=2000)
    
with col3:
    val_3 = st.number_input(label='Kurzschlussstrom "3/4" in mA', min_value=0, max_value=2000)
    
with col4:
    val_4 = st.number_input(label='Kurzschlussstrom "1" in mA', min_value=0, max_value=2000)

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    button_zeichnen = st.button(label='Zeichnen', type='primary') 
    
with colC:
    st.write('')
 
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

x_val = [0, 50, 75, 100]
y_val = [val_1, val_2, val_3, val_4]

fig = plt.figure(1)
plt.plot(x_val, y_val)
plt.title('Kurzschlussstrom über relativer Fläche')
plt.xlabel('relative Fläche der Solarzelle in %')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

if button_zeichnen == 1:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig)
    with col3:
        st.write('')

    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if button_zeichnen == 1:
    
    st.subheader('Erklärung:')
    
    st.write('Wenn ihr die Zeichnung erstellt habt, seht ihr nun, wie sich der Kurzschlussstrom verhält, wenn ihr eine bestimmte Fläche der Solarzelle bestrahlt. Dabei entspricht ein Wert von "100%" einer vollen Bestrahlung, ein Wert von "50%" der halben Fläche (mittleres Blech), etc.')
    
    st.write('tbd')

# ------------------------------------------------------------------------------------------------------------------------ #

