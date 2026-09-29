import streamlit as st
from utils import get_user_searches, transformer_chaine_to_tab, delete_search, reduire_taille

st.session_state.title = ""
st.session_state.tailles_choisies = []
st.session_state.prix_minimum = ""
st.session_state.prix_maximum = ""

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info("""
                - Github Link : <https://github.com/4centquatre>
                """)  
if st.user.is_logged_in:
    st.sidebar.info(f"Logged in as {st.user.email}")

st.title("Your favourites Vinted researches", text_alignment="center", width="stretch")

if st.user.is_logged_in:
    tab_searches = get_user_searches(st.user.sub)

    for i in range(0, len(tab_searches), 4):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            search = tab_searches[i]
            with st.container(height=350, width="stretch", horizontal_alignment="center", vertical_alignment="center"):
                id_search, title, sizes, price_from, price_to = search 
                st.session_state.title = title
                st.session_state.prix_minimum = price_from
                st.session_state.prix_maximum = price_to
                st.session_state.tailles_choisies = transformer_chaine_to_tab(sizes)
                st.markdown(f"##### {title}",text_alignment="center", width="stretch")
                if price_from == "":
                    price_from = "0"
                st.markdown(f"##### {price_from} - {price_to}",text_alignment="center", width="stretch")
                st.markdown(f"##### {reduire_taille(sizes)}",text_alignment="center", width="stretch")
                if st.button("Start", key=str(i + 1000),width="stretch"):
                    st.switch_page("pages/4_Catalog.py")
                if st.button("Delete", key=str(i),width="stretch"):
                    delete_search(id_search)
                    st.rerun()
                        
        if i + 1 < len(tab_searches):
            with col2:
                search = tab_searches[i+1]
                with st.container(height=350, width="stretch", horizontal_alignment="center", vertical_alignment="center"):
                    id_search, title, sizes, price_from, price_to = search 
                    st.session_state.title = title
                    st.session_state.prix_minimum = price_from
                    st.session_state.prix_maximum = price_to
                    st.session_state.tailles_choisies = transformer_chaine_to_tab(sizes)
                    st.markdown(f"##### {title}",text_alignment="center", width="stretch")
                    if price_from == "":
                        price_from = "0"
                    st.markdown(f"##### {price_from} - {price_to}",text_alignment="center", width="stretch")
                    st.markdown(f"##### {reduire_taille(sizes)}",text_alignment="center", width="stretch")
                    if st.button("Start", key=str(i + 1001), width="stretch"):
                        st.switch_page("pages/4_Catalog.py")
                    if st.button("Delete", key=str(i+1), width="stretch"):
                        delete_search(id_search)
                        st.rerun()
        
        if i + 2 < len(tab_searches):
            with col3:
                search = tab_searches[i+2]
                with st.container(height=350, width="stretch", horizontal_alignment="center", vertical_alignment="center"):
                    id_search, title, sizes, price_from, price_to = search 
                    st.session_state.title = title
                    st.session_state.prix_minimum = price_from
                    st.session_state.prix_maximum = price_to
                    st.session_state.tailles_choisies = transformer_chaine_to_tab(sizes)
                    st.markdown(f"##### {title}",text_alignment="center", width="stretch")
                    if price_from == "":
                        price_from = "0"
                    st.markdown(f"##### {price_from} - {price_to}",text_alignment="center", width="stretch")
                    st.markdown(f"##### {reduire_taille(sizes)}",text_alignment="center", width="stretch")
                    if st.button("Start", key=str(i + 1002), width="stretch"):
                        st.switch_page("pages/4_Catalog.py")
                    if st.button("Delete", key=str(i+2), width="stretch"):
                        delete_search(id_search)
                        st.rerun()
                            
        if i + 3 < len(tab_searches):
            with col4:
                search = tab_searches[i+3]
                with st.container(height=350, width="stretch", horizontal_alignment="center", vertical_alignment="center"):
                    id_search, title, sizes, price_from, price_to = search 
                    st.session_state.title = title
                    st.session_state.prix_minimum = price_from
                    st.session_state.prix_maximum = price_to
                    st.session_state.tailles_choisies = transformer_chaine_to_tab(sizes)
                    st.markdown(f"##### {title}",text_alignment="center", width="stretch")
                    if price_from == "":
                        price_from = "0"
                    st.markdown(f"##### {price_from} - {price_to}",text_alignment="center", width="stretch")
                    st.markdown(f"##### {reduire_taille(sizes)}",text_alignment="center", width="stretch")
                    if st.button("Start", key=str(i+1003), width="stretch"):
                        st.switch_page("pages/4_Catalog.py")
                    if st.button("Delete", key=str(i+3), width="stretch"):
                        delete_search(id_search)
                        st.rerun()
                            
else:
    st.warning("Please Log In")
    st.page_link("pages/1_Login_Page.py", label="Login Page")