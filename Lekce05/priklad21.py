# program21 - Twilio

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twilio = pandas.read_csv("twlo.csv")
# Zjisti, kolik má soubor řádku a kolik sloupců.
print(twilio.shape[0])
print(twilio.shape[1])

# Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
print(twilio.head(5))
print(twilio.iloc[:5])

# U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru. Tentokrát využij způsob dle vlastního výběru :-)
print(twilio.tail(1))
print(twilio.iloc[-1])


# Doplňující část
# Počet řádků ulož do proměnné pocet_radku jako číslo.
numberOfRows = twilio.shape[0]

# Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu. Pandas ti tuto dhodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec Close) v souboru a poslední hodnotu zavírací ceny v souboru. Vypočítej, o kolik procent se zvýšila hodnota akcie.
oldValue = twilio.iloc[0, -1]
newValue = twilio.iloc[-1, -1]
percentage = newValue / oldValue * 100
# print(percentage)
difference = percentage - 100
# print(difference)
roundDifference = round(percentage - 100)
print(f"Hodnota akcie se zvýšila o {roundDifference} procent.")

# Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii. Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období. Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (price range).
high = (twilio.iloc[:, 3])
print(high.max())
low = (twilio.iloc[:, 4])
print(low.min())

print(f"Obchodní cena akcie se pohybovala v rozmezí {high.max()} až {(low.min())} korun.")
