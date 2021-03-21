# program19 - Instalace modulu
# Zopakuj si postup při instalaci modulu. Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně, ale umí si kurz měny stáhnout z internetu.
#
# V PyCharmu klikni na File -> Settings -> Project -> Python Interpreter. Následně klikni na tlačítko + (Install) a vyhledej modul forex-python. Dále klini na Install Package a potvrď instalaci.
# Dále se podívej na následující příklad, jak s modulem pracovat. Na prvním řádku je import, aby Python věděl, že s modulem chceme pracovat. Na druhém řádku vytvoříme objekt prevodnik (je to objekt třídy CurrencyRates), který se stará o převod měn.
# Uvažujme třeba, že chceme spočítat, kolik by nás stálo, pokud bychom chtěli 10 dolarů. Použijeme funkci convert(), která má jako první parametr zkraktu cílové měny, jako druhé parametr zkratku zdrojové měny a jako třetí parametr množství požadovaných dolarů. Funkce vypočte, kolik jednotek zdrojové měny je potřeba zaplatit, aby to odpovídalo požadovanému množství cílové měny.
# Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()). Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK. Následně od uživatele získej i požadované množství cílové měny. Nezapomeň toho množství převést na typ int.
#
# Pokročilejší varianta
# Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí, například převod měny do Bitcoinu. Zkus pomocí modulu vytvořit program, který se zeptá uživatele na měnu a požadovaný počet Bitcoinů a vrátí mu množství měny, které by potřeboval, aby požadované množství Bitcoinů mohl koupit.

# from forex_python.converter import CurrencyRates
# converter = CurrencyRates()
# recquiredInTargetCyrrency = 10
# priceInCzk = converter.convert('USD', 'CZK', recquiredInTargetCyrrency)
# print(priceInCzk)

# # 1.
from forex_python.converter import CurrencyRates
converter = CurrencyRates()
currency = input("Zadejte požadovanou měnu: ")
recquiredInTargetCyrrency = int(input("Zadejte požadované množství měny: "))

if currency == "EUR":
  priceInCzk = converter.convert("EUR", "CZK", recquiredInTargetCyrrency)
  print(priceInCzk)
  print(round(priceInCzk))
elif currency == "GBP":
  priceInCzk = converter.convert("GBP", "CZK", recquiredInTargetCyrrency)
  print(priceInCzk)
  print(round(priceInCzk))
elif currency == "DKK":
  priceInCzk = converter.convert("DKK", "CZK", recquiredInTargetCyrrency)
  print(priceInCzk)
  print(round(priceInCzk))

# 2.
from forex_python.bitcoin import BtcConverter
converter = BtcConverter()
currency = input("Zadejte měnu: ")
bitcoins = int(input("Zadejte požadované množství Bitcoinů: "))

price = converter.convert_btc_to_cur(bitcoins, currency)
print(price)
print(round(price))
