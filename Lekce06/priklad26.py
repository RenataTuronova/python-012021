# program26 - Zaměstnanci
# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

# Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
import pandas
employeesPraha = pandas.read_csv("zam_praha.csv")
employeesPlzen = pandas.read_csv("zam_plzeň.csv")
employeesLiberec = pandas.read_csv("zam_liberec.csv")

employeesPraha["mesto"] = "Praha"
employeesPlzen["mesto"] = "Plzeň"
employeesLiberec["mesto"] = "Liberec"

# Vytvoř novou tabulku zaměstnanci a ulož do ní informace o všech zaměstnancích.
employees = pandas.concat([employeesPlzen, employeesPraha, employeesLiberec], ignore_index=True)
print(employees)

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
salary = pandas.read_csv("platy_2021_02.csv")

 # 1. všichni zaměstnanci, i ti, kteří už ve firmě nepracují:
employeesAndSalary = pandas.merge(employees, salary, how = "left")
print(employeesAndSalary)
# print(employees.shape)
# print(salary.shape)
# print(employeesAndSalary.shape)

 # 2. pouze zaměstnanci, kteří ve firmě stále pracují:
employeesAndSalary1 = pandas.merge(employees, salary)
print(employeesAndSalary1)
# print(employees.shape)
# print(salary.shape)
# print(employeesAndSalary.shape)

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
meanSalary = employeesAndSalary.groupby("mesto")["plat"].mean()
print(meanSalary)


# DOBROVOLNÝ DOPLNĚK
# Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
formerEmployees = employeesAndSalary[employeesAndSalary["plat"].isnull()]
numberOfFormerEmployees = formerEmployees.shape[0]
print(numberOfFormerEmployees)
 # nebo:
# numberOfFormerEmployees = len(formerEmployees)
# print(numberOfFormerEmployees)

# V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
# všechny informace o bývalých zaměstnancích
formerEmployees.to_csv("formerEmployees.csv")
# pouze jména bývalých zaměstnanců:
formerEmployeesNames = formerEmployees[["jmeno", "prijimeni"]]
formerEmployeesNames.to_csv("formerEmployeesNames.csv")






