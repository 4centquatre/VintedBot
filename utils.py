import streamlit as st
from vinted_scraper import VintedScraper
import libsql_client

def get_client():
    st.write(st.secrets["turso"]["url"])
    return libsql_client.create_client_sync(url=st.secrets["turso"]["url"], auth_token=st.secrets["turso"]["auth_token"],)

def init_db():
    client = get_client()
    client.execute("CREATE TABLE IF NOT EXISTS users \
                 (google_sub TEXT PRIMARY KEY, name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    client.execute("CREATE TABLE IF NOT EXISTS search_query \
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, google_sub TEXT REFERENCES users(google_sub), title TEXT, sizes TEXT, price_from TEXT, price_to TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    client.close()

def insert_user(google_sub, name):
    client = get_client()
    client.execute("INSERT INTO users (google_sub,name) VALUES (?,?) ON CONFLICT(google_sub) DO UPDATE SET name = excluded.name",[google_sub,name])
    client.close()

def insert_search(google_sub, title, sizes, price_from, price_to):
    client = get_client()
    client.execute("INSERT INTO search_query (google_sub, title, sizes, price_from, price_to) VALUES (?,?,?,?,?)", [google_sub, title, sizes, price_from, price_to])
    client.close()

def get_user_searches(google_sub):
    client = get_client()
    result = client.execute("SELECT id, title, sizes, price_from, price_to FROM search_query WHERE google_sub=?", [google_sub])
    data = [dict(zip(result.columns, row)) for row in result.rows]
    client.close()
    return data

def get_all_users():
    client = get_client()
    result = client.execute("SELECT google_sub FROM users")
    data = [dict(zip(result.columns, row)) for row in result.rows]
    client.close()
    return data

def delete_search(id_search):
    client = get_client()
    client.execute("DELETE FROM search_query WHERE id=?", [id_search])
    client.close()

def make_search(dico):
    scraper = VintedScraper("https://www.vinted.fr")
    items = scraper.search(dico)
    tab_items = []
    for i in range(40):
        tab_items.append(items[i])
    return tab_items

def get_tab_tailles():
    tab_sizes = []
    for i in range(38, 48):
        tab_sizes.append(i)
        tab_sizes.append(i+0.5)
    return tab_sizes

def transformer_tailles_choisies(tailles_choisies):
    dico_tailles = {}
    value = 776
    for i in range(38, 48):
        dico_tailles[str(i)] = str(value)
        dico_tailles[str(i + 0.5)] = str(value + 1)
        value += 2
    chaine = ""
    j = 0
    for i in range(len(tailles_choisies) - 1):
        chaine += dico_tailles[str(tailles_choisies[i])] + ","
        j += 1
    chaine += dico_tailles[str(tailles_choisies[j])]
    return chaine

def transformer_tab_to_chaine(tailles_choisies):
    chaine = ""
    j = 0
    for i in range(len(tailles_choisies) - 1):
        chaine += str(tailles_choisies[i]) + ","
        j += 1
    chaine += str(tailles_choisies[j])
    return chaine

def transformer_chaine_to_tab(chaine):
    return chaine.split(",")

def reduire_taille(chaine):
    tab = chaine.split(",")
    if len(tab) == 1:
        return tab[0]
    else:
        chaine_finie = f"{tab[0]} - {tab[-1]}"
        return chaine_finie