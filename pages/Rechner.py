import streamlit as st

st.title("Notenrechner")

st.write("Mit diesem Rechner könnt ihr Eure Noten berechnen lassen!")

# Initialisiere die Liste 'noten' in der Session State, falls sie noch nicht existiert
if 'noten' not in st.session_state:
    st.session_state.noten = []

with st.form("grade_form"):
    note = st.number_input("Geben Sie Ihre Note ein:", min_value=1.0, max_value=6.0, step=0.01)
    add_note = st.form_submit_button("Note hinzufügen")
    calculate = st.form_submit_button("Durchschnitt berechnen")

if add_note:
    st.session_state.noten.append(note)
    st.write(f"Noten: {st.session_state.noten}")

if calculate:
    if st.session_state.noten:
        durchschnitt = sum(st.session_state.noten) / len(st.session_state.noten)
        st.write(f"Durchschnitt: {durchschnitt:.2f}")
        if durchschnitt < 4.0:
            st.markdown(f"<h1 style='color: red;'>{durchschnitt:.2f}</h1>", unsafe_allow_html=True)
        elif 4.0 <= durchschnitt < 4.5:
            st.markdown(f"<h1 style='color: orange;'>{durchschnitt:.2f}</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='color: green;'>{durchschnitt:.2f}</h1>", unsafe_allow_html=True)
    else:
        st.write("Keine Noten eingegeben.")

if st.button("Noten löschen"):
    st.session_state.noten = []
    st.rerun()