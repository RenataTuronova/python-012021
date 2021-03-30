# program25 - Teplota ve městech podruhé

# Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracovala pokročilou variantu, můžeš pracovat s teplotami ve stupních Celsia.

import pandas
temperature = pandas.read_csv("temperature.csv")

import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:
print(temperature.head())

# Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
specificDay = temperature[temperature["Day"] == 13]
print(specificDay)

# Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
us = temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(us)
temperatureUs = pandas.DataFrame(us, columns=["Region", "Country", "City", "Day", "AvgTemperature", "AvgTemperatureCelsia"])

# Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
specificCity = temperatureUs[temperatureUs["City"].isin(["Washington", "Philadelphia"])]
print(specificCity)

# DOBROVOLNÝ DOPLNĚK

# Vrať se k pomocné tabulce, kterou jsi vytvořila v bodu 2. Vypiš průměrnou hodnotu ze všech měření, která byla provedena 13. listopadu 2017 na úzení Spojených států amerických. K tomu využij funkci .mean(), která funguje stejně jako funkce .sum(), kterou jsme si ukazovali na lekci. Pokud znáš základy statistiky, zkus funkci pro medián .median() a rozptyl .var().
mean = temperatureUs["AvgTemperatureCelsia"].mean()
print(mean)

median = temperatureUs["AvgTemperatureCelsia"].median()
print(median)

variance = temperatureUs["AvgTemperatureCelsia"].var()
print(variance)


