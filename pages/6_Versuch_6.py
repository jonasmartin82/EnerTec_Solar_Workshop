
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

st.title("Versuch 6")

st.write('In diesem Versuch beschäftigen wir uns mit dem Wirkungsgrad einer Solarzelle. Dazu werdet ihr in zwei Teilaufgaben jeweils die aufgenommene Leistung der Solarzelle sowie die abgegebene Leistung der Solarzelle bestimmen. Dazu findet ihr hier zwei mal hintereinander jeweils einen Teil "Aufbau" und einen Teil "Aufgabe". Bearbeitet diese jeweils hintereinander und kombiniert die Ergebnisse am Ende. Die Hinweise zur Einstellung der Multimeter findet ihr hier jeweils im Teil "Aufgabe".')

st.image('page_6_pic_1.png')

st.write('Quelle: https://www.sbz-monteur.de/elektro/entscheidend-ist-was-hinten-rauskommt')

st.write('Für euch noch eine kleine Einführung zum Thema Wirkungsgrad: der Wirkungsgrad wird allgemein definiert als Quotient aus abgegebener Leistung oder Energie und aufgenommener Leistung oder Energie. In unserem Fall ist die aufgenommene Leistung der Teil des Lichts der auf die Fläche der Solarzelle trifft und die abgegebene Leistung die elektrische Leistung der Solarzelle. Dabei ergibt sich die elektrische Leistung der Solarzelle als Produkt aus Spannung und Stromstärke. Die einzelnen Leistungen bestimmen wir nun in den folgenden Aufgabenteilen. Dabei ist die aufgenommene Leistung immer größer wie die abgegebene Leistung, sodass der Wirkungsgrad immer kleiner wie 1 bzw. kleiner wie 100% ist.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_6_pic_2.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mV" oder "Rot mV".')

st.write('Im ersten Teil der Aufgabe bestimmen wir die aufgenommene Leistung der Solarzelle. Dazu messen wir die Bestrahlungsstärke vor der Solarzelle und bestimmen die Fläche des Solarmoduls. Platziert dazu den Strahlungssensor an ein Multimeter angeschlossen vor der Solarzelle. Dabei ist die schwarze Fläche euer Sensor. Die Bestimmung der Größe ist simpel: der Wert der Spannung in mV kann direkt in die Bestrahlungsstärke in W/m^2 umgerechnet werden, also z.B. 504 mV entsprechen demnach 504 W/m^2. Tragt diesen Wert in das Kästchen "Bestrahlungsstärke" ein.')

st.write('Nun bestimmen wir noch die Fläche der Solarzellen die beschienen wird. Um euch diesen Schritt zu erleichtern misst einfach die Breite und die Höhe des Solarmoduls und tragt diese Werte in cm in die Kästchen "Höhe" und "Breite" ein. Klickt anschließend auf den Knopf berechnen und der Wert der aufgenommenen Leistung wird euch angezeigt. Hinweis: wenn ihr alles richtig gemacht habt, solltet ihr einen einstelligen Wert in W erhalten.')

st.write('---')

col1, col2, col3 = st.columns(3)

with col1:
    val_1 = st.number_input(label='Bestrahlungsstärke in W/m^2', min_value=0, max_value=2000)
    
with col2:
    val_2 = st.number_input(label='Breite in cm', min_value=0, max_value=2000)
    
with col3:
    val_3 = st.number_input(label='Höhe in cm', min_value=0, max_value=2000)

# xxx #

if "Berechnen (Versuch 6)" not in st.session_state:
    st.session_state["Berechnen (Versuch 6)"] = False
    
if "Zeichnen (Versuch 6)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 6)"] = False

if "Erklärung (Versuch 6)" not in st.session_state:
    st.session_state["Erklärung (Versuch 6)"] = False
    
if "Einblenden (Versuch 6)" not in st.session_state:
    st.session_state["Einblenden (Versuch 6)"] = False
 
# xxx # 

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Berechnen (Versuch 6)', type='primary'):
        st.session_state['Berechnen (Versuch 6)'] = not st.session_state['Berechnen (Versuch 6)'] 
    
    Area = val_2 * val_3 * 0.0001
    P_auf = Area * val_1
    
with colC:
    st.write('')

colA, colB, colC = st.columns([0.375, 0.25, 0.375])

with colA:
    st.write('')
    
with colB:   
    if st.session_state['Berechnen (Versuch 6)']:
        st.write('Aufgenommene Leistung P_auf in W ist:', P_auf)
    
with colC:
    st.write('')
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_6_pic_3.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('Im zweiten Teil der Aufgabe bestimmen wir die abgegebene Leistung der Solarzelle. Im Sinne der Bestimmung des Wirkungsgrades, möchten wir den Punkt finden, an dem die abgegebene Leistung der Solarzelle maximal wird damit der Wirkungsgrad möglichst groß wird. Baut den Aufbau aus der Abbildung oben nach und legt im Anschluss die Tabelle an, die ihr unten findet.')

st.image('page_6_pic_4.png')

