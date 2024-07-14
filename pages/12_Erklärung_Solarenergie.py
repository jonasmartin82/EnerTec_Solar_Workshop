
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

st.title('Erklärung Solarenergie')

st.write('Auf dieser Seite soll die Solarenergie erklärt werden. Dabei beschäftigen wir uns mit der Quelle der Energie, ihrer Verbreitung und deren Nutzung.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Quelle')

st.image('page_12_pic_1.png', width=600)

st.write('Quelle: https://www.kindernetz.de/wissen/steckbrief-die-sonne-102.html')

st.write('Die Quelle der Solarenergie ist, wie der Name schon vermuten lässt, unsere Sonne selbst. In dem Stern unseres Sonnensystems findet dabei ein Prozess statt, der sich Kernfusion nennt. Dabei verbinden sich im Gegensatz zur Atomkraft, wie wir sie kennen, mehrere kleine Atome Wasserstoff zu einem größeren Atom Helium und setzen dabei zusätzliche Energie frei.')

st.image('page_12_pic_2.PNG')

st.write('Quelle: https://sonnenallianz.spitzen-praevention.com/sonne-und-gesundheit/unsere-sonne/')

st.write('Die dabei freigesetzte Energie wird als elektromagnetische Strahlung bezeichnet. Der für uns nutzbare Teil des Lichtes reicht dabei vom UV-Licht bis zur Infrarot Strahlung. Als Kriterium zur Einteilung der verschiedenen Arten des Lichtes wird die Wellenlänge in Nanometern (nm) verwendet. Dies ist für die weiteren Betrachtungen aber nicht relevant.')

st.write('UV-Strahlung ist für uns Menschen nicht sichtbar und wird hauptsächlich für medizinische Anwendungen oder zum Desinfizieren von Objekten eingesetzt. Diese Strahlung ist gefährlich für den Menschen, weil sie Verbrennungen (auch als Sonnenbrand bekannt) und andere Erkrankungen hervorrufen kann. Glücklicherweise schützt uns unsere Erdatmosphäre, genauer gesagt das Ozon darin, vor einem Großteil der Strahlung. Ohne die Ozonschicht der Erde wäre ein Leben so wie wir es kennen nicht möglich.')

st.write('Auf der anderen Seite ist Infrarot Strahlung für uns in den meisten Fällen ungefährlich. Die Infrarot Strahlung wird auch als Wärmestrahlung bezeichnet und kennt ihr aus dem Alltag. Ihr spürt sie an einem warmen Tag in der Sonne oder in der Nähe eines Feuers. Diese Strahlung ist auch der Grund für den Treibhauseffekt. Bestimmte Materialien, darunter auch Gase und Wasserdampf, reflektieren diese Strahlung, sodass es in einm geschlossenen Raum wärmer wird. Diesen Effekt kann man bei einem Gewächshaus oder unserer Erde (mit ihrer Atmosphäre) selbst beobachten.')

st.write('Es fehlt noch das sichtbare Licht, welches für uns Menschen für die Sinneswahrnehmung am wichtigsten ist: dieses ermöglicht erst unser Sehen. Außerdem funktioniert die Photosynthese, also der Prozess, mit dem Pflanzen Sauerstoff erzeugen, genau mit dieser Strahlung.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Verbreitung')

st.image('page_12_pic_5.png')

st.write('Quelle: https://www.rechnerphotovoltaik.de/photovoltaik/voraussetzungen/sonneneinstrahlung')

st.write('Auf der Abbildung oben seht ihr die Verteilung der Summe der Strahlung über ein Jahr aufsummiert für Deutschland. Wenn ihr einen Blick auf die Skale wirft, seht ihr, dass die Werte umso größer werden, je mehr man Richtung Süden und Südosten geht.')

st.write('Könnt ihr euch vorstellen, warum diese Verteilung so ist? Wo ist es demnach sinnvoll Solaranlagen aufzustellen?')

