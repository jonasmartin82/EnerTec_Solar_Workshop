
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

st.title("Versuch 1")

st.write('In diesem Versuch messt ihr die Leerlaufspannung und den Kurzschlussstrom einer Solarzelle bei verschiedenen Stufen der Abschattung. Leerlaufspannung und Kurzschlusstrom bedeutet in diesem Fall, dass ihr außer eurem Multimeter keine weiteren elektrischen Verbraucher wie z.B. eine Glühbirne oder einen Elektromotor in den Stromkreis integriert.')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mV" oder "Rot mV".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

col1, col2 = st.columns(2)

with col1:
    st.write('Aufbau Spannungsmessung')
    st.image('page_1_pic_1.png')
    
with col2:
    st.write('Aufbau Strommessung')
    st.image('page_1_pic_2.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Baut das Experiment entsprechend der Abbildungen oben nach (der Unterschied in beiden Abbildungen ist nur die Einstellung des Multimeters). Beginnt damit zwei Tabellen auf einem Blatt anzulegen die wie folgt aussehen:')

col1, col2 = st.columns(2)

with col1:
    st.write('Tabelle Spannungsmessung')
    st.image('page_1_pic_3.png')

with col2:
    st.write('Tabelle Strommessung')
    st.image('page_1_pic_4.png')
    
st.write('Diese Tabellen dienen euch als Hilfe beim ausfüllen bzw. während des Experiments. Beginnt mit einer bestrahlten Fläche von "0" (entspricht dem größten Blech) und fahrt so für die Werte "1/2" (mittleres Blech), "3/4" (kleines Blech) und "1" (kein Blech) fort und notiert jeweils die Leerlaufspannung in mV und den Kurzschlusstrom in mA. Dabei könnt ihr zuerst alle Werte für die Leerlaufspannung bestimmen und danach die Werte für den Kurzschlussstrom oder während dem Experiment beide Größen nacheinander für eine Abschattung bestimmen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Wenn ihr alle Werte nun bestimmt habt tragt diese entsprechend in die Kästchen unten ein. Mit einem Klick auf "Zeichnen" werden für euch zwei Diagramme erstellt."')

st.write('')

col1, col2 = st.columns(2)

with col1:
    U_1 = st.number_input(label='Leerlaufspannung "0" in mV', min_value=0, max_value=2000)
    U_2 = st.number_input(label='Leerlaufspannung "1/2" in mV', min_value=0, max_value=2000)
    U_3 = st.number_input(label='Leerlaufspannung "3/4" in mV', min_value=0, max_value=2000)
    U_4 = st.number_input(label='Leerlaufspannung "1" in mV', min_value=0, max_value=2000)
    
with col2:
    I_1 = st.number_input(label='Kurzschlussstrom "0" in mA', min_value=0, max_value=2000)
    I_2 = st.number_input(label='Kurzschlussstrom "1/2" in mA', min_value=0, max_value=2000)
    I_3 = st.number_input(label='Kurzschlussstrom "3/4" in mA', min_value=0, max_value=2000)
    I_4 = st.number_input(label='Kurzschlussstrom "1" in mA', min_value=0, max_value=2000)
    
# xxx #

if "Zeichnen (Versuch 1)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 1)"] = False

if "Erklärung (Versuch 1)" not in st.session_state:
    st.session_state["Erklärung (Versuch 1)"] = False
 
# xxx #    
    
colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen (Versuch 1)', type='primary'):
        st.session_state['Zeichnen (Versuch 1)'] = not st.session_state['Zeichnen (Versuch 1)']
    
with colC:
    st.write('')
 
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

x_val = [0, 50, 75, 100]
U_val = [U_1, U_2, U_3, U_4]
I_val = [I_1, I_2, I_3, I_4]

fig1 = plt.figure(1)
plt.plot(x_val, U_val)
plt.title('Leerlaufspannung über relativer Fläche')
plt.xlabel('relative Fläche der Solarzelle in %')
plt.ylabel('Leerlaufspannung in mV')
plt.grid()

fig2 = plt.figure(2)
plt.plot(x_val, I_val)
plt.title('Kurzschlussstrom über relativer Fläche')
plt.xlabel('relative Fläche der Solarzelle in %')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

