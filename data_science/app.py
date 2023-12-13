import streamlit as st
from data_science import clustering, exploration


def app():
    page = st.sidebar.radio("Page", [clustering.title, exploration.title])
    if page == clustering.title:
        clustering.app()
    elif page == exploration.title:
        exploration.app()



if __name__ == "__main__":
    app()