st.write('Diese Tabelle dient euch als Hilfe beim Ausfüllen bzw. während des Experiments. Diese Tabelle ist dabei wie folgt zu verstehen: wir möchten verschiedene Paare aus Spannung U und Stromstärke I testen. Dazu sind euch bestimmte Werte vorgegeben, entweder ein Wert für die Stromstärke I oder die Spannung U. Ihr könnt die verschiedenen Punkte erreichen, indem ihr den Drehregler des Messbox verändert. Sobald ihr einen der Werte ungefähr eingestellt habt, notiert euch den anderen.')

st.write('---')

st.write('Tragt alle Werte für die Spannung und die Stromstärke in den Kästchen unten ein. Mit einem Klick auf "Zeichnen" wird für euch die Leistung berechnet und das dazugehörige Diagramm erstellt. Dabei gebt ihr in den oberen Kästchen die Werte der Spannung U in V ein zu den vorgegebenen Stromstärken I in mA. In die unteren Kästchen tragt ihr entsprechend die Stromstärke I in mA für die dazugehörigen Spannungen U in V ein.')

st.write('Hinweis: falls die Messung bei euch nicht funktioniert drückt auf "Zeichnen" und danach auf "Erklärung". Zu Beginn der Erklärung ist die ausgefüllte Tabelle, mit der ihr dann selbst den Wirkungsrad berechnen könnt.')

st.write('---')

col1, col2, col3, col4 = st.columns(4)

with col1:
    val_1 = st.number_input(label='Spannung U in V (20mA)', min_value=0.0, max_value=2000.0, step=0.01)
    val_5 = st.number_input(label='Spannung U in V (130mA)', min_value=0.0, max_value=2000.0, step=0.01)
with col2:
    val_2 = st.number_input(label='Spannung U in V (50mA)', min_value=0.0, max_value=2000.0, step=0.01)
    val_6 = st.number_input(label='Spannung U in V (140mA)', min_value=0.0, max_value=2000.0, step=0.01)
with col3:
    val_3 = st.number_input(label='Spannung U in V (80mA)', min_value=0.0, max_value=2000.0, step=0.01)
    val_7 = st.number_input(label='Spannung U in V (150mA)', min_value=0.0, max_value=2000.0, step=0.01)
with col4:
    val_4 = st.number_input(label='Spannung U in V (110mA)', min_value=0.0, max_value=2000.0, step=0.01)
    val_8 = st.number_input(label='Spannung U in V (170mA)', min_value=0.0, max_value=2000.0, step=0.01)

st.write('---')

col1, col2, col3, col4 = st.columns(4)

with col1:
    val_9 = st.number_input(label='Stromstärke I in mA (1,60V)', min_value=0.0, max_value=2000.0, step=0.01)
with col2:
    val_10 = st.number_input(label='Stromstärke I in mA (1,00V)', min_value=0.0, max_value=2000.0, step=0.01)
with col3:
    val_11 = st.number_input(label='Stromstärke I in mA (0,50V)', min_value=0.0, max_value=2000.0, step=0.01)
with col4:
    val_12 = st.number_input(label='Stromstärke I in mA (0,20V)', min_value=0.0, max_value=2000.0, step=0.01)
    
st.write('')

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen (Versuch 6)', type='primary'):
        st.session_state['Zeichnen (Versuch 6)'] = not st.session_state['Zeichnen (Versuch 6)']
    
with colC:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

I_arr = [20, 50, 80, 110, 130, 140, 150, 170, val_9, val_10, val_11, val_12]
U_arr = [val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, 1.60, 1.0, 0.5, 0.2]

P_arr = []

for i in range(len(I_arr)):
    P_temp = I_arr[i] * U_arr[i]
    P_arr.append(P_temp)
    
fig1 = plt.figure(1)
plt.plot(U_arr, I_arr)
plt.title('Stromstärke I über Spannung U')
plt.xlabel('Spannung U in V')
plt.ylabel('Stromstärke I in mA')
plt.grid()

fig2 = plt.figure(2)
plt.plot(U_arr, P_arr)
plt.title('Leistung P über Spannung U')
plt.xlabel('Spannung U in V')
plt.ylabel('Leistung P in mW')
plt.grid()

if st.session_state['Zeichnen (Versuch 6)']:
    col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])
    
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig1)
    with col3:
        st.pyplot(fig2)
    with col4:
        st.write('')

    col1, col2, col3 = st.columns([0.375, 0.25, 0.375])
    
    with col1:
        st.write('')
    with col2:
        st.write('')
        st.write('Maximum der Leistung P_ab (in W) ist:', max(P_arr)/1000)
    with col3:
        st.write('')

    st.write('---')
    
    st.subheader('Frage:')    
    
    st.write('Wie groß ist nun der Wirkungsgrad (absolut und prozentual)?')
    
    st.write('Falls ihr euch unsicher seid betrachtet euch nochmal die Definition des Wirkungsgrades und welche Werte wir für die Leistungen P_auf und P_ab berechnet haben.')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 6)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 6)'):
            st.session_state['Erklärung (Versuch 6)'] = not st.session_state['Erklärung (Versuch 6)']
    with col3:
        st.write('')
    
    st.write('---')
    
# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 6)']:
    
    st.subheader('Erklärung:')
    
    st.write('Sollte eure Messung nicht funktioniert haben, könnt ihr hier die benötigte Leistung P_ab identifizieren und den Wirkungsgrad berechnen. Sollte es funktioniert haben, klappt den Rest der Erklärung unter "Einblenden" aus.')
    
    st.image('page_6_pic_5.png')
    
    st.write('')
    
    st.image('page_6_pic_6.png')
    
    col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Einblenden (Versuch 6)'):
            st.session_state['Einblenden (Versuch 6)'] = not st.session_state['Einblenden (Versuch 6)']
    with col3:
        st.write('')
    
    if st.session_state['Einblenden']:
      
        st.write('---')
        
        st.write('Sollte euer Experiment funktioniert haben könnt ihr hier eure Ergebnisse vergleichen:')
        
        st.write('Wert für Bestrahlungsstärke in W/m^2: ca. 200')
        
        st.write('Wert für Breite in cm: ca. 20')
        
        st.write('Wert für Höhe in cm: ca. 10')
        
        st.write('Wert für P_auf in W: ca. 4')
        
        st.write('Wert für P_ab in W: ca. 0,3')
        
        st.write('Wert für den Wirkunsgrad (absolut und prozentual): 0,075 bzw. 7,5%')
        
        st.write('---')
        
        st.write('Nun ist die Frage welche Bedeutung der Wirkungsgrad hat. Einerseits bedeutet ein höherer Wirkungsgrad, dass man auf der gleichen Fläche mehr elektrische Energie erzeugen kann. Dies ist bei einer begrenzten Fläche interessant, zum Beispiel bei Hausdächern. So ermöglicht ein höherer Wirkungsgrad eine größere Energieerzeugung und damit einen höheren Autarkiegrad. Autarkie bedeutet, dass man den Strom (oder sogar mehr) den man verbraucht selbst erzeugt und der Autarkiegrad gibt euch an, wie viel Prozent der Zeit pro Jahr man diese Bedingung erfüllt. Das hiilft unter anderem dabei seine Stromkosten zu senken, da der selbst erzeugte Strom vom Dach nichts kostet und man sich so spart den Strom aus dem Stromnetz zu kaufen. Abgesehen davon kann eine Solaranlage mit Speichern auch bei kurzfristigen Stromausfällen helfen die Versorgung mit Strom sicherzustellen.')
        
        st.write('Außerdem gibt es verschiedene Typen von Solarzellen bzw. genauer Photovoltaik Modulen. Diese unterscheiden sich natürlich im Wirkungsgrad, was hauptsächlich durch die Auswahl der Materialien folgt. In der Abbildung unten sieht man ein paar Beispiele für verschiedene Typen von Photovoltaik Modulen.')
        
        st.image('page_6_pic_7.png')
        
        st.write('Quelle: https://sveasolar.de/de-de/photovoltaik-ratgeber/arten-von-solarzellen')
        
        st.write('Man sieht hier die drei häufigsten Typen an Modulen, wobei monokristalline und polykristalline Solarmodule am häufigsten vorkommen. Monokristalline Solarmodule bestehen aus einkristallinem Silizium, dass heißt, dass alle Kristalle ordentlich und in die selbe Richtung orientiert sind. Diese Module haben den höchsten Wirkungsgrad mit ca. 15-22%. Polykristalline Solarmodule bestehen auch aus Silizium, allerdings ist die Kristallstruktur anders und deswegen der Wirkungsgrad geringer mit ca. 13-18%. Man kann die Typen auch einfach unterscheiden: polykristalline Solarmodule sehen blau aus, monokristalline Solarmodule sehen schwarz aus. Außerdem gibt es noch sogenannte Dünnschicht Solarmodule. Diese haben einen Wirkungsgrad von ca. 10-12% und bestehen meistens aus anderen Materialien. Diese haben den Vorteil, da sie häufig auf eine Art Kunstoff aufgetragen werden, dass sie flexibel sind und gebogen werden können. Dies ist interessant wenn man unregelmäßige Flächen verwenden möchte, zum Beispiel beim Dach eines Autos, auf Schiffen, etc.')
        
        st.write('Einflussfaktoren auf den Wirkungsgrad sind unter anderem Temperatur, Verschmutzung, Ausrichtung und Neigungswinkel sowie technologische Verbesserungen. Bezüglich der Temperaturen sind niedrigere Werte besser für den Wirkunsgrad. Die Aspekte Neigungswinkel und Ausrichtung wurden bereits in Versuch 2 und 5 besprochen, also wie diese für einen optimalen Wirkunsgrad einzustellen sind. Bezüglich technologischer Verbesserungen sind hier Forschung und Entwicklung an bestehenden und neuen Materialien sowie an der Bauweise der Solarmodule selbst gemeint. Zum Beispiel muss die Schicht über den einzelnene Solarzellen, meistens ein spezielles Glas, wenig Sonnenlicht reflektieren, soll nicht verkratzen, nicht so schnell verschmutzen und muss den Temperaturen am Aufstellunsgort standhalten.')
        
    st.write('---')
        
# ------------------------------------------------------------------------------------------------------------------------ #


