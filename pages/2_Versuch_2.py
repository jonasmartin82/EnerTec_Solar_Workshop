
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

st.write('In diesem Versuch untersuchen wir den Tagesgang der Sonne und welchen Einfluss dieser auf den Ertrag einer Solarzelle hat. In diesem Experiment ist der Versuchsaufbau eine Vereinfachung der Realität: da hier unsere Solarzelle im 90° Winkel zur Lampe steht, vernachlässigen wir die Höhenänderung der Bahn der Sonne. In der Realität werden Anlagen in einem bestimmten Winkel gemessen zum Horizont bzw. zur Waagerechten des Bodens installiert (in Deutschland z.B. 30°). Diesen Effekt der Winkeländerung könnt ihr in Versuch 5 untersuchen. Wir beschäftigen uns hier nur mit dem Tagesgang der Sonne, der einen erheblichen Einfluss auf die Effektivität der Solarzelle hat. Dazu messen wir in diesem Versuch den Kurzschlussstrom für verschiedene Ausrichtungen der Solarzelle.')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot A". Im Fall eines roten Multimeters müsst ihr den Wert noch mit 1000 multiplizieren bzw. das Komma drei Stellen nach rechts verschieben, damit die Einheit von "A" in "mA" umgerechnet wird.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau:')

st.image('page_2_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe:')

st.write('Im Video unten seht ihr den Tagesgang der Sonne aufgenommen von Sonnenaufgang am Morgen bis Sonnenuntergang am Abend (das eigentliche Video startet ab 0:17). Wenn man sich noch einmal an den Verlauf der Sonne erinnert, stellt man fest, dass diese auf der Nordhalbkugel im Osten aufgeht, im Tagesverlauf Richtung Süden wandert und am Abend im Westen untergeht. Auf der Südhalbkugel ist der Verlauf Osten -> Norden -> Westen (unser Versuchsaufbau wurde für den Verlauf auf der Nordhalbkugel entwickelt).')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video(data='https://www.youtube.com/watch?v=xs9hfF3UPQY')
    
with col3:
    st.write('')

st.write('Wie man in dem Video schön sieht, ändert sich im Tagesverlauf auch die Höhe der Sonne bezogen auf den Horizont. Wie bereits anfangs erwähnt untersuchen wir diesen Effekt, der sehr ähnlich zu diesem Versuch ist, in Versuch 5. Wir nehmen hier die Vereinfachung vor und nehmen an, dass die Sonne immer auf einer konstanten Höhe bleibt und die Solarzelle immer im 90° Winkel dazu steht, was dem Versuchsaufbau entspricht. So können wir den Einfluss des Tagesgangs explizit untersuchen.')

st.write('Im folgenden seht ihr eine Tabellenvorlage. Legt diese auf einem Blatt an und füllt sie während dem Experiment aus. Dabei bezeichnen die Akürzungen die Himmelsrichtungen zwischen den vier Himmelsrichtungen Norden, Süden, Osten, Westen. Zum Beisppiel bedeutet "OSO" Ost-Süd-Ost, also die Richtung zwischen Ost und Südost. Die Richtung Südost ergibt sich dabei ähnlich als Richtung zwischen Osten und Süden. Ein Blick auf die Skala auf der Rundung sollte Klarheit verschaffen, wie sich die verschiedenen Bezeichnungen zusammensetzen. Diese werden in genau dieser Weise auch beim Kompass verwendet:')

st.image('page_2_pic_2.png')

st.write('Beginnt zunächst bei einem Extrem z.B. Ost und geht so jede Himmelsrichtung bis West durch.')

st.write('---')

st.write('Wenn ihr nun alle Werte bestimmt habt könnt ihr diese unten in die entsprechenden Kästchen eintragen. Mit einem Klick auf "Zeichnen" wird für euch ein Diagramm erstellt.')

col1, col2, col3 = st.columns(3)

with col1:
    val_1 = st.number_input(label='Kurzschlussstrom in mA (Ost)', min_value=0, max_value=2000)
    val_2 = st.number_input(label='Kurzschlussstrom in mA (OSO)', min_value=0, max_value=2000)
    val_3 = st.number_input(label='Kurzschlussstrom in mA (Südost)', min_value=0, max_value=2000)

