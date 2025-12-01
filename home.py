import streamlit as st
from google.cloud import discoveryengine_v1 as discoveryengine

PROJECT_ID = "restapi-444716"
LOCATION = "global"
DATA_STORE_ID = "recipe-data_1764590305776" 

def search_recipe(query_text):
    """Fungsi untuk menghubungi Vertex AI Search"""
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
st.write("Tanya resep apa saja (misal: 'Nasi Goreng', 'Sate'), AI akan mencarinya di BigQuery!")

query = st.text_input("Mau masak apa hari ini?")

if query:
    with st.spinner(f"Sedang mengaduk data untuk '{query}'..."):
        try:
            response = search_recipe(query)
            
            if not response.results:
                st.warning("Yah, resep tidak ditemukan di database. Coba menu lain ya!")
            else:
                st.success(f"Hore! Ditemukan {len(response.results)} resep.")
                
                for result in response.results:
                    data = result.document.derived_struct_data
                    
                    with st.expander(f"🍽️ {data.get('title', 'Tanpa Judul')}", expanded=True):
                        st.markdown(f"**Bahan-bahan:**\n{data.get('ingredients', '-')}")
                        st.divider()
                        st.markdown(f"**Cara Memasak:**\n{data.get('directions', '-')}")
                        
        except Exception as e:
            st.error(f"Ada error teknis: {e}")
            st.info("Tips: Pastikan API 'Discovery Engine' sudah aktif di Cloud Console.")

st.markdown("---")
st.caption("Dibuat dengan Google Vertex AI Search & Cloud Run")