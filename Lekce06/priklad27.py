# program27 - Projekty

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

# Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.
# Načti data ze souboru a ulož je do tabulky.
import pandas
reports = pandas.read_csv("vykazy.csv")
# print(reports.head())

# #Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
print(reports.groupby("project")["hours"].sum())

# DOBROVOLNÝ DOPLNĚK
# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
employeesPraha = pandas.read_csv("zam_praha.csv")
employeesPlzen = pandas.read_csv("zam_plzeň.csv")
employeesLiberec = pandas.read_csv("zam_liberec.csv")

employeesPraha["mesto"] = "Praha"
employeesPlzen["mesto"] = "Plzeň"
employeesLiberec["mesto"] = "Liberec"

employees = pandas.concat([employeesPlzen, employeesPraha, employeesLiberec], ignore_index=True)

reports = reports.rename(columns={"employee_id": "cislo_zamestnance"})
# employeesAndReports = pandas.merge(employees, reports)
employeesAndReports = pandas.merge(employees, reports, how = "left")
print(employeesAndReports)

# Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
print(employeesAndReports.groupby("mesto")["hours"].sum())
