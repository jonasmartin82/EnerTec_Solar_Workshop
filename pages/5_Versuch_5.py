
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

st.title("Versuch 5")

st.write('In diesem Versuch betrachten wir den Anstellwinkel der Solarzellen zur Waagerechten und welchen Einfluss dieser auf die erzeugte Leistung hat. Dazu messen wir ähnlich zu Versuch 2 nur den Kurzschlussstrom (den zugrundeliegenden Effekt haben wir in Versuch 1 betrachtet) um die Abhängigkeit der Leistung vom Winkel zu bestimmen. Dazu verwenden wir die Winkelskala an unserem Solarmodul, die uns Winkel zwischen 0° und 90° anzeigt.')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_5_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Das Bild unten zeigt euch nochmal als Skizze welchen Winkel wir bestimmen, nämlich den Winkel zwischen einfallendem Licht und der Oberfläche der Solarzelle. In der Erklärung besprechen wir, inwiefern dieser Winkel in der Realität verwendet wird.')

st.image('page_5_pic_2.png')

st.write('Baut das Experiment entsprechend der Abbildung oben unter "Aufbau" nach. Beginnt damit eine Tabelle auf einem Blatt anzulegen die wie folgt aussieht:')

st.image('page_5_pic_3.png')

st.write('Diese Tabelle dient euch als Hilfe beim ausfüllen bzw. während des Experiments. Beginnt bei einem Winkel von 90°, notierten den Kurzschlussstrom und fährt so für die übrigen Winkel fort.')

st.write('---')

st.write('Wenn ihr nun alle Werte bestimmt habt könnt ihr diese unten in die entsprechenden Kästchen eintragen. Mit einem Klick auf "Zeichnen" wird für euch ein Diagramm erstellt.')

col1, col2, col3, col4 = st.columns(4)

with col1:
    val_1 = st.number_input(label='Kurzschlussstrom in mA (90°)', min_value=0, max_value=2000)
    val_5 = st.number_input(label='Kurzschlussstrom in mA (30°)', min_value=0, max_value=2000)
with col2:
    val_2 = st.number_input(label='Kurzschlussstrom in mA (75°)', min_value=0, max_value=2000)
    val_6 = st.number_input(label='Kurzschlussstrom in mA (15°)', min_value=0, max_value=2000)
with col3:
    val_3 = st.number_input(label='Kurzschlussstrom in mA (60°)', min_value=0, max_value=2000)
    val_7 = st.number_input(label='Kurzschlussstrom in mA (0°)', min_value=0, max_value=2000)
with col4:
    val_4 = st.number_input(label='Kurzschlussstrom in mA (45°)', min_value=0, max_value=2000)
    
# xxx #

if "Zeichnen (Versuch 5)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 5)"] = False

if "Erklärung (Versuch 5)" not in st.session_state:
    st.session_state["Erklärung (Versuch 5)"] = False
 
# xxx # 

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen (Versuch 5)', type='primary'):
        st.session_state['Zeichnen (Versuch 5)'] = not st.session_state['Zeichnen (Versuch 5)']
    
with colC:
    st.write('')
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

x = ['0°', '15°', '30°', '45°', '60°', '75°', '90°']
val = [val_7, val_6, val_5, val_4, val_3, val_2, val_1]

fig = plt.figure(1)
plt.plot(x, val)
plt.title('Kurzschlussstrom in mA für verschiedene Winkel alpha')
plt.xlabel('Winkel alpha in °')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3 = st.columns([0.2, 0.4, 0.2])

