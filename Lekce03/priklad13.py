# program13 - Vrácení auta
#
# Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.
#
# Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.
#
# Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.
#
# Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené. Poté vypiš informaci o ceně.


class Car:
  def __init__(self, registrationMark, carMake, kilometers, free=True):
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

  def returnACar(self, odometer, days):
    self.odometer = odometer
    self.free = True
    if days <= 7:
      price = days * 400
      return f"Konecná cena za vypůjčení auta na {days} dní/y je {price} korun."
    else:
      price = days * 300
      return f"Konečná cena za vypůjčení auta na {days} dní je {price} korun."

car1 = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
car2 = Car("1P3 4747", "Škoda Octavia", 41253, True)

# car1 = car2
odometer = input("Kolik kilometrů jste s autem ujel? ")
days = int(input("Zadejte počet dní, po které jste měl auto půjčené: "))

print(car1.returnACar(odometer, days))





