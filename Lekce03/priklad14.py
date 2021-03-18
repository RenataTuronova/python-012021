# program14 - Vyplata

# Uvažujme nyní opět třídu Employee, kterou jsme si ukázali v lekci. Pro zjednodušení nyní nebudeme pracovat s dovolenou, proto nám stačí třída, která je v ukázce níže.
#
# class Employee:
#   def get_info(self):
#     return f"{self.name} pracuje na pozici {self.position}."
#   def __init__(self, name, position):
#     self.name = name
#     self.position = position
# Nyní se budeme zabývat platem. Přidej třídě atribut salary (výše hrubého platu) a children (počet dětí), jehož výši nastavíš ve funkci __init__(). Dále přidej funkci get_net_salary(), která vypočte a vrátí výši čisté mzdy. Uvažuj zjednodušený výpočet: sazba daně je 15 % a sleva na jedno dítě 1500 Kč. Vzorec pro výpočet daně tedy je: daň = hrubá mzda * 0.15 - počet dětí * 1500. Funkce vrátí výši čisté mzdy, tj. čistá mzda = hrubá mzda - daň.
#
# Pokročilejší verze: Pokud máš zájem, můžeš zkusit pokročilejší verzi. Rozlož výpočet do dvou funkcí. Přidej funkci get_tax(), která vypočte výši daně, a poté funkci get_net_salary(). Výpočet daně bude ve funkci get_tax(). Funkce get_net_salary() zavolá funkci get_tax(), aby zjistila výši daně, a poté vrátí čistou mzdu. Volání funkce proveď pomocí klíčového slova, tj. např.:
# net_salary = self.salary - get_tax()
# Bod samozřejmě získáš za obě verze :-)


class Employee:
  def getInfo(self):
    return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children

  def getTax(self):
    tax = (self.salary * 0.15) - (self.children * 1500)
    return tax

  def getNetSalary(self):
    netSalary = self.salary - self.getTax()
    netSalary = round(netSalary)
    return netSalary


employee = Employee("Jana Nováková", "účetní", 40000, 2)
result = employee.getNetSalary()
print(employee.getInfo())
print(f"Výše čisté mzdy zaměstnance je {result} korun.")

employee = Employee("Pavel Nový", "právník", 45000, 1)
result = employee.getNetSalary()
print(employee.getInfo())
print(f"Výše čisté mzdy zaměstnance je {result} korun.")