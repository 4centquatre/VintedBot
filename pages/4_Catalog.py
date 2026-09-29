import streamlit as st
from utils import make_search, transformer_tailles_choisies, transformer_tab_to_chaine, reduire_taille
import time

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

st.title("Shoes Catalog", text_alignment="center", width="stretch")

st.session_state.stop = False
st.session_state.tab_articles = []
st.session_state.step = ""

if "title" not in st.session_state:
    st.session_state.title = ""

if st.session_state.title == "":
    st.warning("No researches has been saved.")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col3:
        if st.button("Make a new search", width="stretch"):
            st.switch_page("pages/2_New_Vinted_Research.py")
    with col4:
        if st.button("Start a saved search", width="stretch"):
            st.switch_page("pages/3_Favourites_Researches.py")

else:
    if st.session_state.tailles_choisies == []:
        for i in range(38, 48):
            st.session_state.tailles_choisies.append(str(i))
            st.session_state.tailles_choisies.append(str(i + 0.5))

    if st.session_state.prix_minimum == "":
        st.session_state.prix_minimum = "0"

    with st.form("Your saved search"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<p style='font-size: 14px; margin-bottom: 4px;'>Title</p>", unsafe_allow_html=True)
        with col2:
            st.markdown("<p style='font-size: 14px; margin-bottom: 4px;'>Price</p>", unsafe_allow_html=True)
        with col3:
            st.markdown("<p style='font-size: 14px; margin-bottom: 4px;'>Sizes</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3, vertical_alignment="center", border=True, width="stretch")
        with col1:
            st.markdown(f"##### {st.session_state.title}",text_alignment="center", width="stretch")
        with col2:
            st.markdown(f"##### {st.session_state.prix_minimum} - {st.session_state.prix_maximum}", text_alignment="center", width="stretch")
        with col3:
            chaine = transformer_tab_to_chaine(st.session_state.tailles_choisies)
            st.markdown(f"##### {reduire_taille(chaine)}", text_alignment="center", width="stretch")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        if st.button("Stop", width="stretch"):
            st.session_state.stop = True

    @st.fragment(run_every=30)
    def show_results():
        if st.session_state.stop:
            return

        tab_results = make_search({"search_text" : st.session_state.title, "price_from" : st.session_state.prix_minimum, "price_to" : st.session_state.prix_maximum, "order" : "newest_first", "attribute_ids[size]" : transformer_tailles_choisies(st.session_state.tailles_choisies)})

        ids_existants = {item.id for item in st.session_state.tab_articles}
        nouveaux = [item for item in tab_results if item.id not in ids_existants]

        st.session_state.tab_articles = nouveaux + st.session_state.tab_articles

        for i in range(0, len(st.session_state.tab_articles), 4):
            col1, col2, col3, col4 = st.columns(4, border=True)
            with col1:
                item = st.session_state.tab_articles[i]
                st.image(item.photo["url"], caption=item.description, width="stretch")
                st.markdown(item.title, text_alignment="center", width="stretch")
                st.markdown(f"{item.price}€", text_alignment="center", width="stretch")
                st.link_button("Voir l'annonce", "https://www.vinted.com" + item.url,width="stretch")
            time.sleep(0.2)

            if i + 1 < len(st.session_state.tab_articles):
                with col2:
                    item = st.session_state.tab_articles[i + 1]
                    st.image(item.photo["url"], caption=item.description, width="stretch")
                    st.markdown(item.title, text_alignment="center", width="stretch")
                    st.markdown(f"{item.price}€", text_alignment="center", width="stretch")
                    st.link_button("Voir l'annonce", "https://www.vinted.com" + item.url, width="stretch")
                time.sleep(0.2)

            if i + 2 < len(st.session_state.tab_articles):
                with col3:
                    item = st.session_state.tab_articles[i + 2]
                    st.image(item.photo["url"], caption=item.description, width="stretch")
                    st.markdown(item.title, text_alignment="center", width="stretch")
                    st.markdown(f"{item.price}€", text_alignment="center", width="stretch")
                    st.link_button("Voir l'annonce", "https://www.vinted.com" + item.url, width="stretch")
                time.sleep(0.2)

            if i + 3 < len(st.session_state.tab_articles):
                with col4:
                    item = st.session_state.tab_articles[i + 3]
                    st.image(item.photo["url"], caption=item.description, width="stretch")
                    st.markdown(item.title, text_alignment="center", width="stretch")
                    st.markdown(f"{item.price}€", text_alignment="center", width="stretch")
                    st.link_button("Voir l'annonce", "https://www.vinted.com" + item.url, width="stretch")
                time.sleep(0.2)

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        if st.button("Start", width="stretch"):
            st.session_state.step = "Start"

if st.session_state.step == "Start":
    show_results()