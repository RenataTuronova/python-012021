# program34 - Teplota ve městech popáté

# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.

import matplotlib.pyplot as plt
import pandas
temperature = pandas.read_csv("temperature.csv")

import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

specificCities = temperature[temperature["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]

ax = specificCities.boxplot(by="City", column="AvgTemperatureCelsia")
ax.set_ylabel("AvgTemperature (°C)")
ax.set_xlabel("City")
plt.show()
