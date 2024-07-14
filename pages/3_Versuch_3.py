
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

st.title("Versuch 3")

st.write('In diesem Versuch messt ihr den Kurzschlussstrom und die Leerlaufspannung einer Solarzelle mit mehreren Solarzellen in Reihe geschaltet. Kurzschlussstrom und Leerlaufspannung bedeutet in diesem Fall, dass ihr außer eurem Multimeter keine weiteren elektrischen Verbraucher wie z.B. eine Glühbirne oder einen Elektromotor in den Stromkreis integriert.')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mV" oder "Rot mV".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_3_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Beginnt damit eine Tabelle auf einem Blatt anzulegen die wie folgt aussieht:')

st.image('page_3_pic_2.png')

st.write('Diese Tabelle dient euch als Hilfe beim ausfüllen bzw. während des Experiments. Beginnt zunächst nur mit einer Solarzelle und bestimmt Strom und Spannung. Anschließend schaltet zwei Solarzellen in Reihe und fährt so fort. Für einen Hinweis was eine Reihenschaltung ist schaut bitte in die Seite "Erklärung Reihenschaltung" hinein.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Wenn ihr alle Werte nun bestimmt habt tragt diese entsprechend in die Kästchen unten ein. Mit einem Klick auf "Zeichnen" wird für euch ein Diagramm erstellt.')

st.write('')

col1, col2, col3, col4 = st.columns(4)

with col1:
    U_1 = st.number_input(label='Leerlaufspannung in mV (Solarzelle 1)', min_value=0, max_value=2000)
    I_1 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1)', min_value=0, max_value=2000)
    
with col2:
    U_2 = st.number_input(label='Leerlaufspannung in mV (Solarzelle 1+2)', min_value=0, max_value=2000)
    I_2 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2)', min_value=0, max_value=2000)
    
with col3:
    U_3 = st.number_input(label='Leerlaufspannung in mV (Solarzelle 1+2+3)', min_value=0, max_value=2000)
    I_3 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2+3)', min_value=0, max_value=2000)
    
with col4:
    U_4 = st.number_input(label='Leerlaufspannung in mV (Solarzelle 1+2+3+4)', min_value=0, max_value=2000)
    I_4 = st.number_input(label='Kurzschlussstrom in mA (Solarzelle 1+2+3+4)', min_value=0, max_value=2000)

# xxx #

if "Zeichnen (Versuch 3)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 3)"] = False

if "Erklärung (Versuch 3)" not in st.session_state:
    st.session_state["Erklärung (Versuch 3)"] = False
 
# xxx # 

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen (Versuch 3)', type='primary'):
        st.session_state['Zeichnen (Versuch 3)'] = not st.session_state['Zeichnen (Versuch 3)']
    
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
plt.xlabel('Anzahl Solarzellen in Reihenschaltung')
plt.ylabel('Leerlaufspannung in mV')
plt.grid()

fig2 = plt.figure(2)
plt.plot(x, I_val)
plt.title('Kurzschlussstrom für unterschiedliche Anzahl an Solarzellen')
plt.xlabel('Anzahl Solarzellen in Reihenschaltung')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

if st.session_state['Zeichnen (Versuch 3)']:
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
 
    st.write('Wie verhalten sich die Leerlaufspannung und der Kurzschlussstrom bei einer Reihenschaltung? Wofür könnte dieses Verhalten nützlich sein?')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 3)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 3)'):
            st.session_state['Erklärung (Versuch 3)'] = not st.session_state['Erklärung (Versuch 3)']
    with col3:
        st.write('')
    
    st.write('---')
    
# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 3)']:
    
    st.subheader('Erklärung:')
    
    st.write('Wenn man mehrere Solarzellen in Reihe schaltet erhöht sich die Spannung, während der Strom ungefähr gleich bleibt. Die Reihenschaltung verhält sich so, weil jede Solarzelle wie eine Spannungsquelle wirkt. Den selben Effekt nutzt man zum Beispiel bei Batterien in einer Fernbedienung aus: wenn mehrere Batterien in Reihe geschaltet sind, erhöht sich insgesamt die Spannung, sodass das Gerät betrieben werden kann.')
    
    st.write('Ihr fragt euch sicherlich warum man eine Reihenschaltung von Solarzellen in der Realität benötigt. Dies hat mehrere Gründe, aber der wichtigste ist das eine höhere Spannung einfacher und mit weniger Verlusten in eine andere Spannung umgewandelt werden kann. Da eine Solarzelle eine Gleichspannung (DC) produziert und unser Stromnetz mit Wechselspannung (AC) funktioniert, muss ein Wechselrichter die Spannung entsprechend anpassen. Dazu benötigt er unter anderem einen gewissen Mindestwert an Spannung. So kann es sein, dass an einem bewölkten Tag oder bei weniger Sonneneinstrahlung in Frühling und Herbst die Spannung einer Solarzelle nicht ausreicht und dieser Wert nur durch die Reihenschaltung erreicht werden kann.')

    st.image('page_3_pic_3.png')
    
    st.write('Quelle: https://publikationen.dguv.de/widgets/pdf/download/article/2896')
    
    st.write('Ein Nachteil der Reihenschaltung ist unter anderem wie in Versuch 1 beschrieben die Anfälligkeit für Verschattung oder Defekt einzelner Solarzellen: bereits eine defekte oder zu stark verschattete Zelle kann die Spannung einer Reihenschaltung dramatisch absenken. Probiert es gerne selbst aus indem ihr bei eurer Reihenschaltung hier eine Solarzelle komplett verdunkelt. Der Wert der Spannung sollte deutlich kleiner sein als im Normalzustand. Aber dazu gibt es technische Maßnahmen wie unter Versuch 1 beschrieben um dieses Problem in der Realität zu umgehen.')
    
    st.write('Die Abbildung oben zeigt eine Skizze eienr Solaranlage mit drei sogenannten "Strings" (Reihenschaltung von Solarzellen) wobei die drei Strings dann parallel geschaltet wurden. Man kann sich vorstellen was bei dem Ausfall eines Moduls eines Strings passiert: der gesamte String ist damit wirkungslos oder stark in seiner Funktion eingeschränkt. Aus diesem Grund schaltet man auch nicht mehr Solarzellen in Reihe wie nötig sondern geht wie hier dazu über, mehrere Strings bzw. Reihenschaltungen parallel zu schalten. Warum dies sinnvoll ist erfährt ihr in Versuch 4 bei der Parallelschaltung von Solarzellen.')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #
