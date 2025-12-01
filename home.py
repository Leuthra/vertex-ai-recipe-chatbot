import streamlit as st

st.title("🤖 Chef Bot - Vertex AI Search")
st.write("Tanya resep apa saja, AI akan mencarikannya dari BigQuery!")

query = st.text_input("Mau masak apa hari ini?")

if query:
    st.info(f"Mencari resep untuk: {query}...")