
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

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mV" oder "Rot mV".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot A". Im Fall eines roten Multimeters müsst ihr den Wert noch mit 1000 multiplizieren bzw. das Komma drei Stellen nach rechts verschieben, damit die Einheit von "A" in "mA" umgerechnet wird.')

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

if "Zeichnen" not in st.session_state:
    st.session_state["Zeichnen"] = False

if "Erklärung" not in st.session_state:
    st.session_state["Erklärung"] = False
 
# xxx # 

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen', type='primary'):
        st.session_state['Zeichnen'] = not st.session_state['Zeichnen'] 
    
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

if st.session_state['Zeichnen']:
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

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung'):
            st.session_state['Erklärung'] = not st.session_state['Erklärung']
    with col3:
        st.write('')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung']:
    
    st.subheader('Erklärung:')
    
    st.write('Wenn man mehrere Solarzellen parallel schaltet erhöht sich der Strom, während die Spannung ungefähr gleich bleibt. Die Parallelschaltung verhält sich so, weil jede Solarzelle einen bestimmten Strom I produziert und sich dieser addiert. Dazu hilft es sich das Wasser-Modell des Stroms vor Augen zu führen (siehe "Erklärung Wasser Modell"): die Stromstärke entspricht der Menge an Wasser die fließt, sodass sich die Stromstärke entsprechend addiert.')
    
    st.write('Eine Parallelschaltung von Solarzellen kann sinnvoll sein, um die Leistung oder die Energie, die eine Anlage liefern kann zu erhöhen, wenn man die Spannung nicht verändern möchte. Wie sich eine Reihenschaltung verhält könnt ihr in Versuch 3 sehen, wobei die wichtigste Erkenntnis aus Versuch 3 ist, dass man mittels einer Reihenschaltung eine gewünschte Spannung einstellen kann. Deswegen wird eine Parallelschaltung verwendet um die Leistung einer Anlage zu erhöhen.')
    
    st.image('page_4_pic_3.png')
    
    st.write('Quelle: https://publikationen.dguv.de/widgets/pdf/download/article/2896')
    
    st.write('Die Abbildung oben zeigt eine Solaranlage, die wie in Versuch 3 beschrieben aus drei sogenannten "Strings" besteht, die lediglich eine Reihenschaltung von Solarzellen darstellt. Diese Strings werden im Anschluss parallel geschaltet um den Strom zu erhöhen. So kann über eine Parallelschaltung von mehreren Strings die Leistung einer Anlage deutlich erhöhen. Reale Solaranlagen funktionieren genau nach diesem Prinzip: eine bestimmte Anzahl an Solarzellen wird in Reihe geschaltet zu Strings und danach werden beliebig viele Strings parallel geschaltet bis die angestrebte Leistung der Solaranlage erreicht wurde.')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #
