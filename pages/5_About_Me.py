import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    GitHub repository: [Annina Delacour](https://github.com/AnninaDelacour/bachelor)
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Annina Ecker: [Mastodon](https://mastodon.world/@aeae) | [LinkedIn](https://www.linkedin.com/in/)
    """
)


st.markdown("<h1 style='font-size: 60px; color: #FF8066;'>Hi :)</h1>", unsafe_allow_html=True)

st.header("Wer ich bin")
st.markdown(
    """
    Mein Name ist Annina und diese Webseite ist der praktische Teil meiner Bachelorarbeit für den Studiengang
    ***"Digital Business & Software Engineering"*** am MCI Innsbruck, wobei der Software Engineering-Aspekt im Fokus meines Studiums steht.
    """, unsafe_allow_html=True)

st.header("Wieso das Thema 'Windenergie'")
st.markdown(
    """
    Der Klimawandel betrifft uns alle, und damit auch mich. Mir persönlich ist es ein Anliegen, mich in dieser Hinsicht stetig
    weiterzubilden, auf dem Laufenden zu bleiben, und bestenfalls meine Fähigkeiten und Kenntnisse in dieser Domäne zukünftig einsetzen zu können.
    <br><br>
    Das Thema rund um Windenergie bzw. erneuerbare Energien allgemein wird uns langfristig immer mehr begleiten.
    Da in meinen Augen aber vor allem im Westen Österreichs noch zu wenig zu diesem Thema passiert, möchte ich Personen,
    die in Tirol wohnen, eine Möglichkeit bieten, sich erstmalig zu informieren und einen Überblick zu verschaffen.<br>
    Wo gibt es überhaupt wirklich Potential für Windenergie? In welchen Zonen liegen Gebiete mit bereits vorhandener, teils
    sehr guter Infrastruktur? Wie viele Naturschutzgebiete, Schutzzonen und dergleichen gibt es in Tirol?<br><br>
    Damit möchte ich meinen kleinen Beitrag leisten und mithelfen, diese - unsere - Welt nachhaltiger und somit auch 
    lebenswert(er) zu gestalten!<br><br>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center">
    <img src="https://i.ibb.co/FVdwCFd/annina-lps2022-edit.jpg"/>
</div>
""", unsafe_allow_html=True)

