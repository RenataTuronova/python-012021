import matplotlib.pyplot as plt
import pandas
# import wget
#
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.txt")
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt")

# # # 1.
# # jedna se sice o soubor .txt, ale podoba se csv, proto pouzivame pandas.read_csv (proste to Jirka rekl, sama bych na to neprisla)
# kostky = pandas.read_csv("kostky.txt", header=None) # header=None znamena, ze chceme, at si python popisky udela sam
# print(kostky.head())
#
# kostky = pandas.Series(kostky)
#
# kostky.hist(bins=[2, 3, 6, 8, 10, 12])
# plt.show()
# #
# #
# # # 2.
# # V souboru callcentrum.txt najdete několik tisíc záznamů pro call centrum, které udávají časy mezi jednotlivými příchozími hovory v minutách a vteřinách. Načtěte tato data do série v Pythonu. Časy převeďte na vteřiny a zobrazte jejich histogram a boxplot. Co lze z těchto dvou grafů vyčíst?
#
# from datetime import datetime as dt
#
# zaznam = pandas.read_csv("callCentrum.txt", header=None)
# # nebo prevest rucne delenim 60
# zaznam = pandas.Series(zaznam)
# print(dt.timestamp(dt(zaznam)))
#
# print(zaznam.head())

# # 3.
#
snih = [
  [1968, 480, 351],
  [1969, 462, 663],
  [1970, 443, 490],
  [1971, 518, 444],
  [1972, 537, 420],
  [1973, 446, 941],
  [1974, 446, 691],
  [1975, 450, 477],
  [1976, 356, 395],
  [1977, 381, 652],
  [1978, 345, 525],
  [1979, 430, 762],
  [1980, 266, 316],
  [1981, 533, 781],
  [1982, 471, 769],
  [1983, 407, 801],
  [1984, 526, 633],
  [1985, 391, 488],
  [1986, 361, 624],
  [1987, 470, 471],
  [1988, 506, 514],
  [1989, 333, 208],
  [1990, 462, 909],
  [1991, 438, 443],
  [1992, 364, 488],
  [1993, 452, 579],
  [1994, 484, 519],
  [1995, 460, 809],
  [1996, 465, 682],
  [1997, 431, 814],
  [1998, 463, 595],
  [1999, 460, 512],
  [2000, 503, 750],
  [2001, 462, 951],
  [2002, 429, 413],
  [2003, 405, 738],
  [2004, 477, 777],
  [2005, 385, 316],
  [2006, 368, 417],
  [2007, 513, 635],
  [2008, 448, 689],
  [2009, 525, 443],
  [2010, 427, 225],
  [2011, 460, 618],
  [2012, 417, 742],
  [2013, 517, 247],
  [2014, 466, 552],
  [2015, 523, 441],
  [2016, 422, 690],
  [2017, 420, 699]
]

snihdf = pandas.DataFrame(snih, columns=['rok', 'Hora silenstvi', 'Prasne udoli'])
snihdf = snihdf.set_index('rok')
#
# snihdf.plot(kind="box", whis=[10, 90])
# plt.show()
# # Vypravila bych se do Prasneho udoli, kde je pravdepodobne vetsi mnozstvi snehu

# pokud bych si z toho chtela vytvorit html soubor:
snihdf.to_html("tabulka.html")