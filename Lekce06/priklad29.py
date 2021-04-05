# program29 - Teplota ve městech potřetí

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
correctValues = november13[november13["AvgTemperature"] != -99]
print(correctValues)

# # Výpočty se všemi záznamy (november13):
# Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
dataByRegion = november13.groupby("Region").count()
print(dataByRegion)

# Vypočti průměrnou teplotu za jednotlivé regiony.
avgTemperatureByRegion = november13.groupby("Region")["AvgTemperatureCelsia"].mean()
print(avgTemperatureByRegion)

# Vypočti maximální a minimální teplotu v každém regionu.
extremeValuesByRegion = november13.groupby("Region").agg({"AvgTemperatureCelsia": ["max", "min"]})
print(extremeValuesByRegion)

# # Výpočty se záznamy po odstranění chybných hodnot (correctValues):
# Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
dataByRegion1 = correctValues.groupby("Region").count()
print(dataByRegion1)
# Vypočti průměrnou teplotu za jednotlivé regiony.
avgTemperatureByRegion1 = correctValues.groupby("Region")["AvgTemperatureCelsia"].mean()
print(avgTemperatureByRegion1)
# Vypočti průměrnou teplotu za jednotlivé regiony.
extremeValuesByRegion1 = correctValues.groupby("Region").agg({"AvgTemperatureCelsia": ["max", "min"]})
print(extremeValuesByRegion1)

