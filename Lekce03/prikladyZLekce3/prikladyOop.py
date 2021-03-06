# # 1
# class Book:
#   def __init__(self, title, pages, price)
#     self.title = title
#     self.pages = pages
#     self.price = price
#
#
#   def getInfo(self):
#     return f"Kniha se jmenuje {self.title} má {self.pages} stran a stojí {self.price} korun"
#
#   def discount(self, sale):
#     self.price -= self.price * (sale / 100)
#
# kniha = Book ("Harry Potter", 350, 250)
# print(kniha.getInfo())

# 2
class Package:
  def __init__(self, address, weightInKilos)
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

  def deliver(self):
    self.delivered = True

  def getInfo(self):
    # return f"Adresa: {self.address}, Váha: {self.weightInKilos}, Stav: {self.delivered}"
    if self.delivered:
      return f"Balík na adresu {self.address} s váhou {self.weight} kg byl doručen."
    return f"Balík na adresu {self.address} s váhou {self.weight} kg nebyl doručen."



balik = Package("Nova", 11, True)

# # 3
# class Employee:
#   def __init__(self, name, position, probation):
#     self.name = name
#     self.position = position
#     self.holidays = 25
#     self.probation = probation
#
#
#   def takeHolidays(self, days):
#   # self.holidays = self.holidays - days (ale neresi to, ze by clovek mohl jit do minusu, coz je problem)
#     if self.holidays >= days:
#       self.holidays -= days
#       return "Dovolená schválená"
#     else:
#       return f"Můžeš si vzít pouze {self.holidays} dní."
#
#
#
# def getInfo(self):
#   return f"{self.name} pracuje na pozici {self.position}."
