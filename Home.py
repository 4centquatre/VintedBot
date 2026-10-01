import streamlit as st
from utils import init_db

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info("""
                - Github Link : <https://github.com/4centquatre>
                """)  
if st.user.is_logged_in:
    st.sidebar.info(f"Logged in as {st.user.email}")

st.json(st.user)

init_db()

st.session_state.title = ""
st.session_state.tailles_choisies = []
st.session_state.prix_minimum = ""
st.session_state.prix_maximum = ""

st.title("Free Vinted Scraper",width="stretch", text_alignment="center")

if st.user.is_logged_in:
    st.subheader(f"Hi {st.user.given_name} !",width="stretch", text_alignment="center")

st.text("This is a free open source Vinted scraper. You can use it to search more efficiently articles on vinted",width="stretch", text_alignment="center")

options = {"Log In" : "pages/1_Login_Page.py", "Make a new search" : "pages/2_New_Vinted_Research.py", "See your favourite searches" : "pages/3_Favourites_Researches.py", "Catalog" : "pages/4_Catalog.py"}
result = st.pills("Make your choice", options, width="stretch")
if result is not None:
    st.switch_page(options[result])


