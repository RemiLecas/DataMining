from functools import reduce
import pandas

#PART 1

# Q1
df = pandas.read_csv("book.csv")

print(df.head(5))

# Q2
df.info()

# Q3
to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(columns=to_drop)

print(df.head(5))

# Q4

df.set_index("Identifier")

# Q5

print(df["Date of Publication"].head(25))

# Q6

unwanted_characters = ['[', ',', '-']
# Completer la fonction suivante
def clean_dates(item):
    dop= str(item.loc['Date of Publication'])
    
    if dop == 'nan' or dop[0] == '[':
        return "NULL"
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]       
    
    return dop

df['Date of Publication'] = df.apply(clean_dates, axis = 1)

print(df["Date of Publication"].head(25))

# Q7 

def clean_author_names(author):
    
    author = str(author)
    
    if author == 'nan':
        return 'NaN'
    
    author = author.split(',')

    if len(author) == 1:
        name = filter(lambda x: x.isalpha(), author[0])
        return reduce(lambda x, y: x + y, name)
    
    last_name, first_name = author[0], author[1]

    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    
    if first_name.endswith(('.', '.|')):
        first_name = first_name[:-1]
        parts = first_name.strip().split()

        if len(parts) > 1:
            # Si plusieurs initiales/prénoms, conserver uniquement les initiales alphabétiques
            first_name = ' '.join(parts)
        else:
            # Si une seule initiale, la garder telle quelle (en supprimant les caractères spéciaux)
            first_name = ''.join(filter(lambda x: x.isalpha(), parts[0]))
    
    last_name = last_name.capitalize()
    
    return f'{first_name} {last_name}'


df['Author'] = df['Author'].apply(clean_author_names)

print(df["Author"].head(25))

# Q9

def clean_title(title):
    
    if title == 'nan':
        return 'NaN'
    
    if title[0] == '[':
        title = title.replace(title[0], "", 1)

    if 'by' in title:
        title = title[:title.find('by')]
    
    if 'By' in title:
        title = title[:title.find('By')]        
    
    if '[' in title:
        title = title[:title.find('[')]        

    while title.endswith(('.', ' ')):
        title = title[:-1]
        
    title = list(map(str.capitalize, title.split()))
    return ' '.join(title)
    
df['Title'] = df['Title'].apply(clean_title)
print(df['Title'].head())

# PART 2

# Q1-2

university_towns = []
with open('university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
             university_towns.append((state, line))

towns_df = pandas.DataFrame(university_towns, columns=['State', 'City'])
print(towns_df.head())

# Q3

def clean_up(item):
    if '(' in item:
        return item[:item.find('(') - 1]
    
    if '[' in item:
        return item[:item.find('[')]
    

towns_df = towns_df.map(clean_up)
print(towns_df)

# Part 3

# Q1-2
df = pandas.read_csv("olympics.csv", skiprows = 1, header = 0)

print(df.head(5))

# Q3

new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
              '03 !': 'Bronze',
              '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
              '03 !.1': 'Bronze.1',
              '? Games': '# Games', 
              '01 !.2': 'Gold.2',
              '02 !.2': 'Silver.2',
              '03 !.2': 'Bronze.2'}

df.rename(columns=new_names, inplace=True)

print(df.head())