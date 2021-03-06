# 1. Balik
# class Package:
#   def __init__(self, address, weightInKilos)
#     self.address = address
#     self.weightInKilos = weightInKilos
#     self.delivered = False
#
#   def deliver(self):
#     self.delivered = True
#
#   def getInfo(self):
#     # return f"Adresa: {self.address}, Váha: {self.weightInKilos}, Stav: {self.delivered}"
#     if self.delivered:
#       return f"Balík na adresu {self.address} s váhou {self.weight} kg byl doručen."
#     return f"Balík na adresu {self.address} s váhou {self.weight} kg nebyl doručen."
#
# class ValuablePackage(Package):
#   def __init__(self, address, weightInKilos, value):
#     super().__init__(address, weightInKilos)
#     self.value = value
#
# valuablePackage = ValuablePackage("Nova, Praha", 80, 100)

# 2. Castecny uvazek

class Employee:
  def __init__(self, name, position):
    self.name = name
    self.position = position

  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."


class PartTimeEmployee(Employee):
  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload

  def getInfo(self):
    print(super().getInfo())
    return f"Jde o part-time pracovnika s uvazkem {self.workload}."

brigadnik = PartTimeEmployee("Renata Turonova", "brigadnik ve skladu", 0.5)
print((super().getInfo(), print(getInfo())


