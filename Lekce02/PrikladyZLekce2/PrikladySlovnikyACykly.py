books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
# totalPages = 0
# for item in books:
#   totalPages += item["pages"]
# print(f"Celkove Gustav precetl {totalPages} stran.")

# book8 = 0
# for item in books:
#   if item["rating"] >= 8:
#     book8 += 1
# print(f"Pocet knih s hodnocenim alespon 8 je {book8}.")

# # Vysvedceni
schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}

# sumMarks = 0
# for subject, mark in schoolReport.items():
#   sumMarks += mark
# print(sumMarks)
# prumer = sumMarks / 2
# print(prumer)

for subject, mark in schoolReport.item():
  if mark == 1:
    print(subject)

# # ukol 3
# plates = {"4A2 3000": "František Novák",
#   "6P5 4747": "Jana Pilná",
#   "3B7 3652": "Jaroslav Sečkár",
#   "1P5 5269": "Marta Nováková",
#   "37E 1252": "Martina Matušková",
#   "2A5 2241": "Jan Král"}
#
# for spz, majitel in plates.items():
#   if spz[1] == "P":
#     print(majitel)