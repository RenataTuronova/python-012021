# # import wget
# # wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
# import wget
# # wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")
# # wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
#
# # dataframe znamena, ze
# # v pripade, ze se nam to nepovede stahnout, zkusit jeste takto:
# # "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv"]
# # for soubor in soubory:
# # #   wget.download(soubor)
# # import pandas
# # u202 = pandas.read_csv("u202.csv")
# # u203 = pandas.read_csv("u203.csv")
# # u302 = pandas.read_csv("u302.csv")
#
# # # print(u202.head())
# # # pozor! - NaN neznamena 0 ale chybejici hodnotu!
# #
# # # chybejici hodnoty si muzeme najit takto ... pak je treba v praxi zjistit, jestli zak z tohoto predmetu nematuroval nebo jen neni zadan
# # # print(u202[u202["znamka"].isnull()])
# #
# # # dropna( ) - vraci datovy set ocisteny od chybejicich dat
# # u202 = pandas.read_csv("u202.csv").dropna()
# # u203 = pandas.read_csv("u203.csv").dropna()
# # u302 = pandas.read_csv("u302.csv").dropna()
# #
# # # po spojeni tabulek vsak nevime, kdo v jake mistnosti maturoval. Tuto informaci si tedy doplnime do puvodnich tri tabulek
# # u202["mistnost"] = "u202"
# # u203["mistnost"] = "u203"
# # u302["mistnost"] = "u302"
# #
# # # spojeni tri dataframe do jednoho - funkce CONCAT
# # maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# # # je potreba to mit v seznamu(list)
# # # concat = spojovani retezcu(i v Excelu)
# # # print(maturita(head())
# #
# # maturita.to_csv("maturita.csv", index=False)
# # maturita.to_excel("maturita.xlsx", index=False)
# #
# # #
# # # UNION = dve nebo vice tabulek pod sebe
# # # JOIN = dve nebo vice tabulek vedle sebe
#
# # import wget
# # wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
#
# import pandas
#
# studenti = pandas.read_csv("studenti.csv")
# print(studenti.head())
# u202 = pandas.read_csv("u202.csv").dropna()
# u203 = pandas.read_csv("u203.csv").dropna()
# u302 = pandas.read_csv("u302.csv").dropna()
# u202["mistnost"] = "u202"
# u203["mistnost"] = "u203"
# u302["mistnost"] = "u302"
# maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# #
# # # propojeni studentu a maturit = ve svete pandas = merge, jinak = join
# # #  je inner, left a right join, vyber podle potreby, podle typu parametru, vetsinou se pouziva left
# # vysledky_se_jmeny = pandas.merge(maturita, studenti, how="left")
# # # # print(vysledky_se_jmeny.head())
# # # # print(maturita.shape)
# # # # print(vysledky_se_jmeny.shape)
# # # # print(maturita[maturita["mistnost"].isnull()])
# # # print(vysledky_se_jmeny[vysledky_se_jmeny["jmeno"].isnull()])
# # # budu pracovat jen se 202, protoze ostatni seznamy maji chybna/chybejici data, coz jsem zjistila.
# # #
# # # import wget
# # # wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")
# #
# # predsedajici = pandas.read_csv("predsedajici.csv")
#
# # # zbaveni se mezer aby nam to nedelalo neplechu a v pripade nechtene mezery nam daneho predsedajiciho program nevyradil
# # predsedajici["den"] = predsedajici["den"].str.strip()
# # vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on=["den"])
# # print(vysledky_se_jmeny_a_predsedajicimi())
# # # print(vysledky_se_jmeny.columns)
# # # print(predsedajici.columns)
# # pokud se nezachovaji nektere radky z duvodu toho, ze funkce merge pro tyto radky nenajde odpovidajici vyznam, musime vyuzit jeste parametru "how".
# # vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on=["den"], how="outer")
#
# # posledni neprijemnost - sloupce jmeno se autom. prejmenovaly, aby v tabulce nemely stejny nazev, pouzijeme tedy metodu rename..
# # vysledky_se_jmeny_a_predsedajicimi = vysledky_se_jmeny_a_predsedajicimi.rename(columns={'jméno_x': 'jméno', 'jméno_y': 'předs'})
#
# # AGREGACE
# # slouzi ke spocitani znamek, prumernou znamku podle predmetu, mistnosti...
# # spocteni hodnot pro kazdy sloupecek:
# # print(maturita.groupby("mistnost").count())
#
# # prumer z hodnot
# print(maturita.groupby("predmet")["znamka"].mean())
#
# # nejhorsi znamka
# print(maturita.groupby("predmet")["znamka"].max())
#
# # a dalsi funkce
# # min = minimum
# # median  = median
# # rozsah znamek = var
# # standardni odchylka hodnot = std
# # prvni hodnota = first
# # posledni hodnota = last
# # True, pokud jsou vsechny hodnoty True = all
# # True, pokud je alespon jedna z hodnot True = any
#
# # soucet znamek
# print(maturita.groupby("predmet")["znamka"].sum())
#
# # import wget
# # wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/03d3b81430e651e03743b19084e935d87dd40ccd/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
#
# nakupy = pandas.read_csv("nakupy.csv")
# print(nakupy.groupby("Jméno").sum())
#
# # pozn.
# # stahnout si request
# # request.get(ulozit si predsedajici atd)
# # posledni radek napr. open u202_csv

import pandas
states = pandas.read_json("staty.json")
states = states.set_index("name")

# Pocitane sloupce = muzeme pridat sloupec, ve kterem bude urcita vypoctena hodnota jiz ze zadanych hodnot.
states["population_density"] = states["population"] / states["area"]

# razeni
# metoda sort_values standardne radi vzestupne(ascending), pokud chceme opacne, musime vypsat podminku ascending=False
# states = states.sort_values(by="population_density", ascending=False) # = chci hodnoty sestupne

states = states.sort_values([by="population_density", "area"], ascending=(False,True))
print(states.head())