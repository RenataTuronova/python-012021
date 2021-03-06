# import wget
# wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

# # Wget slouzi ke stazeni dat z internetu
# import wget
# wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

# pandas vyuzivam, kdyz chci data jakoukoli praci s datama - vycistit, zjistit nejakou informaci, zpracovat data a ziskat z nich neco...
# sel by vyuzit i v ukolech z lekce 2, napriklad v praci se staty

import pandas
nakupy = pandas.read_csv('nakupy.csv')
print(nakupy)


nakupy.info()

# vypis radku
print(nakupy.shape)

# pokud chceme pocet radku  - zajima nas pozice 0, pokud pocet sloupcu - pozice 1
print(nakupy.shape[0])

# vypis sloupcu
print(nakupy.columns)

# funkce iloc[] - vyberu si konkretni radek nakupu, v tomto pripade 4 radek
print(nakupy.iloc[3])

#vsechny radky
print(nakupy.iloc[:])

#  vyberu rozmezi radku, ktere chci vypsat ... tady je to 1 - 6 radek
print(nakupy.iloc[0:5])

# vyberu prvnich nebo poslednich nekolik radku
print(nakupy.iloc[:3]) # budou zde radky 0, 1, 2
print(nakupy.iloc[8:]) # pokud vime kolik mame celkove radku a chceme vypsat od 8 radku
print(nakupy.iloc[-3:]) # pokud nevime kolik mame celkove radku, znaku, vyuzijeme cislo s minusem a odpocita se to od konce

pozdrav = "Ahoj Aleno"
print(pozdrav[-5:]) # vybere nam to 5 poslednich znaku

#pokud mame problem s mezerami, napr. neukazneni zakaznici:
pozdrav = " Ahoj Aleno "
print(pozdrav.strip()) # odebere nam to mezery pred a za
print(pozdrav.strip().replace("  ", " ")) # replace nahradi mezeru o dvou mezernicich za jeden mezernik

#krome iloc jde pouzit i head a tail, do zavorky budto jen cislo nebo n=cislo, je to jedno
print(nakupy.head(5)) # vrchni, pocatecni radky, pismena
print(nakupy.tail(n=3)) # koncove radky, pismena

# pokud potrebujeme prvnich nekolik radku a vyselektovat nej nektery sloupec nebo nektere sloupce
# prvni cislo je pocet radku, druhe sloupce. Pokud chceme vice sloupcu udelame to jako jejich seznam []
print(nakupy.iloc[:5, 0])
print(nakupy.iloc[:5, [0, 3])
print(nakupy.head(n=3))

# vsechny radky a vyselektovane sloupce
print(nakupy.iloc[:, [0, 3])

# terminologie Pandas, jsou zde 2 datove typy v Pandas:
#  - serie = serie - jednorozmerna
#  - dataframe = tabulka - dvourozmerna



## moduly:
## pro Excel: openpyxl
## pro odeslani requestu: suds

#### api je zjednodusene v cisnik v restauraci, ktery zaridi komunikaci s backendem, coz je kuchyne.
#### je system, ty potrebujes nejaky pozadavek, api zaridi komunikacni rozhrani se sluzby.

###  druhy učení včetně ML jsem prošla https://www.freecodecamp.org/learn


# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")

# 1
import pandas
jobs = pandas.read_csv("DataAnalyst.csv")

# 2
print(jobs.columns)
# lze tady treba vyuzit i funkci len

print(jobs.iloc[0])

## 3
print(jobs.shape)
# print(jobs.info()) - ukazuje vice informaci o jednotlivych columns ... jako datovy object, kolik je tam nenulovych hodnot..

## 4 musime si uvedomit, ze to cisluje od 0, proto 10 radek = [9]
# napr. kdyz si vypisu prvnich 25 radku = print(jobs.head[25]), tak vidim, ze to cisluje od 0.
print(jobs.iloc[9])  # vrati mi to series
# lze to i dale  indexovat, kdyz chceme treba jen job description:
print(jobs.iloc[9]["Job Description"])

## 5
print(jobs.loc[11:21, "Job Title"])
# lze to pouzit i takto, pomoci pridani zaindexovani
print(jobs.loc[11:21]["Job Title"])