if st.session_state['Zeichnen (Versuch 5)']:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig)
    with col3:
        st.write('')

    st.write('---')
 
    st.subheader('Frage:')    
 
    st.write('Ähnlich zu Versuch 2: wie verhält sich der Kurzschlussstrom in Abhängigkeit des WInkels? Welcher Winkel ist am besten und wieso?')

    st.write('(kurze Erinnerung an Versuch 1 und Versuch 4: die Leistung einer Anlage ergibt sich aus dem Produkt von Stromstärke I und Spannung U. Da die Spannung einer Solarzelle über einen großen Bereich konstant ist (siehe Versuch 1 mit der Abschattung -> erst bei fast vollständiger Abschattung bricht Spannung ein) muss die Stromstärke einen größeren Einfluss auf die Leistung haben. Deswegen betrachten wir hier nur den Strom I und sehen z.B. in Versuch 4, dass die Stromstärke auch hier verwendet wird, um die Leistung einer Anlage einzustellen.)')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 5)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 5)'):
            st.session_state['Erklärung (Versuch 5)'] = not st.session_state['Erklärung (Versuch 5)']
    with col3:
        st.write('')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 5)']:
    
    st.subheader('Erklärung:')
    
    st.write('Wie ihr in dem Bild unten sehen könnt ist der Verlauf des Kurzschlussstroms eine Gerade, die zu größeren Winkeln hin steigt. Theoretisch ist der Verlauf ähnlich zu einem Sinus, was ihr hier aber aufgrund der wenigen Messwerte nicht sehen könnt. Die Erklärung für dieses Verhalten ist analog zur Erklärung aus Versuch 2 mit dem Tagesgang. Deswegen doppeln sich einige Punkte im folgenden, wenn ihr Versuch 2 schon durchgeführt habt.')
    
    st.image('page_5_pic_6.png')
    
    st.write('')
    
    st.image('page_5_pic_7.png')

    st.write('Jetzt ist die Frage warum sich der Kurzschlussstrom so verhält wie er es tut. Dazu könnt ihr auch unter "Erklärung Solarenergie" im Abschnitt "Verbreitung" die Erklärung ansehen: ähnlich zur Verteilung der Strahlung auf der Erde, die sich aufgrund der Wölbung vom Äquator zu den Polen hin verringert, wird auch hier euer Kurzschlusstrom geringer, weil aufgrund des Winkels der Lampe zur Solarzelle immer weniger Licht (also eine Menge) auf die gleiche Fläche der Solarzelle trifft. Diese Größe, also allgemein gesprochen eine Menge pro Fläche zum Beispiel, bezeichnet man als Intensität. Je geringer die Intensität, desto geringer die Energie des Lichts. Sonnenlicht an einem Sommertag hat eine sehr hohe Intensität oder Energie, wohingegen zum Beispiel euer Blitz am Smartphone eine wesentlich geringere Energie hat. Anschaulich kann man die Intensität der Lampe in unserem Versuch auch fühlen: die Umgebung der Lampe wird aufgeheizt und das Licht, dass zum Beispiel auf eure Hand trifft, fühlt sich warm an, da die Energie des Lichts zum Teil von eurer Hand absorbiert wird.')

    st.write('Wenn ihr euch jetzt das Diagramm für den Winkel anschaut seht ihr, dass die beste Ausrichtung ein Winkel von 90° zur Sonne darstellt. Allerdings fällt einem auf, wenn man die Abbildung unten betrachtet oder sich das Video in "Versuch 2" anschaut, dass die Höhe der Sonne über dem Horizont nie die gleiche ist: wir starten mit einem geringen Winkel, der bis zur Mitagszeit zu seinem Maximum ansteigt und danach wieder abfällt. In der Realität gibt es zwei Varianten diesem Problem zu begegnen: entweder legt man einen Winkel fest (meistens der Winkel des Sonnenhöchststands) oder man installiert eine sogenannte Nachführung, die die Solarzelle immer optimal zur Sonne orientiert.')
    
    st.image('page_5_pic_4.png', width=800)
    
    st.write('Quelle: https://www.enargus.de/pub/bscw.cgi/d11786-2/*/*/Sonnenstandsdiagramm?search=Sonnenstandsdiagramm&op=Wiki.getwiki')
    
    st.write('Das Diagramm oben sollte euch nicht verunsichern: die drei blauen Kurven geben euch jeweils die Verläufe für drei Tage im Jahr an, hier die beiden Extremwerte mit dem Minimum am 21.12 und dem Maximum am 21.06 und der mittlere Wert am 21.03. Die schwarzen Linien verbinden die blauen Kurven zu einer bestimmten Uhrzeit. So bedeutet zum Beispiel der Schnittpunkt im roten Kreis den Winkel am 21.03 um 9 Uhr morgens mit einem Wert von ungefähr 40°. Wenn ihr wollt könnt ihr einmal die Winkel für den grünen und den lila Kreis versuchen abzulesen. Nachdem ihr dieses Diagramm verstanden habt, fällt euch vielleicht das Problem auf, welches aus einem festen Winkel folgt: ein fester Winkel passt jeweils nur für einen Tag im Jahr. Wenn ihr den optimalen Winkel für den Sommer einstellt wird der Ertrag im Rest des Jahres geringer sein und umgekehrt genauso. Um dieses Problem zu umgehen und den Ertrag zu steigern gibt es eine sogenannte Nachführung die ihr in der Abbildung unten seht.')
    
    st.image('page_5_pic_5.png')
    
    st.write('Quelle: https://www.haustechnikdialog.de/SHKwissen/Showimage.aspx?ID=5465')
    
    st.write('Diese Abbildung ist auch für Versuch 2 relevant: wie ihr seht besteht der Zweck einer einachsigen Nachführung nur darin, den Effekt des Tagesgangs auszugleichen und so den Ertrag zu steigern. Dafür wählt man hier einen festen Winkel zur Horizontalen z.B. 30° und führt die Solarzelle nur von Osten nach Westen über den Tag nach. Die ausgereifteste Lösung stellt eine zweiachsige Nachführung dar. Wie ihr euch anhand der Abbildung überlegen könnt, wird so der Effekt des Tagesgangs und die sich verändernde Höhe der Sonne über dem Horizont ausgeglichen. So wird die Fläche der Solarzelle immer senkrecht zur Sonne ausgerichtet und kann den maximalen Ertrag liefern.')
    
    st.write('Nur um ein Gefühl zu bekommen: bereits eine einachsige Nachführung kann den Ertrag um 20 bis 30% steigern, mit einer zweiachsigen Nachführung schafft man sogar eine Steigerung von 50 bis 60%! Wenn es darauf ankommt, den maximalen Ertrag zu erbringen, ist eine Nachführung für Solarzellen unverzichtbar. Allerdings sollte man die Kosten nicht außer Acht lassen, die für ein System mit Nachführung nicht unerheblich sind. Außerdem benötigen die Systeme mit einer Nachführung mehr Platz um sich bewegen zu können und nicht mit anderen Objekten zu kollidieren. So kann es je nach Einzelfall auch besser sein, eine fixe Ost/West Ausrichtung wie in Versuch 2 beschrieben zu verwenden.')
    
    st.write('---')
    
# ------------------------------------------------------------------------------------------------------------------------ #

