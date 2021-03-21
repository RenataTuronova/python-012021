# program20 - Fake news
#
# Moduly v Pythonu se často snaží zpříjemnit život programátorům. Například je občas otrava vymýšlet jména nebo adresy, když chceme vyzkoušet, jestli náš program funguje. Jindy třeba potřebujeme nějaká data anonymizovat, tj. odebrat z nich citlivé osobní údaje jako jména, adresy atd. Pro tento účel existuje modul Faker, která nám umí vygenerovat jména, adresy a řadu dalších dat, které můžeme využít při testování našich programů.
# Nainstaluj si modul Faker pomocí postupu, který jsme si ukazovali na cvičení a je popsán v příkladu 19.
# Níže máš příklad použití modulu. Nejprve provedeme import modulu, následně vytvoříme objekt generator_falesnych_dat třídy Faker. Využijeme parametr "cs_CZ", který řekne modulu, aby nám generoval česká jména a adresy. Objekt generator_falesnych_dat má naprogramované funkce jako name() pro vygenerování náhodného jména, address pro vygenerování náhodné adresy atd.


from faker import Faker
fake = Faker("cs_CZ")

# print(fake.name())
# print(fake.address())

class Balik:
  def getInfo(self):
    print(f"Příjemce balíku: {self.name}")
    print("Balík doručte na adresu: " + self.address)

  def __init__(self, name, address):
    self.name = name
    self.address = address

# 1.
# Zkus nyní vytvořit nějaký objekt ze třídy Balik a přiřadit mu náhodně vygenerované jméno příjemce a adresu. Pomocí funkce get_info() si nech informace o balíku vypsat.
#name = fake.name()

name = fake.name()
address = fake.address()

balik = Balik(name, address)
print(balik.getInfo())

# 2.
# Pokročilejší varianta
# Uvažujme nyní společnost, která přepravuje balíky do více zemí. V dokumentaci si najdi odstavec Localization. Tam najdeš informaci, že "faker.Faker also supports multiple locales". Podívej se, jak je v příkladu vytvořen objekt Faker (je použit seznam). Zkus nyní upravit svůj program tak, aby generoval adresy v rámci České i Slovenské republiky. Příslušnou zkratku pro Slovensko najdeš taktéž v dokumentaci k modulu.

from faker import Faker
fake = Faker(["cs_CZ", "sk_SK"])

class Balik:
  def getInfo(self):
    print(f"Příjemce balíku: {self.name}")
    print("Balík doručte na adresu: " + self.address)

  def __init__(self, name, address):
    self.name = name
    self.address = address

name = fake.name()
address = fake.address()

balik = Balik(name, address)
print(balik.getInfo())
