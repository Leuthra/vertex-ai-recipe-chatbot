# 🍳 AI Recipe Search Chatbot

Project ini adalah implementasi **RAG (Retrieval Augmented Generation)** menggunakan Google Cloud Platform.

## 🏗️ Arsitektur
1.  **Data Source:** BigQuery (Dataset resep).
2.  **Engine:** Vertex AI Agent Builder (Search App).
3.  **Frontend:** Streamlit (Python).
4.  **Deployment:** Google Cloud Run.

## 🚀 Cara Kerja
1.  Script `setup_bigquery.py` mengupload data dummy ke BigQuery.
2.  Vertex AI Search mengindeks data tersebut agar bisa dicari secara semantik.
3.  User bertanya via aplikasi chat, dan AI menjawab berdasarkan data resep yang valid.

## 🛠️ Tech Stack
* Python
* Google Cloud Platform (BigQuery, Vertex AI, Cloud Run)