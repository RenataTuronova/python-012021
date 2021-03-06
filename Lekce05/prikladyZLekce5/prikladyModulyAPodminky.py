# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

#udelala jsem ze sloupce index, uz to neni standardni sloupec (uz se sloupci tolik zvedne sebevedomi, ze se neobtezuje zobrazovat se ve vypisu.
# print(staty.index) # jmena tech statu jsou ted tady v jakesi mnozine indexu nasich dat

# # chci si vypsat informaci napr. o CR, pokud bych nevyuzivala toto, musela bych si zjistit na kterem radku CR je, bylo by to slozite
# # takto je to jednodussi pomoci ".loc[]"
# print(staty.loc["Czech Republic"])
#
# # kdyz chceme vypsat vsechny infomrace o statech od CR az po Dominikanskou republiku
# print(staty.loc["Czech Republic":"Dominican Republic"])
#
# # chci vypsat info o vsech statech od Uzbekistanu az do konce
# print(staty.loc["Uzbekistan":])
#
# # chci vypsat jen vybrane staty, v tomto pripade CR a Slovensko
# print(staty.loc[["Czech Republic", "Slovakia"]])
#
# # chci vypsat pro urcite staty pouze urcity sloupec (informaci)
# print(staty.loc[["Czech Republic", "Slovakia"], "capital"])
# print(staty.loc[["Czech Republic", "Slovakia"], "gini"])
#
# # chci pro urcite staty vypsat konkretni info (2 sloupce), dam je do seznamu[] jako druhy parametr
# print(staty.loc[["Slovakia", "Poland", "Austria", "Germany"], "gini"]
# print(staty.loc[["Slovakia", "Poland", "Austria", "Germany"], ["area", "population"]]

# # chci vypsat konkreti sloupec, vypisu konkretne nazev sloupce
# # hranatou zavorku napiseme primo za nazev promenne, kde mame ulozeny DataFrame a vepiseme do ni nazev sloupce
# populace = staty["population"]
# populace = staty[["population", "area"]]
#
# # chci celovou populaci
# print(populace.sum())
#
# # chci vypsat staty s populaci mensi nez 1000 obyvatel
# # tento zapis nam da pouze polotovar = hodnoty True and False
# print(staty[staty["population"] < 1000)
# # proto je potreba  nasi podminku vlozit do hranatych zavorek. Rika nam to, ze stale pracujeme se staty, ale s jeho vyberem staty[staty a neco (
#
# ministaty = staty[staty["population"] < 1000]
# ministaty[["population", "area"]]
#
# lidnateEvropskeStaty = staty[(staty["population"] > 2000000)] # takto se nam vypisi staty s poctem obyvatel nad 20000000 ale z celeho sveta, musime jeste vyselektovat Evropu
# print(lidnateEvropskeStaty)
#
# # znak "&" znamena "a", obe podminky musi byt splneny
lidnateEvropskeStaty = staty[(staty["population"] > 20000000) & (staty["region"] == "Europe")]
# # lidnateEvropskeStaty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")] #lze zapsat i s podtrzitky, python si toho nevsima, je to jen pro nas pro vetsi prehlednost
# print(lidnateEvropskeStaty)
#
# #znak "|" (Alt + W) znamena "nebo", jedna z podminek musi byt splnena
vyznameneStaty = staty[(staty["population"] > 1_000_000_000) | (staty["area"] > 3_000_000)]

# # funkce .isin()
# staty["subregion"].isin(["Western Europe", "Estern Europe"])
# # pokud bych dala jen print a toto, opet by mi vysly jen hodnoty True nebo False


zapVychEvropa = staty[staty["subregion"].isin(["Western Europe", "Estern Europe"])]
print(zapVychEvropa)


