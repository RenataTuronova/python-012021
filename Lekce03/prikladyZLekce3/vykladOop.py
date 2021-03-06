# class Employee:
#   def getInfo(self):
#     return f"{self.name} pracuje na pozici {self.position}."
#
#   def __str__(self):
#     return self.name
#   # return self.name + ", " + self.position + ", " + str(self.holidays)
#
#   def __init__(self, name, position):
#   # def __init__(self, name, position #probation = false):
#
#     self.name = name
#     self.position = position
#     # muzu napsat i primo hodnotu...
#     self.holidays = 25
#     # self.probation = True
#
# # frantisek = Employee()
# # frantisek.name = "František Novák"
# # frantisek.position = "konstruktér"
# # frantisek.getInfo()
# #
# #
# # klara = Employee()
# # klara.name = "Klára Nová"
# # klara.position = "konstruktérka"
# # klara.getInfo()
#
# frantisek = Employee("František Novák", "konstruktér")
# klara = Employee("Klára Nová", "konstruktérka")
# print(frantisek)
#
#
# # print(frantisek.getInfo())
# # print(klara.getInfo())


class Employee:
  def takeHolidays(self, days):
  # self.holidays = self.holidays - days (ale neresi to, ze by clovek mohl jit do minusu, coz je problem)
    if self.holidays >= days:
      self.holidays -= days
      return "Dovolená schválená"
    else:
      return f"Můžeš si vzít pouze {self.holidays} dní."

print(frantisek.takeHoliday)
