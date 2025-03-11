import pandas as pd

# URL du CSV
url = "https://raw.githubusercontent.com/nevermind78/DM/refs/heads/master/TP1/Datasets/BL-Flickr-Images-Book.csv"

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(url)

# Afficher les 5 premières lignes
print(df.head())
