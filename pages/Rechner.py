from datetime import datetime
# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

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

def calculate_average():
    """
    Calculate the weighted average and return a dictionary with inputs, weighted average, category, and timestamp.

    Returns:
        dict: A dictionary containing the inputs, calculated weighted average, category, and timestamp.
    """
    if not st.session_state.noten or not st.session_state.gewichtungen:
        raise ValueError("Es müssen Noten und Gewichtungen eingegeben werden.")

    total_weight = sum(st.session_state.gewichtungen)
    if total_weight == 0:
        raise ValueError("Die Summe der Gewichtungen darf nicht 0 sein.")

    weighted_average = sum(n * g for n, g in zip(st.session_state.noten, st.session_state.gewichtungen)) / total_weight

    if weighted_average < 4.0:
        category = 'Nicht bestanden'
    elif 4.0 <= weighted_average < 4.5:
        category = 'Bestanden'
    else:
        category = 'Gut bestanden'

    result_dict = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "noten": st.session_state.noten,
        "gewichtungen": st.session_state.gewichtungen,
        "beschreibungen": st.session_state.beschreibungen,
        "weighted_average": round(weighted_average, 2),
        "category": category,
    }

    return result_dict

if calculate:
    try:
        result = calculate_average()
        st.write(f"Notendurchschnitt: {result['weighted_average']}")
        st.write(f"Kategorie: {result['category']}")
        st.write(f"Zeitstempel: {result['timestamp']}")
        if result['weighted_average'] < 4.0:
            st.markdown(f"<h1 style='color: red;'>{result['weighted_average']} 😢</h1>", unsafe_allow_html=True)
        elif 4.0 <= result['weighted_average'] < 4.5:
            st.markdown(f"<h1 style='color: orange;'>{result['weighted_average']} 😐</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='color: green;'>{result['weighted_average']} 😃</h1>", unsafe_allow_html=True)
    except ValueError as e:
        st.error(str(e))

if st.button("Noten löschen"):
    st.session_state.beschreibungen = []
    st.session_state.noten = []
    st.session_state.gewichtungen = []
    st.rerun()

    # Speichern des neuen Eintrags
    DataManager().append_record(session_state_key='data_df', record_dict=result)