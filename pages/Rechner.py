import streamlit as st

st.title("Notenrechner")

st.write("Mit diesem Rechner könnt ihr Eure Noten berechnen lassen!")

# Initialisiere die Liste 'noten', 'gewichtungen' und 'beschreibungen' in der Session State, falls sie noch nicht existiert
if 'noten' not in st.session_state:
    st.session_state.noten = []
if 'gewichtungen' not in st.session_state:
    st.session_state.gewichtungen = []
if 'beschreibungen' not in st.session_state:
    st.session_state.beschreibungen = []


# Seitenleiste für Eingabefelder
with st.sidebar:
    st.header("Noteneingabe")
    beschreibung = st.text_input("Fach:")
    note = st.number_input("Note:", min_value=1.0, max_value=6.0, step=0.25)
    gewichtung = st.number_input("Gewichtung:", min_value=1.0, max_value=10.0, step=1.0)
    add_note = st.button("Note hinzufügen")
    calculate = st.button("**Durchschnitt berechnen**")  

if add_note:
    st.session_state.beschreibungen.append(beschreibung)
    st.session_state.noten.append(note)
    st.session_state.gewichtungen.append(gewichtung)


# Funktion zum Löschen einer spezifischen Note, Gewichtung und Beschreibung
def delete_entry(index):
    del st.session_state.beschreibungen[index]
    del st.session_state.noten[index]
    del st.session_state.gewichtungen[index]

# Anzeigen der Noten, Gewichtungen und Beschreibungen mit Lösch-Schaltflächen
for i, (beschreibung, note, gewichtung) in enumerate(zip(st.session_state.beschreibungen, st.session_state.noten, st.session_state.gewichtungen)):
    st.markdown(f"<u>{beschreibung}({gewichtung}x):</u> **{note}**", unsafe_allow_html=True)
    if st.button(f"{i+1} . Note löschen", key=f"delete_{i}"):
        delete_entry(i)
        st.rerun()

if calculate:
    if st.session_state.noten and st.session_state.gewichtungen:
        total_weight = sum(st.session_state.gewichtungen)
        if total_weight == 0.0:
            st.error("Die Summe der Gewichtungen darf nicht 0 sein.")
        else:
            weighted_average = sum(n * g for n, g in zip(st.session_state.noten, st.session_state.gewichtungen)) / total_weight
            st.write(f"Notendurchschnitt:")
            if weighted_average < 4.0:
                st.markdown(f"<h1 style='color: red;'>{weighted_average:.2f} 😢</h1>", unsafe_allow_html=True)
            elif 4.0 <= weighted_average < 4.5:
                st.markdown(f"<h1 style='color: orange;'>{weighted_average:.2f} 😐</h1>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h1 style='color: green;'>{weighted_average:.2f} 😃</h1>", unsafe_allow_html=True)
 
    else:
        st.write("Keine Noten eingegeben.")

if st.button("Noten löschen"):
    st.session_state.beschreibungen = []
    st.session_state.noten = []
    st.session_state.gewichtungen = []
    st.rerun() 