st.image('page_12_pic_6.png')

st.write('Quelle: https://echtsolar.de/globalstrahlung/')

st.write('Das Bild zeigt die Verteilung der Jahressumme weltweit. Auch hier ist ein Muster zu erkennen. Betrachtet die Karte genau und vergleicht diese mit einer Ansicht von z.B. Google Maps in einem neuen Fenster. Aktiviert hier am besten unter "Ebenen" die Option "Gelände" die euch die Topologie, also die Höhe des Geländes anzeigt.')

# xxx #

if "Erklärung" not in st.session_state:
    st.session_state["Erklärung"] = False
 
# xxx #  

colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Erklärung', type='primary'):
        st.session_state['Erklärung'] = not st.session_state['Erklärung']
    
with colC:
    st.write('')

if st.session_state['Erklärung']:
    
    st.write('---')
    
    st.subheader('Erklärung')
    
    st.image('page_12_pic_7.png')
    
    st.write('Quelle: https://www.ardalpha.de/wissen/umwelt/klima/wetter-atmosphaere-meteorologie-wolken-wind-regen-luft-100.html')
    
    st.write('Die Abbildung oben zeigt den Hauptgrund für die Verteilung der Strahlung. Unsere Erde ist eine Kugel und dadurch, verteilt sich die selbe Menge an Strahlung unterschiedlich, je nachdem wo sie auf die Erde trifft. In diesem Fall sieht man, dass sich die Strahlung nahe der Pole auf eine viel größere Fläche aufteilt und somit die Summe über ein Jahr deutlich geringer ist wie in der Äquator Region. Dieser Effekt ist selbst über die, im Verhältnis zum Umfang der Erde, geringe Länge Deutschlands zu sehen.')
    
    st.write('Ein weiterer Aspekt, der für die Intensität, also die Stärke der Strahlung verantwortlich ist, ist ide Höhe eines Punktes auf der Erde (häufig zum Meeresspiegel gemessen). Die Erklärung ist ganz einfach: je höher ein Punkt liegt, desto geringer ist die Höhe der Atmosphäre, die sich über diesem Punkt befindet (da die Höhe der Atmosphäre an jedem Punkt der Erde ungefähr gleich ist) und somit wird weniger der Strahlung absorbiert oder an andere Punkte gestreut. Deswegen sieht man auf der Karte oben, die die ganze Welt darstellt, auch bei großen Gebirgen eine Erhöhung der Strahlung. Dies erklärt auch den Anstieg der Werte in Deutschland Richtung Süden und Südosten, da in Deutschland die durchscnittliche Höhe über dem Meeresspiegel von Norden nach Süden bzw. Südosten ansteigt.')
    
    st.write('Abgesehen davon gibt es weitere Aspekte, die einen Einfluss haben, die sich in der Regel unter dem Punkt Wetter zusammenfassen lassen können. Als ein Beispiel dafür könnt ihr euch einmal die Mitte Afrikas anschauen. Hier seht ihr, obwohl diese Gegend näher am Äquator liegt, dass die Strahlung geringer ist. Dies liegt an dem Klima der Region. In dieser Region entstehen (fast) jeden Tag große Wolken, die die Strahlung der Sonne von der Erde fernhalten und so die Strahlung am Boden verringern.')
    
st.write('---')
   
# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Nutzung')

st.write('Die Solarenergie lässt sich auf vielfältige Art und Weise nutzen. Im folgenden sollen die beiden Hauptanwendungen kurz vorgestellt werden.')

st.image('page_12_pic_3.png')

st.write('Quelle: https://www.brenner-energie.de/aktuelles-artikel/monokristallin-vs-polykristallin-eine-frage-des-geschmacks')

