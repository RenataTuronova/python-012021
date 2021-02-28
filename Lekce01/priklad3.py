# program03 - Zasedačky
#
# Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku. Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné. Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room. Poté vypíše počet volných místností, které jsou k dispozici.

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input("Na kterou hodinu chcete zamluvit meeting room? "))
if hodina in volnePokoje:
  pocetZasedacek = len(volnePokoje[hodina])
  print(f"Místností k dispozici: {pocetZasedacek}.")
  print(volnePokoje[hodina])
else:
  print ("Žádná meetingová místnost není k dispozici.")