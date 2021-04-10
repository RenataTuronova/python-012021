# program 32 - Twilio podruhé

# Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
# Stažení souboru pomocí wget:

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas

import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")

# 1.
# Výše uvedeným programem načti data o vývoji ceny akcie. Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.
twilio1 = twilio.set_index("Date")
twilio1["Close"].plot()
plt.show()

# DOBROVOLNÝ DOPLNĚK
# Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
ax1 = twilio1["Close"].plot()
ax1.set_ylabel("Cena ($)")
ax1.set_xlabel("Datum")
ax1.set_title("Vývoj ceny akcií v čase")
plt.show()

# 2.
# Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím. Porovnej grafy a zjisti, co se změnilo.
twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio2 = twilio.set_index("Date")
twilio2["Close"].plot()
plt.show()
# Zhodnocení: Na průběhu grafu se nezměnilo nic. Změnil se pouze formát dat na ose x. V prvním případě popisky obsahují den, měsíc i rok, v druhém případě pouze měsíc a rok.

# DOBROVOLNÝ DOPLNĚK
# Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
ax2 = twilio2["Close"].plot()
ax2.set_ylabel("Cena($)")
ax2.set_xlabel("Datum")
ax2.set_title("Vývoj ceny akcií v čase")
plt.show()


