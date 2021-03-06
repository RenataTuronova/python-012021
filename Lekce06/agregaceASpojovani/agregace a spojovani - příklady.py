# agregace = seskupeni

# import wget
#
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')
#

import pandas
# jmena = pandas.read_csv("jmena.csv")
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")

# 1. Načtěte dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce concat je spojte do jednoho setu.
studenti = pandas.concat([studenti1, studenti2])

# 2. Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
chyba1 = studenti[studenti["ročník"].isnull()]
print(f"Chybi rocnik, nestuduje: {chyba1}")
print(len(chyba1))
chyba2 = studenti[studenti["kruh"].isnull()]
print(f"Dalkovy student: {chyba2}")
print(len(chyba2))
# 3. Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze s prezenčními studenty.
studenti = studenti.dropna()

# 4. Zjistěte, kolik prezenčních studentů je v každém z oborů.
obor = studenti.groupby("obor").count()
print(obor)

# 5. Zjistěte průměrný prospěch studentů v každém oboru.
prospech = studenti.groupby("obor")["prospěch"].mean()
print(prospech)

# 6. Načtěte datový set s křestními jmény. Proveďte join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.
jmena = pandas.read_csv("jmena.csv").dropna()
propojeni = pandas.merge(jmena, student)
pohlavi = propojeni.groupby("pohlaví").count
print(pohlavi)

# 7. Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.
if int(pohlavi["jmeno"][0]) > int(pohlavi["jmeno"][1]]):
  print("muzi")
else:
  print("zeny")





