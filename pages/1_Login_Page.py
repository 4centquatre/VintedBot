import streamlit as st
from utils import insert_user

st.title("Log In", text_alignment="center", width="stretch")

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info("""
                - Github Link : <https://github.com/4centquatre>
                """)
if st.user.is_logged_in:
    st.sidebar.info(f"Logged in as {st.user.email}")

st.session_state.title = ""
st.session_state.tailles_choisies = []
st.session_state.prix_minimum = ""
st.session_state.prix_maximum = ""

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if st.button("Authenticate", width="stretch"):
        st.login("google")

if st.user.is_logged_in:
    insert_user(st.user.sub, st.user.name)

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if st.button("Log Out", width="stretch"):
        st.logout()