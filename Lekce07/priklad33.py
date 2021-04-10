# program 33 - Velikonoce

# Ze souboru velikonoce.csv načti data o tom, kolikrát na který datum připadaly Velikonoce v letech 1600 až 2100.
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import matplotlib.pyplot as plt
import pandas

easter = pandas.read_csv("velikonoce.csv")
date = easter["Datum"]
easter = easter.set_index("Datum")
easter["Počet"].plot(kind="bar")
plt.show()

# Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
ax = easter["Počet"].plot(kind="bar", color="orange")
ax.set_xlabel("Date")
ax.set_ylabel("Number of years")
ax.set_title("Dates of Easter (years 1600 - 2100)")
plt.show()

# ROZŠÍŘENÉ ZADÁNÍ
# Vytvoř si datový soubor sama. Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem python-dateutil. Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost.

import matplotlib.pyplot as plt
import pandas
from dateutil import easter

dates = []
for year in range(1600, 2100):
  date = easter.easter(year)
  # Naformátuj datum jako řetězec tak, aby obsahovalo jen měsíc a den. Měsíc dej na začátek a za něj den - použij funkci strftime, kterou jsme spolu probírali
  easterDate = date.strftime("%m-%d")
  # Naformátovane datum ulož do seznamu data
  dates.append(easterDate)
# print(dates)

easterDates = pandas.DataFrame(dates, columns=["Datum"])
easterDates = easterDates.groupby("Datum").size()
ax2 = easterDates.plot(kind="bar", color="orange")
ax2.set_xlabel("Date")
ax2.set_ylabel("Number of years")
ax2.set_title("Dates of Easter (years 1600 - 2100)")
plt.show()
