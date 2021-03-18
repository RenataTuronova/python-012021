# program15 - Prodej vstupenek
#
# Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.
#
# Datum	                      Cena
# 1. 7. 2021 - 10. 8. 2021	  250 Kč
# 11. 8. 2021 - 31. 8. 2021	  180 Kč
# Mimo tato data je středisko zavřené.
#
# Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime(). Následně se zeptej na počet osob,
# Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.
# Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.".
#
# prvni_udalost = datetime(2021, 7, 1)
# druha_udalost = datetime(2021, 7, 3)
# if prvni_datum < druhe_datum:
#   print("Druhá událost se stala po první události")

from datetime import datetime

cinema = input("Zadejte datum, na které chcete vstupenku koupit: ")
date = datetime.strptime(cinema, "%d. %m. %Y")


startDate1 = datetime(2021, 7, 1)
endDate1 = datetime(2021, 8, 10)
startDate2 = datetime(2021, 8, 10)
endDate2 = datetime(2021, 8, 31)

if date >= startDate1 and date <= endDate1:
  persons = int(input("Zadejte počet požadovaných vstupenek: "))
  price = 250 * persons
  print(f"Celková cena za vstupenky je {price} korun.")
elif date > startDate2 and date <= endDate2 :
  persons = int(input("Zadejte počet požadovaných vstupenek: "))
  price = 180 * persons
  print(f"Celková cena za vstupenky je {price} korun.")
else:
  print("Letní kino je v zadaný termín uzavřené.")