st.write('Die Abbildung oben zeigt zwei Photovoltaikzellen. Das Wort setzt sich aus dem griechischen Wort für Licht und Volt (für elektrischen Strom) zusammen. Wie die Erklärung andeutet, entsteht dabei elektrischer Strom durch die Einstrahlung von Licht. Photovoltaikzellen werden aus Silizium hergestellt, welches aus gewöhnlichem Quarzsand gewonnen wird. Nach dessen Aufbereitung werden flache Scheiben aus dem Material geschnitten und in Form einer Zelle wie oben zu sehen in ein Gehäuse eingefasst. Dabei unterscheidet man in mono- und polykristalline Photovoltaikzellen, wobei die monokristallinen schwarz sind und die polykristallinen blau sind. Der Unterschied in der Farbe ergibt sich aus einer anderen Anordnung der Kristalle im Material.')

st.image('page_12_pic_4.png')

st.write('Quelle: https://www.fm-solar.de/solarkollektor-shc24_46524_5414/')

st.write('Die Abbildung oben zeigt einen Solarthermie-Kollektor. Das Wort setzt sich aus den Worten für Sonne und Wärme zusammen und beschreibt die Funktion gut. Durch eine Flüssigkeit in den schwarzen Röhren, wird die Energie des Lichts absorbiert und an die Flüssigkeit übergeben, mit der sich unter anderem warmes Wasser erzeugen oder eine Heizung betreiben lässt. Diese Anlagen sind seltener wie Photovoltaikzellen, können aber bei kleiner Fläche im Sommer ein gesamtes Haus mit warmen Wasser versorgen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Anteil am Strommix')

st.write('Im folgenden beschäftigen wir uns mit dem Anteil der Solarenergie an der Stromerzeugung beziehungsweise dem Anteil des Stroms an der Gesamtenergie.')

st.image('page_12_pic_8.png')

st.write('Quelle: https://www.unendlich-viel-energie.de/mediathek/grafiken/der-strommix-in-deutschland-im-jahr-2023')

st.write('Die Abbildung oben zeigt den Strommix in Deutschland im Jahr 2023. Man sieht, dass die erneuerbaren Energien einen Anteil von 52% an der gesamten Stromerzeugung haben. Die Photovoltaik nimmt mit 11,9% an der Gesamtstromerzeugung neben der Windkraft den größten Anteil ein. Auch wenn diese Zahlen vielversprechend aussehen, ist noch ein großer Bedarf vorhanden erneuerbare Energien weiter auszubauen damit unser Strom irgendwann zu 100% aus erneuerbaren Energiequellen gewonnen werden kann.')

st.image('page_12_pic_9.png')

st.write('Quelle: https://www.umweltbundesamt.de/daten/energie/primaerenergieverbrauch#definition-und-einflussfaktoren')

st.write('Ein weiterer Aspekt ist der Primärenergieverbrauch, der neben dem Stromverbrauch auch sämtliche anderen Formen der Energie beinhaltet wie zum Beispiel Benzin oder Diesel für Autos und LKW oder Gas für euere Heizung. Betrachtet man hier den Gesamtanteil der erneuerbaren Energien am Primärenergieverbrauch sieht man, dass der Anteil wesentlich geringer ist und nur 19,6% in 2023 betrug. Ohne weiter auf diese Thematik eingehen zu wollen, sollte erwähnt werden, dass auch nach und nach andere Bereiche elektrifiziert werden, also vorhandene Technologien durch Strom ersetzt werden. So geschieht dies bereits durch E-Autos im Verkehrsbereich oder durch Wärmepumpen im Bereich der Heizung. Diese Faktoren bedeuten, dass wir nicht nur 100% des jetzigen Stromverbrauches durch erneuerbare Energien decken müssen, sondern langfristig einen Großteil, wenn nicht sogar den ganzen Primärenergieverbrauch. Man sieht also, dass uns noch eine Menge Arbeit bevorsteht, um unsere Gesellschaft langfristig auf erneuerbare Energien umzustellen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #



    
    
    
