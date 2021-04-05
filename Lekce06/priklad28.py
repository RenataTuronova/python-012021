# program28 - Státy světa potřetí

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. Zkusme nyní zpracovat podobné úlohy pomocí pandas.

# Načti data ze souboru do tabulky.
import pandas
states = pandas.read_json("staty.json")
# print(states.head())

# Vyfiltruj státy, které leží v Evropě.
europe = states[states["region"] == "Europe"]
print(europe)

# Zjisti počet států v jednotlivých subregionech Evropy.
numberOfEuropeStates = europe.groupby("subregion")["name"].count()
print(numberOfEuropeStates)

# Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
populationInSubregion = europe.groupby("subregion")["population"].sum()
print(populationInSubregion)

# ROZŠÍŘENÉ ZADÁNÍ
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za roky 2017-2019 ze Světové banky.
# Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
gdp1 = pandas.read_csv("gdp.csv")
gdp = pandas.read_csv("gdp.csv").dropna()

# Propoj obě tabulky podle třípísmenného kódu států.
gdp = gdp.rename(columns={"Country Code": "alpha3Code"})

statesAndGdp = pandas.merge(states, gdp, how="left")
print(statesAndGdp.head())

# print(states.shape)
# print(gdp.shape)
# print(statesAndGdp.shape)

# Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
gdpAndPopulation2019 = statesAndGdp.groupby("subregion")[["2019", "population"]].sum()

# # Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst). K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.
gdpAndPopulation2019["gdp per capita"] = gdpAndPopulation2019["2019"] / gdpAndPopulation2019["population"]
print(gdpAndPopulation2019)
