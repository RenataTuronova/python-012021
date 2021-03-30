# program 22 - Hra o trůny

# Pozn. Úkoly se týkají zcela nevýznamných postav, proto je riziko spoileru minimální :-)

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.
import pandas
gameOfThrones = pandas.read_csv("character-deaths.csv")
gameOfThrones = gameOfThrones.set_index("Name")

# Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
print(gameOfThrones.columns)

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
print(gameOfThrones.loc["Hali"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
print(gameOfThrones.loc["Gevin Harlaw":"Gillam"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
print(gameOfThrones.loc["Gevin Harlaw":"Gillam", "Death Year"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.
print(gameOfThrones.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])

