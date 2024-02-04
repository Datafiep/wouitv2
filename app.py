import streamlit as st
from Welcome import welcome_page
from Futures import futures_page

# Créez une barre de navigation pour basculer entre les pages
page = st.sidebar.selectbox("Choose a page", ["Welcome", "Futures"])

if page == "Welcome":
    welcome_page()
elif page == "Futures":
    futures_page()
