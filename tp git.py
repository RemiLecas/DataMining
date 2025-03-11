import numpy as np
import pandas as pd
from functools import reduce

# Part 1
# 1 : Exploration du dataset
# URL du CSV
url = "https://raw.githubusercontent.com/nevermind78/DM/refs/heads/master/TP1/Datasets/BL-Flickr-Images-Book.csv"

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(url)

# Afficher les 5 premières lignes
# print(df.head())

# 2 : Jeter un coup d'oeil dans le dataset
# df.info()

# 3 : Qu'est ce que vous remarquez?
# On remarque qu'on obtient toutes les informations sur les données présentes
# dans le CSV avec le nom des colonnes et leurs type

# 4 : Dropping unnecessary columns
#to_drop = ['Edition Statement',
           #'Corporate Author',
           #'Corporate Contributors',
           #'Former owner',
           #'Engraver',
           #'Contributors',
           #'Issuance type',
           #'Shelfmarks']

#df.drop(columns=to_drop)

#print(df.head())


# 5 : Setting the index of the dataset

# Changer l'index avec la colonne 'Identifier'
# df.set_index("Identifier")

# Afficher le DataFrame après modification de l'index
# print(df.head())

# 6 : Donner un appérçu sur la colonne Date of Publication
# print(df["Date of Publication"].head(25))

# 7 : Cleaning columns using the .apply function
unwanted_characters = ['[', ',', '-']

#def clean_dates(item):
#    dop= str(item.loc['Date of Publication'])
    
#    if dop == 'nan' or dop[0] == '[':
#        pass
    
#    for character in unwanted_characters:
#        if character in dop:
#            pass
#            pass
    
#    return dop

#df['Date of Publication'] = df.apply(clean_dates, axis = 1)
#print(df.head())

# 8 : Observer la collone Author
def clean_author_names(author):
    """Nettoie les noms des auteurs en supprimant les caractères inutiles et en formatant correctement."""
    
    if pd.isna(author):  # Vérifie si la valeur est NaN
        return 'NaN'
    
    author = str(author).strip()  # Supprime les espaces inutiles
    
    # Séparer nom et prénom (ex: "Doe, John")
    parts = author.split(',')
    
    if len(parts) == 1:  # Cas où il n'y a pas de virgule (ex: "A. A.")
        return author.strip()
    
    # Extraction du nom et du prénom
    last_name = parts[0].strip()
    first_name = parts[1].strip()
    
    # Nettoyage des tirets dans les prénoms
    if '-' in first_name:
        first_name = first_name.split('-')[0].strip()
    
    # Supprimer les points après les initiales (ex: "A., A." → "A A")
    first_name = first_name.replace('.', '').strip()
    
    # Capitalisation correcte
    last_name = last_name.capitalize()
    first_name = first_name.capitalize()
    
    return f'{first_name} {last_name}'

# Appliquer la fonction sur la colonne "Author"
df['Author'] = df['Author'].apply(clean_author_names)

# Afficher les 10 premières lignes pour vérifier le nettoyage
df[['Author']].head(10)
