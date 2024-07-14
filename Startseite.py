
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

st.title("Startseite")

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Bitte lesen!')

st.write('Herzlich Willkommen im EnerTec!')

st.write('Ihr befindet euch auf der Startseite des Solar Workshops.')

st.write('Diese Internetseite ist interaktiv aufgebaut. Ihr könnt in der Seitenleiste links die verschiedenen Seiten auswählen und entsprechend verwenden. Diese Webseite enthält mehrere Versuche aus denen ihr auswählen könnt, je nachdem was euch am meisten interessiert. Eine Übersicht über den Inhalt der Versuche findet ihr weiter unten.')

st.write('Zusätzlich gibt es noch weitere Seiten mit Zusatzinformationen und Erklärungen, wenn ihr euch intensiver mit einem Thema beschäftigen möchtet. Außerdem findet ihr auf der Seite "Aufbau Versuchskoffer" eine detaillierte Erklärung, wie ihr den Versuchskoffer für die Experimente aufbauen müsst. Auf jeder Seite eines Versuches findet ihr nochmals ein Bild zur Kontrolle des Aufbaus.')

st.write('Bei Fragen meldet euch gerne bei den Betreuern. Ansonsten: jetzt seid ihr dran, viel Spaß beim Experimentieren!')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('---')

st.subheader('Übersicht Versuche')

st.write('Hier findet ihr eine Übersicht der angebotenen Versuche mit dem Titel und einer kurzen Beschreibung')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 1: die Leerlaufspannung und der Kurzschlussstrom einer Solarzelle bei Abschattung')

st.write('In diesem Versuch messt ihr die Leerlaufspannung und den Kurzschlussstrom einer Solarzelle bei verschiedenen Stufen der Abschattung. Damit seht ihr den Effekt der Abschattung einer Solarzelle und formuliert eure Gedanken worauf bei der Platzierung einer Solarzelle zu achten ist.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 2: der Tagesgang der Sonne und der Einfluss auf den Ertrag')

st.write('In diesem Versuch bestimmen wir den Einfluss des Tagesganges der Sonne auf den Ertrag der Solarzelle indem wir den Kurzschlusstrom für verschiedene Himmelsrichtungen bestimmen. Danach könnt ihr die Frage beantworten wie man eine Solaranlage optimal ausrichtet und welche Alternativen es gibt.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 3: Reihenschaltung von Solarzellen')

st.write('In diesem Versuch messt ihr den Kurzschlussstrom und die Leerlaufspannung einer Solarzelle mit mehreren Solarzellen in Reihe geschaltet. Damit seht ihr den Effekt der Reihenschaltung und lernt, wofür diese in realen Anlagen verwendet wird.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 4: Parallelschaltung von Solarzellen')

st.write('In diesem Versuch messt ihr den Kurzschlussstrom und die Leerlaufspannung einer Solarzelle mit mehreren Solarzellen parallel geschaltet. Damit seht ihr den Effekt der Parallelschaltung und lernt, wofür diese in realen Anlagen verwendet wird.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 5: Anstellwinkel der Solarzellen')

st.write('In diesem Versuch bestimmt ihr den Einfluss des Anstellwinkels der Solarzelle zur Sonne indem wir auch hier den Kurzschlussstrom messen. Dadurch könnt ihr verstehen, warum und in welchem Winkel zum Horizont man Solarzellen platziert und wie man den Ertrag einer Solaranlage durch eine Nachführung steigern kann.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 6: Wirkungsgrad einer Solarzelle')

st.write('In diesem Versuch bestimmen wir den Wirkungsgrad der Solarzelle. Ihr lernt den Wirkungsgrad kennen, wie man ihn bestimmt und wir vergleichen unseren Wert mit dem für verschiedene Typen von Solarzellen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #





