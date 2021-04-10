# program 30(lekce7) - Řazení

# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.

import pandas
temperature = pandas.read_csv("temperature.csv")

import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

# Vyfiltruj si informace o teplotách 13. listopadu 2017.
november13 = temperature[temperature["Day"] == 13]
print(november13)

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
correctTemperature = november13[november13["AvgTemperature"] != -99]
print(correctTemperature)

# Seřad hodnoty v souboru podle teploty od největší po nejmenší.
sortedByTemperature = correctTemperature.sort_values(by="AvgTemperatureCelsia", ascending=False)
print(sortedByTemperature)

# Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
maxTemperature = sortedByTemperature.head(5)
print(maxTemperature[["City", "AvgTemperatureCelsia"]])

minTemperature = sortedByTemperature.tail(5)
sortedMinTemperature = minTemperature.sort_values(by="AvgTemperatureCelsia")
print(sortedMinTemperature[["City", "AvgTemperatureCelsia"]])