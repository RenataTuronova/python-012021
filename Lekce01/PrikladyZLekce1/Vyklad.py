# # #
#slovnik = slozene zavorky
# item = {"title": "Cajova konvicka", "price": 899, "inStock": True}
#
# title = item["title"]
# print(title)
# or
# print(item["title"]

# # 3 zpusoby zapsani vety: 1.
# print("Vybrany predmet je " + item["title"] + ".")
#
# # 2. (nevyhoda je, ze vlozi pred tecku mezeru a s tim nic nenadelame)
# print("Vybrany predmet je", item["title"], ".")
#
# # 3. formou formatovaneho retezce
# print(f"Vybrany predmet je {item['title']}.")
#
# # pridani ceny, ale pozor v Python nejde slozit retezec s cislem

# print("Vybrany predmet je " + item["title"] + " a cena je " + str(item["price"]) + ".")
# print("Vybrany predmet je", item["title"], "a cena je", item["price"], ".")
# print(f"Vybrany predmet je {item['title']} a cena je {item['price']}.")

# # zjisteni zda neco ve slovniku je
# item = {"title": "Cajova konvicka", "price": 899, "inStock": True}
# if "weight" in item:
#     print(f"Hmotnost je {item['weight']}")
# else:
#     print("Hmotnost neni zadana.")

# # pridani nejakeho klice nebo uprava
# item = {"title": "Cajova konvicka", "price": 899, "inStock": True}
# item["weight"] = 0.5
# if "weight" in item:
#     print(f"Hmotnost je {item['weight']}")
# else:
#     print("Hmotnost neni zadana.")

# # zmena nejakeho klice, existujici polozky
# item = {"title": "Cajova konvicka", "price": 899, "inStock": True}
# item["price"] = 999
# price = item["price"]
# print(price)


#opekani burtu
# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
# # pocet polozek
# print(len(sausages))
# # nekde nakonec neprijde, potrebuju ho vyradit
# # budto takto, ale nezmeni nam to pocet prichozich
# sausages["Jirka"] = 0
# # lepsi postup
# sausages.pop("Jirka")
# print(len(sausages))


# # 1.priklad
# print("Vysvedceni")
# predmet = {"cesky jazyk": 3, "matematika": 1, "dejepis" : 2}
# print(predmet)

#2.priklad
# print("Detektivky")
# sales = {"Zkus mě chytit": 4165, "Vrah zavolá v deset": 5681, "Zločinný steh": 2565}
# sales["Noc, ktera me zabila"] = 0
# print(sales)

# sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 100
# print(sales)
# #or
# sales["Vrah zavolá v deset"] += 100
# print(sales)

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
#
# # #  # Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku.
# # # Vstup uživatele si převeď na int!
# cisloListku = int(input("Zadej cislo listku: "))
# # # Zkontroluj, zda je číslo lístku ve slovníku.
# if cisloListku in tombola:
#     print(f"Vyhral jsi {tombola[cisloListku]}")
#     tombola.pop(cisloListku)
# else:
#     print(f"Bohuzel nevyhravas nic.")
# # Pokud ne, vypiš text "Bohužel nevyhráváš nic."
# # Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.


# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
#
# jmeno = input ("Zadej tve jmeno: ")
# if jmeno in passwords:
#     heslo = input("Zadej tve heslo: ")
#     if heslo = paswords["jmeno"]


#
# else:
#     print("Nejsi na seznamu, nemuzes vstoupit.")