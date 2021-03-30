# program24 - Teplota ve městech

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv("temperature.csv")

# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
print(temperature.head(10))

# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
prague = temperature[temperature["City"] == "Prague"]
print(prague)
# Průměrná teplota je na Prahu vysoká, důvodem je, že hodnoty jsou ve stupních Fahrenheita.

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
higherAvgTemperature = temperature[temperature["AvgTemperature"] > 80]
print(higherAvgTemperature)

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
europe = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
print(europe)

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
extremeValues = temperature[(temperature["AvgTemperature"] > 80) | (temperature["AvgTemperature"] < -20)]
print(extremeValues)

# POKROČILEJŠÍ VARIANTA
# Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
higherAvgTemperature1 = temperature[temperature["AvgTemperatureCelsia"] > 30]
print(higherAvgTemperature1)

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
europe1 = temperature[(temperature["AvgTemperatureCelsia"] > 15) & (temperature["Region"] == "Europe")]
print(europe1)

# # Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů.
extremeValues1 = temperature[(temperature["AvgTemperatureCelsia"] > 30) | (temperature["AvgTemperatureCelsia"] < -10)]
print(extremeValues1)
# Některé hodnoty, např. v Africe méně než -70 stupňů Celsia, jsou podivné. Pravděpodobně se jedná o chybné hodnoty.