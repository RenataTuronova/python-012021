# pokud bychom chteli vyclenit zamestance na polovicni uvazek a delali to prekopirovanim a upravou podtridy (potomka) podle potreb, pokud by bylo vice vyclenenych podtrid, byl by zapis velmi dlouhy a snadno bychom udelali chybu pri kopirovani.
# viz toto:

class Employee:
  def takeHolidays(self, days):
    # self.holidays = self.holidays - days (ale neresi to, ze by clovek mohl jit do minusu, coz je problem)
    if self.holidays >= days:
      self.holidays -= days
      return "Dovolená schválená"
    else:
      return f"Můžeš si vzít pouze {self.holidays} dní."

  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25


class PartTimeEmployee:
  def takeHolidays(self, days):
    if self.holidays >= days:
      self.holidays -= days
      return "Dovolená schválená"
    else:
      return f"Můžeš si vzít pouze {self.holidays} dní."

  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

# proto vyuzivame dedicnost:

class Employee:  # = RODIC
  def takeHolidays(self, days):
  # self.holidays = self.holidays - days (ale neresi to, ze by clovek mohl jit do minusu, coz je problem)
    if self.holidays >= days:
      self.holidays -= days
      return "Dovolená schválená"
    else:
      return f"Můžeš si vzít pouze {self.holidays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

# trida partTimeEmployee patri pod tridu Employee, proto dame tuto tridu do zavorky
class PartTimeEmployee(Employee): # = POTOMEK
  def __init__(self, name, position, workload):
    self.name = name
    self.position = position
    self.workload = workload
    self.remainingHolidayDays = 25  # muzu napsat i primo hodnotu...

brigadnik = PartTimeEmployee ("Renata Turonova", "brigadnik ve skladu", 0.5)

# ZAVOLANI FUNKCE OD RODICE - vyuzitim "super()" a tim muzu vymazat v tomto pripade self.name a self.position, ktere plne prejimam od rodice.
class PartTimeEmployee(Employee): # = POTOMEK
  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload