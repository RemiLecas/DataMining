import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/Iris_flower_data_set"

tables = pd.read_html(url)

# Sélection du tableau contenant les données
df = tables[0]

# Affiche les colonnes
print(df.columns)

# Affiche (nb_lignes, nb_colonnes)
print(df.shape)  

# Supprimer la colonne "Dataset order"
df = df.iloc[:, 1:]

# Renommer les colonnes restantes
df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

# Vérifier le résultat
print(df.head())

colors = {"I. setosa": "red", "I. versicolor": "blue", "I. virginica": "green"}
for species, color in colors.items():
    subset = df[df["Species"] == species]
    plt.scatter(subset["Sepal Length"], subset["Sepal Width"], label=species, color=color)

plt.xlabel("Longueur des sépales")
plt.ylabel("Largeur des sépales")
plt.title("Relation entre la longueur et la largeur des sépales")
plt.legend()
plt.show()
