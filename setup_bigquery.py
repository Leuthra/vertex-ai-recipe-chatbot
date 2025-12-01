import pandas as pd
from google.cloud import bigquery

project_id = 'restapi-444716'
dataset_id = 'recipe_data'
table_id = 'recipes'

data = [
    {"title": "Nasi Goreng Spesial", "ingredients": "Nasi putih, 2 butir telur, kecap manis, bawang merah, bawang putih, garam", "directions": "Tumis bumbu halus hingga harum. Masukkan telur, orak-arik. Masukkan nasi, aduk rata dengan kecap dan garam."},
    {"title": "Sate Ayam Madura", "ingredients": "Daging ayam fillet, kacang tanah goreng, kecap manis, cabai rawit, jeruk nipis", "directions": "Potong ayam kotak-kotak, tusuk sate. Bakar hingga matang. Haluskan kacang, campur kecap dan air untuk bumbu."},
    {"title": "Gado-Gado Jakarta", "ingredients": "Tahu, tempe, bayam, tauge, kacang panjang, kerupuk, bumbu kacang instan", "directions": "Rebus semua sayuran. Goreng tahu dan tempe. Campur semua dengan bumbu kacang yang sudah diseduh air hangat."}
]

df = pd.DataFrame(data)

print("Sedang memproses ke BigQuery...")

client = bigquery.Client(project=project_id)
dataset_ref = client.dataset(dataset_id)

try:
    client.get_dataset(dataset_ref)
    print(f"Dataset '{dataset_id}' sudah ada, lanjut upload...")
except:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"
    client.create_dataset(dataset)
    print(f"Dataset '{dataset_id}' berhasil dibuat!")

table_ref = f"{project_id}.{dataset_id}.{table_id}"
df.to_gbq(table_ref, project_id=project_id, if_exists='replace')

print("SUKSES! Data sudah masuk BigQuery.")