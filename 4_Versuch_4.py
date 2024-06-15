
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

st.title("Versuch 4")

st.write('In diesem Versuch messt ihr den Kurzschlussstrom und die Leerlaufspannung einer Solarzelle mit mehreren Solarzellen parallel geschaltet. Kurzschlussstrom und Leerlaufspannung bedeutet in diesem Fall, dass ihr außer eurem Multimeter keine weiteren elektrischen Verbraucher wie z.B. eine Glühbirne oder einen Elektromotor in den Stromkreis integriert.')

st.write('Hinweis: wenn in eurem Versuchskoffer ein schwarzes Multimeter vorhanden ist stellt es bitte auf "DC A 2000m" bzw. "DC V 2000m" ein. Falls ein rotes Multimeter vorhanden ist, steckt den schwarzen Adapter in die Buchse "CON" und den roten Adapter in die Buchse mit "10A". Stellt das Multimeter auf "A -" ein. In diesem Fall müsst ihr den Wert des Multimeters in mA umrechnen, indem ihr den Wert mit 1000 multipliziert bzw. das Komma drei Stellen nach rechts verschiebt. Um die Spannung zu messen steckt den roten Adapter in den Anschluss "" und stellt das Multimeter auf "V -" ein.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_3_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Beginnt damit eine Tabelle auf einem Blatt anzulegen die wie folgt aussieht:')

st.image('page_3_pic_2.png')

st.write('Diese Tabelle dient euch als Hilfe beim ausfüllen bzw. während des Experiments. Beginnt zunächst nur mit einer Solarzelle und bestimmt Strom und Spannung. Anschließend schaltet zwei Solarzellen parallel und fährt so fort. Für einen Hinweis was eine Parallelschaltung ist schaut bitte in die Seite "Erklärung Parallelschaltung" hinein.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Wenn ihr alle Werte nun bestimmt habt tragt diese entsprechend in die Kästchen unten ein. Mit einem Klick auf "Zeichnen" wird für euch ein Diagramm erstellt."')

st.write('')

col1, col2, col3, col4 = st.columns(4)

with col1:
    U_1 = st.number_input(label='Leerlaufspannung in mA (Solarzelle 1)', min_value=0, max_value=2000)
    
    I_1 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1)', min_value=0, max_value=2000)
    
with col2:
    U_2 = st.number_input(label='Leerlaufspannung in mA (Solarzelle 1+2)', min_value=0, max_value=2000)
    
    I_2 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2)', min_value=0, max_value=2000)
    
with col3:
    U_3 = st.number_input(label='Leerlaufspannung in mA (Solarzelle 1+2+3)', min_value=0, max_value=2000)
    
    I_3 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2+3)', min_value=0, max_value=2000)
    
with col4:
    U_4 = st.number_input(label='Leerlaufspannung in mA (Solarzelle 1+2+3+4)', min_value=0, max_value=2000)
    
    I_4 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2+3+4)', min_value=0, max_value=2000)

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    button_zeichnen = st.button(label='Zeichnen', type='primary') 
    
with colC:
    st.write('')
 
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

x = [1, 2, 3, 4]
U_val = [U_1, U_2, U_3, U_4]
I_val = [I_1, I_2, I_3, I_4]

fig1 = plt.figure(1)
plt.plot(x, U_val)
plt.title('Leerlaufspannung für unterschiedliche Anzahl an Solarzellen')
plt.xlabel('Anzahl Solarzellen in Parallelschaltung')
plt.ylabel('Leerlaufspannung in mV')
plt.grid()

fig2 = plt.figure(2)
plt.plot(x, I_val)
plt.title('Kurzschlussstrom für unterschiedliche Anzahl an Solarzellen')
plt.xlabel('Anzahl Solarzellen in Parallelschaltung')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

if button_zeichnen == 1:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig1)
    with col3:
        st.pyplot(fig2)
    with col4:
        st.write('')
    
    st.write('---')
    
    st.subheader('Frage:')    
    
    st.write('Wie verhalten sich die Leerlaufspannung und der Kurzschlussstrom bei einer Parallelschaltung? Wofür könnte dieses Verhalten nützlich sein?')

    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if button_zeichnen == 1:
    
    st.subheader('Erklärung:')
    
    st.write('Wenn man mehrere Solarzellen parallel schaltet erhöht sich der Strom, während die Spannung ungefähr gleich bleibt. Die Parallelschaltung verhält sich so, weil jede Solarzelle einen bestimmten Strom I produziert und sich dieser addiert. Dazu hilft es sich das Wasser-Modell des Stroms vor Augen zu führen (siehe "Erklärung Wasser Modell"): die Stromstärke entspricht der Menge an Wasser die fließt, sodass sich die Stromstärke entsprechend addiert.')
    
    st.write('tbd')

# ------------------------------------------------------------------------------------------------------------------------ #