if st.session_state['Zeichnen (Versuch 1)']:
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
    
    st.write('Wie verhalten sich die Leerlaufspannung und der Kurzschlussstrom bei verschiedenen Graden der Abschattung? Warum könnte dieses Verhalten ein Problem sein?')
    
    st.write('Überlege wie Anlagen auf Hausdächern und im freien Feld davon beeinflusst werden könnten. Wie kann man diese Probleme vermeiden?')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 1)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 1)'):
            st.session_state['Erklärung (Versuch 1)'] = not st.session_state['Erklärung (Versuch 1)']
    with col3:
        st.write('')
    
    st.write('---')
        
# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 1)']:
    
    st.subheader('Erklärung:')
    
    st.write('Wenn ihr die Zeichnungen erstellt habt, seht ihr nun, wie sich die Leerlaufspannung und der Kurzschlussstrom verhält, wenn ihr eine bestimmte Fläche der Solarzelle bestrahlt. Dabei entspricht ein Wert von "100%" bzw, "1/1" einer vollen Bestrahlung, ein Wert von "50%" bzw. "1/2" der halben Fläche (mittleres Blech), etc.')
    
    st.write('Die beiden Abbildungen unten stellen die Leerlaufspannung und den Kurzschlusstrom für eine Messung dar. Euer Schaubild sollte so ähnlich aussehen, also eine Gerade für den Kurzschlussstrom und eine Kurve (möglicherweise ein Polynom dritten Grades oder ähnliches) für die Leerlaufspannung.')
    
    col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])
    
    with col1:
        st.write('')
        
    with col2:
        st.image('page_1_pic_6.png')
        
    with col3:
        st.image('page_1_pic_5.png')
        
    with col4:
        st.write('')
    
    st.write('Wie ihr seht, steigt der Wert der Leerlaufspannung sehr schnell nahe an den maximalen Wert heran. Selbst wenn die Hälfte der Solarzelle bedeckt ist, erreicht ihr trotzdem 95% des Endwertes. Auf der anderen Seite fällt der Wert der Leerlaufspannung schnell ab, sobald mehr und mehr der Zelle verdunkelt wird.')

    st.write('Wenn ihr euch den Verlauf des Kurzschlussstroms anschaut seht ihr ein lineares Verhalten: je mehr der Fläche der Solarzelle beschienen wird, desto größer der Kurzschlussstrom. Dort ist kein rapides Abfallen des Stroms zu sehen. Dieses Verhalten macht auch intuitiv Sinn: je mehr Fläche beschienen wird, desto mehr Elektronen können die Solarzelle verlassen und zum Stromfluss beitragen.')

    st.write('Ihr fragt euch sicherlich wofür dieser Effekt nun nützlich ist, bzw. warum es nützlich ist ihn zu kennen (vor allem auf die Spannung bezogen). Am einfachsten könnt ihr dies herausfinden, indem ihr bei Versuch 3 eine der Solarzellen in der Reihenschaltung komplett verdunkelt und euch anschaut, wie sich die Spannung ändert. Warum könnte so ein Verhalten problematisch sein?')    
    
    st.write('Die Erklärung dazu ist ganz einfach: Solarzellen werden wie in Versuch 3 in der Realität oft in Reihe geschaltet. Wenn nun eine der Solarzellen komplett verschattet wird (oder einfach defekt ist: dazu reicht auch ein lockerer Stecker aus oder eine Beschädigung durch Sturm, etc.) wird die Gesamtspannung der Reihenschaltung wesentlich geringer sein, wie im Normalzustand. So kann eine gesamte Anlage, oder zumindest ein Strang einer Anlage ausfallen, wenn nur eine Solarzelle defekt oder verschattet ist. In diesem Fall gilt: die Kette ist nur so stark wie ihr schwächstes Glied.')
    
    st.write('In der Realität kann man das Problem zum Beispiel mit sogenannten Bypass Dioden lösen: diese ermöglichen einzelne Solarzellen aus der Reihenschaltung herauszunehmen, indem der Strom um die defekte oder verschattete Solarzelle herum geführt wird. Es gibt auch andere Ansätze, wie zum Beispiel in der Abbildung unten auf der Ebene eines einzelnen Moduls, in dem der Strom durch die einzelnen Zellen nicht in einer störanfälligen Mäanderform geleitet wird sondern als eine Art Matrix oder Gitter: so können einzelne defekte Bereiche umgangen werden.')
    
    st.image('page_1_pic_7.png')
    
    st.write('Quelle: https://www.energie-experten.org/erneuerbare-energien/photovoltaik/planung/verschattung')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #
        

    
    
    
    
    
