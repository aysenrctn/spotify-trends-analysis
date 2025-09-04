import zipfile
import pandas as pd

# ZIP dosyasının yolu
zip_path = 'archive.zip'

# ZIP içindeki CSV dosyasının adı
csv_filename = 'Spotify most streamed.csv'

# ZIP dosyasını aç ve CSV'yi oku
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    with zip_ref.open(csv_filename) as csv_file:
        df = pd.read_csv(csv_file)
        print(df.head())  