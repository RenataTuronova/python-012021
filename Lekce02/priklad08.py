# program08 - SMS brana
#
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#
# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:
#
# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
#
# Tip: Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš tak, že použiješ funkci replace() a tečkovou notaci. První parametr je znak, který chceš nahradit, a druhý parametr nový znak. Níže je příklad použití.

import math

phoneNumber = input("Zadejte číslo, na které chcete zprávu zaslat: "))
phoneNumber = phoneNumber.replace(" ", "")

def verification(phoneNumber):
  if len(phoneNumber) == 9:
    return True
  elif len(phoneNumber) == 13 and phoneNumber[0:4] == "+420":
    return True
  else:
    print("Zadané číslo má špatný formát.")
    return False

vysledek1 = verification(phoneNumber)
if vysledek1:
  sms = input("Zadejte text zprávy: ")

def totalPrice(sms):
  smsCount = math.ceil(len(sms) / 180)
  paidText = smsCount * 3
  return paidText

print(f"Výsledná cena zprávy je {totalPrice(sms)} Kč.")

