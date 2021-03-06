
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")

import pandas
jmena = pandas.read_csv("jmena.csv")
# pokud bych si sloupce chtela prejmenovat, treba proto ze mi vadi hacky a carky, muzu takto:
# jmena = jmena.rename(columns={
#       "jméno":"jmeno",
#       "četnost":"cetnost",
#       "věk":"vek",
#       "pohlaví":"pohlavi",
#       "svátek":"svatek",
#       "původ":"puvod",
# })
jmena = jmena.set_index("jméno")

# # 1
print(jmena.loc["Jiří"])

# # 2
print(jmena.loc[["Martin", "Zuzana", "Josef"]])

# # 3
print(jmena.loc[:"Renata"])

# pozn. pokud bych si chtela jmena seradit jinak, muzu takto:
jmena = jmena.sort_index()
# pokud si chci seradit podle nejakeho sloupce:
jmena = jmena.sort_values(by="četnost")
# automaticky to radi od nejmensiho po nejvetsi, proto pokud chci opacne:
jmena = jmena.sort_values(by="četnost", ascending=False)

# # 4 kdyz chceme rozmezi, nedavame pridatne zavorky, vse je v jedne zavorce. Kdyz chceme konkretni jmena, pridavame zavorky
print(jmena.loc["Martin":"Tereza", "věk"])

# # 5
print(jmena.loc["Libor":, ["věk", "původ"]])

# # 6
print(jmena[jmena[:, "věk":"původ"])
# nebo muzeme sloupecky vypsat pomoci cisel. iloc bere jen to mezi, nebere ty krajni hodnoty
print(jmena.iloc[:, 2:-1])



