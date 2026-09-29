from utils import get_tab_tailles, insert_search, transformer_tab_to_chaine, insert_user
import streamlit as st
import time

st.session_state.title = ""
st.session_state.tailles_choisies = []
st.session_state.prix_minimum = ""
st.session_state.prix_maximum = ""


insert_user(st.user.sub, st.user.name)

st.markdown("""
<style>
[data-testid="stImage"] img {
    height: 350px;
    object-fit: cover;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info("""
                - Github Link : <https://github.com/4centquatre>
                """)  
if st.user.is_logged_in:
    st.sidebar.info(f"Logged in as {st.user.email}")

st.title("Make a new Vinted research", text_alignment="center", width="stretch")

st.info("You first have to save a search to start it.")

st.session_state.tailles_choisies = []

with st.form("Enter a new research"):
    col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="bottom")
    with col1:
        st.markdown("<p style='font-size: 14px; margin-bottom: 4px;'>Category</p>", unsafe_allow_html=True)
        with st.popover("", width="stretch"):
            st.session_state.categories = []
            for category in ["Shoes", "T-Shirt", "Sweatshirt", "Trousers"]:
                with st.popover(category, width="stretch"):
                    for genre in ["Men", "Women"]:
                        if st.checkbox(genre, key=f"{category}_{genre}"):
                            st.session_state.categories.append(category + genre)
    with col2:
        title = st.text_input("Title")
        st.session_state.title = title
    with col3:
        st.markdown("<p style='font-size: 14px; margin-bottom: 4px;'>Sizes</p>", unsafe_allow_html=True)
        with st.popover("", width="stretch"):
            st.session_state.tailles_choisies = []
            for taille in get_tab_tailles():
                if st.checkbox(taille, key=f"size_{taille}"):
                    st.session_state.tailles_choisies.append(taille)
    with col4:
        st.session_state.prix_minimum = st.text_input("Minimum Price")
    with col5:
        st.session_state.prix_maximum = st.text_input("Maximum Price")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        validee = st.form_submit_button("Save", width="stretch")

    if validee:
        if not st.user.is_logged_in:
            st.warning("Please Log In")
        elif st.session_state.title == "":
            st.warning("Your research need to have at least a title !")
        else:
            if st.session_state.tailles_choisies == []:
                for i in range(38, 48):
                    st.session_state.tailles_choisies.append(str(i))
                    st.session_state.tailles_choisies.append(str(i + 0.5))
            chaine = transformer_tab_to_chaine(st.session_state.tailles_choisies)
            insert_search(st.user.sub, st.session_state.title, chaine, st.session_state.prix_minimum, st.session_state.prix_maximum)
            st.info("Your research has been succesfully saved !")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col4:
    if st.button("Start", width="stretch"):
        st.switch_page("pages/4_Catalog.py")

