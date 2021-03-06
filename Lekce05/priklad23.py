# program23 - Vakcíny

# Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.
import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

import pandas
countryVaccinations = pandas.read_csv("country_vaccinations.csv")

# Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10 (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).
specificDate = countryVaccinations[countryVaccinations["date"] == "2021-03-10"]
print(specificDate[["country", "total_vaccinations"]])

# Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
vaccinated = countryVaccinations[(countryVaccinations["date"] == "2021-03-10") & (countryVaccinations["total_vaccinations"] > 1_000_000)]
print(vaccinated)

# Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.
extremeValues = countryVaccinations[(countryVaccinations["daily_vaccinations"] > 100_000) | (countryVaccinations["daily_vaccinations"] < 100)]
print(extremeValues)

# DOBROVOLNÝ DOPLNĚK
# Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy. Použij např. funkci isin().
selection = countryVaccinations[countryVaccinations["date"].isin(["2021-03-10", "2021-03-11"]) & countryVaccinations["country"].isin(["United Kingdom", "Finland", "Italy"])]
print(selection)

# Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09. Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj. opět nemusíš použít modul datetime.
japan = countryVaccinations[(countryVaccinations["country"] == "Japan") & (countryVaccinations["date"] >= "2021-03-03") & (countryVaccinations["date"] <= "2021-03-09")]
print(japan)