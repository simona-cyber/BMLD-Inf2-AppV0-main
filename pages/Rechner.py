import streamlit as st

st.title("Notenrechner")

st.write("Mit diesem Rechner könnt ihr Eure Noten berechnen lassen!")

# Initialisiere die Liste 'noten' in der Session State, falls sie noch nicht existiert
if 'noten' not in st.session_state:
    st.session_state.noten = []
if 'gewichtungen' not in st.session_state:
    st.session_state.gewichtungen = []

with st.form("grade_form"):
    note = st.number_input("Geben Sie Ihre Note ein:", min_value=1.0, max_value=6.0, step=0.25)
    gewichtung = st.number_input("Geben Sie die Gewichtung der Note ein:", min_value=1.0, max_value=10.0, step=1.0)
    add_note = st.form_submit_button("Note hinzufügen")
    calculate = st.form_submit_button("Durchschnitt berechnen")

if add_note:
    st.session_state.noten.append(note)
    st.session_state.gewichtungen.append(gewichtung)
    st.write(f"Noten: {st.session_state.noten}")
    st.write(f"Gewichtungen: {st.session_state.gewichtungen}")

# Funktion zum Löschen einer spezifischen Note und Gewichtung
def delete_entry(index):
    del st.session_state.noten[index]
    del st.session_state.gewichtungen[index]

# Anzeigen der Noten und Gewichtungen mit Lösch-Schaltflächen
for i, (note, gewichtung) in enumerate(zip(st.session_state.noten, st.session_state.gewichtungen)):
    st.write(f"Note {i+1}: {note}, Gewichtung: {gewichtung}")
    if st.button(f"{i+1}. Note löschen", key=f"delete_{i}"):
        delete_entry(i)
        st.experimental_rerun()

if calculate:
    if st.session_state.noten and st.session_state.gewichtungen:
        total_weight = sum(st.session_state.gewichtungen)
        if total_weight == 0.0:
            st.error("Die Summe der Gewichtungen darf nicht 0 sein.")
        else:
            weighted_average = sum(n * g for n, g in zip(st.session_state.noten, st.session_state.gewichtungen)) / total_weight
            st.write(f"Gewichteter Durchschnitt: {weighted_average:.2f}")
            if weighted_average < 4.0:
                st.markdown(f"<h1 style='color: red;'>{weighted_average:.2f}</h1>", unsafe_allow_html=True)
            elif 4.0 <= weighted_average < 4.5:
                st.markdown(f"<h1 style='color: orange;'>{weighted_average:.2f}</h1>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h1 style='color: green;'>{weighted_average:.2f}</h1>", unsafe_allow_html=True)
    else:
        st.write("Keine Noten eingegeben.")

if st.button("Noten löschen"):
    st.session_state.noten = []
    st.session_state.gewichtungen = []
    st.rerun() 