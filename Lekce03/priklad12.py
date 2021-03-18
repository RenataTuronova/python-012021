# program12 - Půjčení auta
# Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.
#
# Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, vrátí text "Potvrzuji zapůjčení vozidla" a změní hodnotu atributu, který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
#
# Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.
#
# Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.
#
# Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát.

class Car:
  def __init__(self, registrationMark, carMake, kilometers, free = True):
    self.registrationMark = registrationMark
    self.carMake = carMake
    self.kilometers = kilometers
    self.free = free

  def rentACar(self):
    if self.free:
      self.free = False
      return "Potvrzuji možnost zapůjčení vozidla."
    else:
      return "Vozidlo není k dispozici."

  def getInfo(self):
    if self.free:
      return f"Vozidlo značky {self.carMake} s spz {self.registrationMark} má najeto {self.kilometers} kilometrů."
    else:
      return f"Vozidlo značky {self.carMake} s spz {self.registrationMark} má najeto {self.kilometers} kilometrů."

car1 = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
car2 = Car("1P3 4747", "Škoda Octavia", 41253, True)

car = input("Jakou značku auta si přejete půjčit? [Peugeot / Škoda] ")
if car == "Peugeot":
  print(car1.getInfo())
  print(car1.rentACar())
if car == "Škoda":
  print(car2.getInfo())
  print(car2.rentACar())


car = input("Jakou značku auta si přejete půjčit? [Peugeot / Škoda] ")
if car == "Peugeot":
  print(car1.getInfo())
  print(car1.rentACar())
if car == "Škoda":
  print(car2.getInfo())
  print(car2.rentACar())

