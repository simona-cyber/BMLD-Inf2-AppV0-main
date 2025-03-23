# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

st.title('Notendurchschnitte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Notendurchschnitte vorhanden. Berechnen Sie Ihre Durchschnitte auf der Startseite.')
    st.stop()

# Debugging: Zeige den Inhalt des DataFrames an
st.write("DataFrame Inhalt:")
st.write(data_df)

# Überprüfe, ob die Spalte 'timestamp' im DataFrame vorhanden ist
if 'timestamp' not in data_df.columns:
    st.error("Die Spalte 'timestamp' ist im DataFrame nicht vorhanden.")
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)