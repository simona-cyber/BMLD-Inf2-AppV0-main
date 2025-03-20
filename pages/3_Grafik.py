# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === Notendurchschnitte Grafik ===
import streamlit as st

st.title('Notendurchschnitte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Notendurchschnitte vorhanden. Berechnen Sie Ihre Durchschnitte auf der Startseite.')
    st.stop()


# Notendurchschnitte
st.line_chart(data=data_df.set_index('beschreibung')['weighted_average'], use_container_width=True)
st.caption('Noten')