with col2:
    val_4 = st.number_input(label='Kurzschlussstrom in mA (SSO)', min_value=0, max_value=2000)
    val_5 = st.number_input(label='Kurzschlussstrom in mA (Süd)', min_value=0, max_value=2000)
    val_6 = st.number_input(label='Kurzschlussstrom in mA (SSW)', min_value=0, max_value=2000)

with col3:
    val_7 = st.number_input(label='Kurzschlussstrom in mA (Südwest)', min_value=0, max_value=2000)
    val_8 = st.number_input(label='Kurzschlussstrom in mA (WSW)', min_value=0, max_value=2000)
    val_9 = st.number_input(label='Kurzschlussstrom in mA (West)', min_value=0, max_value=2000)

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

x = ['Ost', 'OSO', 'Südost', 'SSO', 'Süd', 'SSW', 'Südwest', 'WSW', 'West']
val = [val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9]

fig = plt.figure(1)
plt.plot(x, val)
plt.title('Nachbildung eines Tagesgangs (Kurzschlusstrom über Himmelsrichtungen)')
plt.xlabel('Himmelsrichtungen')
plt.ylabel('Kurzschlussstrom in mA')
plt.grid()

col1, col2, col3 = st.columns([0.2, 0.4, 0.2])

if st.session_state['Zeichnen']:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig)
    with col3:
        st.write('')

    st.write('---')
 
    st.subheader('Frage:')    
 
    st.write('Wie verhält sich der Kurzschlussstrom bei einem Tagesgang? Welche Ausrichtung ist demnach die beste für den höchsten Ertrag?')

    st.write('(kurze Erinnerung an Versuch 1 und Versuch 4: die Leistung einer Anlage ergibt sich aus dem Produkt von Stromstärke I und Spannung U. Da die Spannung einer Solarzelle über einen großen Bereich konstant ist (siehe Versuch 1 mit der Abschattung -> erst bei fast vollständiger Abschattung bricht Spannung ein) muss die Stromstärke einen größeren Einfluss auf die Leistung haben. Deswegen betrachten wir hier nur den Strom I und sehen z.B. in Versuch 4, dass die Stromstärke auch hier verwendet wird, um die Leistung einer Anlage einzustellen.)')

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
    
    st.write('Wie ihr in dem Bild unten sehen könnt ist der Verlauf des Kurzschlussstroms eine Kurve mit dem Maximum in Richtung Süden. Zu Osten und Westen hin nimmt der Strom fast bis zu Null ab (Hinweis: ihr werdet nie einen Wert von 0mA messen können, da diffuse Strahlung der Lampe bzw. das Sonnenlicht und die Beleuchtung im Raum selbst auch von der Solarzelle absorbiert werden und somit einen Strom erzeugen.). Dieses Verhalten des Tagesganges kennt ihr sicher selbst, zum Beispiel aus dem Sommer, an dem es mittags extrem heiß wird und morgens und abends die Temperaturen spürbar niedriger sind. Das folgt unter anderem aus dem Tagesgang der Sonne.')
    
    st.image('page_2_pic_5.png')
    
    st.write('')
    
    st.image('page_2_pic_6.png')

    st.write('Jetzt ist die Frage warum sich der Kurzschlussstrom so verhält wie er es tut. Dazu könnt ihr auch unter "Erklärung Solarenergie" im Abschnitt "Verbreitung" die Erklärung ansehen: ähnlich zur Verteilung der Strahlung auf der Erde, die sich aufgrund der Wölbung vom Äquator zu den Polen hin verringert, wird auch hier euer Kurzschlusstrom geringer, weil aufgrund des Winkels der Lampe zur Solarzelle immer weniger Licht (also eine Menge) auf die gleiche Fläche der Solarzelle trifft. Diese Größe, also allgemein gesprochen eine Menge pro Fläche zum Beispiel, bezeichnet man als Intensität. Je geringer die Intensität, desto geringer die Energie des Lichts. Sonnenlicht an einem Sommertag hat eine sehr hohe Intensität oder Energie, wohingegen zum Beispiel euer Blitz am Smartphone eine wesentlich geringere Energie hat. Anschaulich kann man die Intensität der Lampe in unserem Versuch auch fühlen: die Umgebung der Lampe wird aufgeheizt und das Licht, dass zum Beispiel auf eure Hand trifft, fühlt sich warm an, da die Energie des Lichts zum Teil von eurer Hand absorbiert wird.')

    st.write('Wenn ihr euch jetzt das Diagramm für den Tagesgang anschaut, sollte euch klar werden, dass die beste Ausrichtung einer Anlage Richtung Süden sein wird (entsprechend mit einem Winkel zur Horizontalen, den wir hier nicht weiter betrachten). Dies ist sinnvoll, da die Sonne um die Mittagszeit herum die höchste Intensität hat und in diesem Zeitraum aus Richtung Süden scheint. Natürlich ist es auch möglich eine Anlage Richtung Osten, Westen oder in beide Richtungen auszurichten, allerdings verpasst man dann das Maximum der Sonneneinstarhlung im Süden und anderseits wird dadurch auch die Zeit geringer, in der die Anlage beschienen wird. Man überlege sich eine Anlage die Richtung Osten ausgerichtet ist: sie wird ihren maximalen Ertrag am Morgen erbringen und gegen Mittag, spätestens jedoch gegen Abend keinen oder nur minimalen Ertrag liefern, da die Anlage dann nicht mehr oder nur kaum von der Sonne beschienen wird.')
    
    st.image('page_2_pic_3.png')
    
    st.write('Quelle: https://www.ibc-blog.de/2013/08/freiflachenanlagen-ost-west-ist-das-neue-suden/')
    
    st.write('Nichtsdestotrotz gibt es wie ihr in der Abbildung oben sieht auch Anlagen, die absichtlich Richtung Osten und/oder Westen ausgerichtet werden. Lasst euch dabei nicht von den Zahlen verunsichern, betrachtet euch nur die gelbe Fläche und die blaue und grüne Kurve. Die grüne Kurve gibt die erzeugte Leistung an, die blaue Kurve die verbrauchte Leistung durch z.B. ein Haus oder eine Fabrik und die gelbe Fläche markiert den Bereich, in dem ihr die erzeugte Leistung der Solaranlage selbst verbraucht. Es sollte euch auffallen, dass eine Ost/West Ausrichtung erlaubt fast den ganzen Tag über den benötigten Strom oder sogar mehr zu erzeugen, wie verbraucht wird. Demgegenüber liegt eine vergleichbare Solaranlage mit Südausrichtung immer unterhalb der Verbrauchskurve.')
    
    st.write('Anzumerken sei hier, dass die Anlage in Ost/West Richtung größer ist und deswegen andere Werte an Leistung erreicht, was sich mit dem nächsten Bild erklären lässt. Außerdem lässt sich eine Anlage in Ost/West Richtung nur auf Flachdächern von z.B. Fabriken oder einem freien Feld installieren. Bei einem normalen Hausdach in Ost/West Ausrichtung würde immer ein Teil der Anlage vom Dach selbst beschattet werden, sodass der Vorteil der Ausrichtung verschwindet. Zusätzlich sollte euch auffallen, dass das Maximum bei der Ost/West Ausrichtung trotzdem symmetrisch in der Mitte liegt. das liegt daran, dass hier beide Richtungen, also Ost und West betrachtet werden und sich somit die einezlnen Kurven addieren und in der Mittagszeit beide Solarzellen (also die in Ost und West Richtung) beschienen werden. Diese Aspekte lassen sich gut in der Grafik unten beobachten und verstehen.')

    st.image('page_2_pic_4.png')
    
    st.write('Quelle: https://gruenes.haus/pv-anlage-ost-west-ausrichtung/')
    
    st.write('Man sieht hier gut die Vorteile der Ost/West Ausrichtung: bei gleicher Fläche kann man auf einer ebenen Fläche deutlich mehr Solarzellen platzieren und so mehr Leistung erreichen, da man kein Abstand wegen Schattenwurf berücksichtigen muss. So kann man auf einen Verzicht der Süd Ausrichtung den Ertrag sogar erhöhen.')

    st.write('---')
    
# ------------------------------------------------------------------------------------------------------------------------ #
