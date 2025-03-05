import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Albulena Ibishi (ibishalb@students.zhaw.ch)
- Simona Flachsmann (flachsim@students.zhaw.ch)

Diese App ist ein Notenrechner.
""" 


if st.button("Rechner"):
    st.switch_page("pages/Rechner.py")
