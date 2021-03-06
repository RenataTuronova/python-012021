sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# print("Vydane knizky: ")
# # jedna hodnota
# for key in sales:
#   print(key)
# # or
#   print(sales[key])
#
# # vice hodnot
# for key, value in sales.items():
#   print(f"Knihy {key} se prodalo {value} kusu.")
#
# # celkovy pocet hodnot
# total = 0
# for key, value in sales.items():
#   print(f"Knihy {key} se prodalo {value} kusu.")
#   total += value
#   # total = total + value
# print(f"Celkem bylo prodano {total} knih.")
# print(f"Celkem bylo prodano " + str(total) + " knih.")

# # TROJROZMERNE SLOVNIKY
# celkove trzby
books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
# total = 0
for item in books:
  total += item["sold"] * item["price"]
# print(f"Celkove trzby jsou {total}.")

# trzby jen za nektere knizky
# total = 0
# for item in books:
#   if item["year"] == 2019:
#      total += item["sold"] * item["price"]
# print(f"Celkove trzby jsou {total}.")