# program18 - Inverview
#
# Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků, zaměstnanců, uchazečů o práci atd.).
# class Kontakt:
#   def __init__(self, jmeno, email):
#     self.jmeno = jmeno
#     self.email = email
# Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci. Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru. Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".
# Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru. Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl. Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl, vrať chybový text, který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis a vrať text s informací, že zápis byl uložen.


from datetime import datetime

now = datetime.now()
dateNow = now.strftime("%d. %m. %Y")

class Contact:
  def __init__(self, name, email):
    self.name = name
    self.email = email

class Candidate(Contact):
  def __init__(self, name, email, dateOfInterview, recordFromInterview = ""):
    super().__init__(name, email)
    self.dateOfInterview = dateOfInterview
    self.recordFromInterview = recordFromInterview

  def saveRecord(self, recordFromInterview):
    self.recordFromInterview = recordFromInterview
    if self.dateOfInterview < dateNow:
      return f"Zápis z pohovoru byl uložen."
    else:
      return f"Chybné zadání. Je potřeba zadat již proběhlý pohovor."



candidate1 = Candidate("David Kopec", "davidkopec@gmail.com", "15. 3. 2021")
candidate2 = Candidate("Eva Volná", "evavolna@gmail.com", "16. 3. 2021")
candidate3 = Candidate("Dorota Malá", "dorotamala@gmail.com", "17. 3. 2021")

print(f"Kontaktní údaje uchazeče: {candidate1.name}, email: {candidate1.email}, datum pohovoru: {candidate1.dateOfInterview}")
print(candidate1.saveRecord("Kandidát byl u pohovoru úspěšný."))

print(f"Kontaktni udaje uchazece: {candidate2.name}, email: {candidate2.email}, datum pohovoru: {candidate2.dateOfInterview}")
print(candidate2.saveRecord("Kandidat byl u pohovoru uspesny."))