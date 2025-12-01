import streamlit as st
from google.cloud import discoveryengine_v1 as discoveryengine

PROJECT_ID = "restapi-444716"
LOCATION = "global"
DATA_STORE_ID = "recipe-data_1764590305776" 

def search_recipe(query_text):
    client = discoveryengine.SearchServiceClient()
    serving_config = client.serving_config_path(
        project=PROJECT_ID,
        location=LOCATION,
        data_store=DATA_STORE_ID,
        serving_config="default_config",
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=query_text,
        page_size=5,
    )
    return client.search(request)

st.set_page_config(page_title="Chef Bot AI", page_icon="🍳")
st.title("🍳 Chef Bot - Asisten Resep")

query = st.text_input("Mau masak apa hari ini?")

if query:
    with st.spinner(f"Sedang mencari '{query}'..."):
        try:
            response = search_recipe(query)
            
            if not response.results:
                st.warning("Resep tidak ditemukan.")
            else:
                st.success(f"Hore! Ditemukan {len(response.results)} resep.")
                
                for result in response.results:
                    data = result.document.struct_data
                    
                    data_dict = {}
                    for key, value in data.items():
                        data_dict[key] = value

                    title = data_dict.get('title', 'Tanpa Judul')
                    ingredients = data_dict.get('ingredients', 'Data bahan tidak terbaca')
                    directions = data_dict.get('directions', 'Data cara masak tidak terbaca')

                    with st.expander(f"🍽️ {title}", expanded=True):
                        st.markdown(f"**Bahan-bahan:**\n{ingredients}")
                        st.divider()
                        st.markdown(f"**Cara Memasak:**\n{directions}")

        except Exception as e:
            st.error(f"Error: {e}")