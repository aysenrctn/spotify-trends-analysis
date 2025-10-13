# Import zipfile library to work with ZIP files
import zipfile

# Import pandas to read CSV data
import pandas as pd

# Path to the ZIP file
zip_path = 'archive.zip'

# Name of the CSV file inside the ZIP
csv_filename = 'Spotify most streamed.csv'

# Open the ZIP file and read the CSV inside
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Open the CSV file from inside the ZIP
    with zip_ref.open(csv_filename) as csv_file:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)
        print(df.head())  

# Read the CSV file directly from disk
df=pd.read_csv("Spotify most streamed.csv")
print(df.head(10))
