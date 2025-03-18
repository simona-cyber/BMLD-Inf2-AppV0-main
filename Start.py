import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title("Meine erste Streamlit App")

# Initialisierung des Data Managers (hier mit Verbindung zu SwitchDrive)
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Albumona")  

# Laden der Daten
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

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
