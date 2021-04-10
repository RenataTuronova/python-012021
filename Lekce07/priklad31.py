# program 31 - Histogram platy

# Stáhni si znovu soubor platy_2021_02.csv s informacemi o platech v softwarové firmě, se kterými jsme již pracovali v příkladu 26.
# Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import matplotlib.pyplot as plt

import pandas
salary = pandas.read_csv("platy_2021_02.csv")
# print(salary.head())

salary["plat"].hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
plt.xlabel("CZK")
plt.title("Plat zaměstnanců softwarové firmy")
plt.show()

# DOBROVOLNÝ DOPLNĚK
# Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist(). Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.
# Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci pracují (to jsme již dělali v příkladu) příkladu 26. Následně sloupec mesto použij na rozdělení podgrafů.

employeesAndSalary = pandas.read_csv("employeesAndSalary.csv")
salary1 = employeesAndSalary["plat"]
city = employeesAndSalary["mesto"]
salary1.hist(by=city, bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
plt.show()


