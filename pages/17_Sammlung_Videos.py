
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

st.title('Sammlung Videos')

st.write('Auf dieser Seite findet ihr zu verschiedenen Themen gesammelt Videos die die behandelten Themen vertiefen oder neue Aspekte einführen. Dabei ist dieses Angebot nicht verpflichtend und kann von euch nach belieben angenommen werden. Gerne könnt ihr euch zwischen den Versuchen oder gegen Ende noch einige interessante Videos anschauen so wie ihr es wollt.')

st.write('Hinweis: wenn ein Video flackert klickt bitte auf das Zahnrad und deaktiviert die Option "Anmerkungen".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Koventionelle Energien')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=N5WWw0u_dNE')

    st.video('https://www.youtube.com/watch?v=iqUVR2OFqGk')
    
with col3:
    st.write('')
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Übersicht Formen erneuerbarer Energie')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=_FcKxgfgc2k')

    st.video('https://www.youtube.com/watch?v=9GjP9jCkgyY')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Erklärung Windkraft')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=KIJRuNdt1tY')

    st.video('https://www.youtube.com/watch?v=ZP-bEgvoDZQ')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Erklärung Solarenergie')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=kEujwGGoyjQ')

    st.video('https://www.youtube.com/watch?v=ZFlG4bz0Cfg')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Erklärung Wasserkraft und Biomasse')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=ccVv8BBEtVE')

    st.video('https://www.youtube.com/watch?v=kbojtMCT75I')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Energiewende')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=d-d7AAtVbLk')

    st.video('https://www.youtube.com/watch?v=A0HXc-N5qFI')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Energiespeicher')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=dyW4le3h6OU')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Sektorenkopplung')

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col1:
    st.write('')
    
with col2:
    st.video('https://www.youtube.com/watch?v=I7LZ4oytldQ')

    st.video('https://www.youtube.com/watch?v=4eB3QU65EpM')
    
    st.video('https://www.youtube.com/watch?v=n9D_4OnzKd0')
    
    st.video('https://www.youtube.com/watch?v=Ien6HQhRWcE')
    
with col3:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #


