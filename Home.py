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
    Annina Ecker: [Mastodon](https://mastodon.world/@aeae) | [LinkedIn](https://www.linkedin.com/in/annina-ecker/)
    """
)


st.title("Windenergie Tirol")
st.markdown("""
Auf dieser Webseite findest du viele Informationen zum Thema <strong>Windenergie in Tirol</strong>.
Darunter finden sich auch diverse interaktive Karten (oder Windatlanten), mit welchen du sehen kannst, wo potentielle Standorte für Windräder
in Tirol sind, wie es mit dem Windpotential allgemein aussieht (gibt es davon überhaupt genug, um Windräder in Tirol aufzustellen?),
und Grafiken, die Vergleiche zwischen Tirol und dem gesamten österreichischen Gebiet aufzeigen.
""", unsafe_allow_html=True)


st.markdown("""
_________________________________________________________________
""")

st.header("Was ist ein Windatlas und wofür braucht man das?")
st.markdown(
    """
    Ein Windatlas ist eine Art Karte, die die Windverhältnisse in einer bestimmten Region darstellt.
    Diese Karten zeigen in der Regel die Windgeschwindigkeit und -richtung an verschiedenen Orten in der Region 
    und können auch Informationen über die Windverteilung im Laufe des Jahres enthalten. 
    Windatlasse werden oft verwendet, um die Auswirkungen von Windenergieprojekten auf die Umwelt vorherzusagen 
    und um die besten Standorte für Windenergieanlagen zu bestimmen.
    """
)



st.subheader("Und wieso ist das nun wichtig?")

st.markdown("""

Auf der Webseite <https://windfakten.at> sind eine Vielzahl an Informationen, Statistiken und andere nützliche Hinweise 
zum Thema Windenergie, Windkraft und dergleichen zu finden.
Hier findet man unter anderem "Windfakten", die einem vor Augen führen, weshalb es im Kampf gegen den Klimawandel 
(aber nicht nur in Sachen Klimawandel) wichtig ist, sich mit dieser Thematik auseinanderzusetzen:
""")

st.info(""" 

- Ein einziges Windrad mit 5 Megawatt Leistung erzeugt pro Jahr Strom für rund 3.700 Haushalte.

- Durch das erhöhte Windaufkommen im Jahr 2019 konnte die Windkraft in Österreich rund 13 Prozent zur Stromversorgung beitragen.

- Die Windräder in Österreich erzeugen Strom für mehr als 50 Prozent aller österreichischen Haushalte.

- Mit dem Strom, den ein Windrad in einer Stunde erzeugt, kann man 65 Jahre lang täglich eine Stunde fernsehen.

- Mit dem Strom, den ein Windrad in einer Stunde erzeugt kann man mehr als 15.000 Liter Wasser kochen.

- Mit dem Strom, den ein Windrad in einer Stunde erzeugt kann man zwei Jahre lang rund um die Uhr Playstation spielen.

- Mit dem Strom den ein Windrad (3MW) in einer Sekunde erzeugt kannst Du 7,5 Liter Wasser zum kochen bringen. (Stand: April 2020)

- Mit dem Strom, den ein Windrad in einer Sekunde produziert, kann man 4 Tage "Last Christmas" anhören. (Stand: Dez. 2019)

- Mit dem Strom, den ein Windrad in einer Sekunde produziert, kann man 2 Häferl Glühwein kochen. Da sind immerhin gut 7.000 Häferl stündlich pro Windrad. (Stand: Dez. 2019)

- Windkraft spart 350 Mio. Euro jährlich durch vermiedene Stromimporte. (Stand: Oktober 2019)""")

st.markdown(""" Österreich hat somit noch sehr viel Potentiale, die es ausschöpfen kann, um nicht nur ökonomisch, 
sondern auch weitesgehend ökologisch Strom zu erzeugen!
Grüner und günstiger Strom kommt uns alle zugute; je mehr Autonomie wir über unseren Strom haben, desto weniger können wir 
von Krisen gebeutelt werden. Zudem schaffen wir nachhaltige Arbeitsplätze und
können so den Ausbau als auch die Weiterentwicklung solcher Technologien fördern und fordern.""", unsafe_allow_html=True)

st.markdown("""
_________________________________________________________________
""")


st.header("Wenn Windkraft so toll ist, wieso stellt man nicht einfach überall Windräder auf?")

st.markdown(""" 
Selbst wenn die Bedingungen günstig sind, gibt es gesetzliche Regelungen als auch ethische Einwände, 
die eine Umsetzung erschweren. Da ein Windrad auch betrieben werden muss, benötigt man:
- Eine gut funktionierende Infrastruktur für dauerhafte Benutzung
- Anschluss ans Stromnetz

Diese beiden Punkte wirken zunächst nicht überwältigend, bedeuten aber eine intensive Auseinandersetzung mit:
- geeigneten Standorten, die auf Dauer günstig gelegen sind, aber auch 
- Standorte, bei denen eine Wartung der Anlagen und Turbinen möglich ist
- als auch den Einfluss auf das Leben der Bewohnerinnen und Bewohner vor Ort bzw. in der Nähe der Windturbinen und -anlagen
- und den Einfluss der Turbinen und Anlagen auf das umgebende Ökosystem

Wie man auf der [Zonenkarte](Zonenkarte) sehen kann, gibt es viele Naturschutzgebiete u.ä. Das bedeutet,
neben diesen Faktoren muss man sich auch mit vielen Gesetzen auseinandersetzen. In Österreich können die Bundesländer 
sehr vieles für sich selbst entscheiden, denn es gilt das bundesstaatliche Prinzip.<br>
Es wird notwendig sein, abzuwägen, wie hoch ein potentieller Schaden in Kauf genommen werden kann für Pilotprojekte.
Hierzu braucht es die Zusammenarbeit mit verschiedenen Interessensgruppen und den Austausch von Expertinnen und Experten.
Das <strong>gemeinsame Ziel</strong>, den fortschreitenden Klimawandel zu bremsen 
und ein noch viel drastischeres Artensterben zu verhindern, muss dabei immer im Mittelpunkt bleiben.<br><br>

<b><font color='red'>Stirbt unser Ökosystem, haben auch wir keine Chance auf eine stabile und funktionierende Zukunft.</font></b>
""", unsafe_allow_html=True)


st.markdown("""
_________________________________________________________________
""")


st.header("Können Windräder nicht gefährlich sein für Tiere? Verschandeln sie nicht zusätzlich das Landschaftsbild?")

st.markdown(""" 
[Wenn wir unsere Natur schützen und erhalten wollen](https://windfakten.at/?xmlval_ID_KEY[0]=1272), darf in dieser Diskussion die Frage bezüglich des allg. Natur- und 
Artenschutzes nicht fehlen.<br>
[Windräder können potentiell für Tiere ein Riskio darstellen](https://naturschutz.ch/news/forschung/windturbinen-auf-stand-by-weniger-kollisionen-mit-fledermaeusen/123806). Es ist faktisch nicht wahr, dass es keinerlei Auswirkungen hat;
Wald- und Wildtiere ändern ebenso ihr Verhalten und passen sich an wie auch ihre hochentwickelten Nachbarn - wir Menschen.
Jedoch können nicht alle gleich gut oder schnell ihr Verhalten anpassen. Zudem erleben wir seit Jahren, dass mehr und mehr Arten 
aussterben oder davon bedroht sind, auszusterben. Da ein gesundes Ökosystem ein komplexes System darstellt, zu dem Insekten, Vögel,
Hirsche, Wölfe, Luchse uvm., gehören, braucht es den Dialog zwischen verschiedenen Expertinnen und Experten, die diese Themen seit 
vielen Jahren eingehend studieren und sich auch mit der Situation in unseren Nachbar\:innenländern befassen (Schweiz, Italien, Deutschland).
<br>
Allerdings gilt dies alles nicht nur für Windenergie: [Auch bezüglich Wasserkraft sollten wir nicht die Augen davor verschließen, dass 
Schäden für die Umwelt entstehen.](https://naturschutz.ch/news/natur/jeder-fuenfte-fisch-stirbt-bei-der-passage-von-wasserkraftturbinen/165366)<br>

Auch wenn [Lobbyist\:innen aus der Kohle- und Erdölindustrie versuchen, nach wie vor ihre eigene Agenda durchzubringen](https://www.lobbycontrol.de/lobbyismus-und-klima/lobbyismus-bremst-klimaschutz-problematische-naehe-zwischen-fossiler-industrie-und-politik-92893/), gibt es 
viele Personen, die an [besseren Lösungen](https://link.springer.com/article/10.1007/s41064-021-00141-4) forschen. Wir sollten ihnen 
endlich die Möglichkeit geben, sich vor einem breiteren Publikum zu äußern. Und genau das sollten wir von unseren Politiker\:innen verlangen:
Eine öffentliche Debatte, bei der auch WIR mitreden und gehört werden.
<br>

Ein nicht zu vernachlässigendes Thema ist auch das Landschaftsbild, das mittel- bis längerfristig 
durch Windräder verändert wird. Auch wenn Geschmäcker verschieden sind, so ist es doch essentiell notwendig, diese Debatte 
auf persönlicher, aber auch politischer Ebene zu führen. Eine [Studie aus dem Jahr 2021](https://www.mdpi.com/2073-445X/10/7/693),
die sich mit dem Tourismus in Island beschäftigt hinsichtlich der Frage, welche Auswirkungen das Aufstellen von Windrädern auf 
der Insel hätte. Die befragten Personen waren im Schnitt alle sehr negativ eingestellt, denn ihrer Meinung nach kämen Tourist\:innen
vor allem deswegen gerne nach Island, um "unberührte Natur" vorzufinden. <br>
Man sollte nicht leichtfertig mit diesem Thema umgehen, denn der Erholungsfaktor in manchen Regionen ist von wirtschaftlich großer Bedeutung.
<br>
<br>
[Aber auch hier gibt es bereits Menschen, die mithilfe innovativer Ideen helfen wollen,](https://enerkite.de/)
 solche und ähnliche Debatten zu lösen: [KiteKraft](https://www.kitekraft.de/de/fliegende-windkraft)



""", unsafe_allow_html=True)


st.markdown("""
_________________________________________________________________
""")


st.header("Und was ist mit Wasserkraft? Ich dachte, Österreich sei ein \"Wasserkraft-Land\"...")

st.warning("""
"Strom aus Wasserkraft hat ein gutes Image.\n
Zu Unrecht, denn erst auf den zweiten Blick wird deutlich: Das Wasser ist erneuerbar, 
die zerstörten Lebensräume sind es jedoch nicht. Daher muss der Wasserkraft-Ausbau ökologisch 
und sozial verträglich erfolgen.
 Die Rücksichtnahme auf die Natur wird in der Praxis jedoch grob vernachlässigt.\n
Unter dem Argument des öffentlichen Interesses werden Kraftwerke in ökologisch sensiblen Flussstrecken bewilligt. 
Damit handelt Österreich europäischen Gesetzen zuwider, 
die uns verpflichten den Zustand unserer Gewässer nicht weiter zu verschlechtern. 
Mittels politischer Weisungen werden selbst nicht genehmigungsfähige Kraftwerke wie 
z.B. das Kraftwerk Lesachbach (Oberstufe) in Osttirol durchgewinkt. 
Dabei steht der minimale Beitrag zur Energiewende, den solche Kleinkraftwerke leisten in keinem Verhältnis 
zur angerichteten Naturzerstörung.\n
Es fehlt ein Gesamtkonzept, das festlegt, wo und unter welchen Bedingungen
 Wasserkraft noch möglich ist, und wo Flussjuwele für zukünftige Generationen bewahrt werden."
""")

st.markdown("Quelle: [WWF - Wasserkraft in Österreich](https://www.wwf.at/das-schuetzen-wir/fluesse/wasserkraft-in-oesterreich/)", unsafe_allow_html=True)

st.markdown("""
Wasserkraft alleine wird nicht ausreichen. [Bei bereits mehr als 5.200 Kraftwerken in Österreich, 
die bereits eine Belastung für Fließgewässer sind, braucht es Alternativen](https://www.fluessevollerleben.at/aktuelle-bedrohung-karte/).
<br>Außerdem: Wasserkraft ist vor allem in den wärmeren Monaten ideal und "ertragreich" (Frühling bis Herbst), 
im Winter punkten jedoch *Windkrafträder. Fügen wir dem Bild noch PV-Anlagen hinzu, könnten wir auf lange Sicht einen "grünen 
Energiekreislauf" entwickeln.
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .small-text {{
        font-size: 11px;
    }}
</style>
<span class="small-text">* [1)](https://www.igwindkraft.at/?mdoc_id=1042884), 
[2)](https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.msg-id-90116.html),
 [3)](https://www.planet-wissen.de/technik/energie/erneuerbare_energien/windenergie-110.html)
</span>
""", unsafe_allow_html=True)


st.markdown("""
_________________________________________________________________
""")

st.header("Okay, okay... Aber was kann ich tun?")

st.markdown(""" 
Im ersten Schritt ist es wichtig, mehr Bewusstsein für dieses Thema, das uns alle betrifft, zu schaffen.<br>
Gerne kannst du diese Seite mit anderen Teilen, dich überall durchklicken und auch die anderen Webseiten,
die hier geteilt werden, ansehen.<br>
Auch wenn es oft nicht so scheint, es gibt VIELE Personen,
die sich mit dieser Problematik bereits viel befasst haben bzw. befassen, und sehr gute 
und gut verständliche Beiträge veröffentlicht haben.<br>
<br>
Hier eine Liste dazu:
- [Faktencheck (Profil) - ÖVP liegt falsch: Windräder sind auch in Tirol wirtschaftlich sinnvoll](https://www.profil.at/faktiv/oevp-liegt-falsch-windraeder-sind-auch-in-tirol-wirtschaftlich-sinnvoll/402017754)
- [WWF - Mythos Wasserkraft](https://www.fluessevollerleben.at/wp-content/uploads/2019/11/Broschuere_Mythos_Wasserkraft-Ansicht.pdf)
- [IG Windkraft (Austrian Wind Energy Association) - Windenergie in Österreich](https://windfakten.at/?xmlval_ID_KEY[0]=1234)
- [Kleine Windkraft AT - Wie funktioniert ein Windrad?](https://www.kleinewindkraft.at/?xmlval_ID_KEY%5b0%5d=1276)
- [Gotthard Windpark Schweiz - Eine Vorschau für AT?](https://www.aet.ch/DE/Gotthard-Windpark-fa0c5600)
- [WWF - Windkraft in der Schweiz](https://www.wwf.ch/de/unsere-ziele/windenergie-die-optimale-ergaenzung-fuer-die-stromproduktion-in-der-schweiz)
- [SDG Watch Austria](https://www.sdgwatch.at/de/ueber-sdgs/)


Es gibt natürlich auch etwas detailliertere Lektüre - für all jene, die sich gern mehr und umfassender damit beschäftigen wollen:
- [IG Windkraft - Windkraftausbau 2022 + Vorschau 2023](https://windfakten.at/mmedia/download/2023.01.17/1673942588253231.pdf)
- [IPCC - Sixth Assessment Report; Climate Change 2022: Impacts, Adaption and Vulnerability](https://www.ipcc.ch/report/ar6/wg2/)
- [Österreich SDGs (Sustainable Development Goals) und die Agenda 2030](https://sustainabledevelopment.un.org/content/documents/26661VNR_2020_Austria_Report_German.pdf)
- [WWF - Positionspapier EAG 2020](https://www.wwf.at/wp-content/uploads/2021/08/EAG-2020_Positionspapier-WWF-Oesterreich-und-Umweltdachverband.pdf)
- [Austrian Power Grid AG - Stromversorgung](https://www.apg.at/stromnetz/netzausbau/netzentwicklungsplan-2021/)

Wer lieber Videos schaut, kann sich beispielsweise von Kurzgesagt einiges ansehen
(in der Videobeschreibung findet man auch einen Link zu allen Studien, auf die die Videos aufbauen!):
""", unsafe_allow_html=True)

kurzgesagt_de_fix_climate = "https://www.youtube.com/watch?v=FvjbhiILmPk"
kurzgesagt_de_nuclear = "https://www.youtube.com/watch?v=vcsmWBqa2LQ"
wdr_mailab = "https://www.youtube.com/watch?v=oJ1zm65u-ck"
quarks = "https://www.youtube.com/watch?v=itllxeBM8ro"

col1, col2 = st.columns(2)

with col1:
    st.video(kurzgesagt_de_fix_climate)

with col2:
    st.video(wdr_mailab)

col3, col4 = st.columns(2)

with col3:
    st.video(kurzgesagt_de_nuclear)

with col4:
    st.video(quarks)

st.markdown("""
_________________________________________________________________
""")

st.markdown("""
[Je mehr Menschen darüber sprechen](https://www.youtube.com/watch?v=VxOSGe8HG8o), je mehr Menschen sich informieren (können) und aufgeklärt diesem Thema gegenübertreten,
desto schwerer wird es für Politiker und Politikerinnen, diesem Bereich aus dem Weg zu gehen und fadenscheinige Argumente 
zu liefern.<br>
<b>Daher ist die eigenständige Aufklärung und das "unter die Leute bringen" so wichtig!</b><br>

<b>Du</b> kannst jederzeit deinen Beitrag leisten, auf vielfältigste Art und Weise!<br>
Nachhaltiger und bewusster Konsum (von Lebensmittel, Kleidung, Elektro-Geräte, usw.).
<br>Aber auch, wenn du [dich selber informierst und mit anderen austauscht](https://www.youtube.com/watch?v=sTPSM5f23IY). <br>
Fordere DEIN Recht auf einen lebenswerten Planeten ein!<br><br>
Wie schon der 14. Dalai Lama (Tenzin Gyatso) sagte:<br>
""", unsafe_allow_html=True)

st.markdown("""
<span style="color: #2cb978; font-variant: italic; font-size: 30px;">
"Falls du glaubst, dass du zu klein bist, um etwas zu bewirken, 
<br>dann versuche mal zu schlafen, wenn eine Mücke im Raum ist."</span>
""", unsafe_allow_html=True)
