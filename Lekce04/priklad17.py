# program17 - Streamovací služba podruhé
#
# Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.
# Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).
# Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.
# Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.
# Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().


# Jednodušší varianta
class Item:
  def __init__(self, title, genre):
    self.title = title
    self.genre = genre

  def getInfo(self):
    return f"Pořad má název {self.title} a žánrem spadá do kategorie {self.genre}."

class Movie(Item):
  def __init__(self, title, genre, lenght):
    super().__init__(title, genre)
    self.lenght = lenght

  def getInfo(self):
    print(super().getInfo())
    return f"Jedná se o film, jehož délka je {self.lenght} minut."

  def getTotalLenght(self):
    totalLenght = self.lenght
    return totalLenght

class Serial(Item):
  def __init__(self, title, genre, numberOfEpisodes, episodeLenght):
    super().__init__(title, genre)
    self.numberOfEpisodes = numberOfEpisodes
    self.episodeLenght = episodeLenght

  def getInfo(self):
    print(super().getInfo())
    return f"Jedná se o seriál, který má {self.numberOfEpisodes} epizod. Délka jedné epizody je {self.episodeLenght} minut."

  def getTotalLenght(self):
    totalLenght = self.numberOfEpisodes * self.episodeLenght
    return totalLenght

movie = Movie("Přelet nad kukaččím hnízdem", "drama", 133)
serial = Serial("The Big Bang Theory", "sitcom", 12, 20)

totalLenght = movie.getTotalLenght() + serial.getTotalLenght()

class User:
  def __init__(self, username, lenghtOfWatching=0):
    self.username = username
    self.lenghtOfWatching = lenghtOfWatching


  def addViews(self, totalLenght):
    result = self.lenghtOfWatching + totalLenght
  # return f"Uživatel shlédl celkově {result} minut videa."

    hours = result // 60
    minutes = result % 60
    return f"Uživatel shlédl celkově {hours} hodin a {minutes} minut videa."

user = User("Pavel", 250)
print(user.addViews(totalLenght))


# Složitější varianta
# V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval. Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam). Dále přidej funkci zhledni_polozku(), která do seznamu zhlédnutých pořadů přidánovou položku.
# Dále vytvoř funkci delka_sledování() pro uživatele, která projde položky v seznamu a vrátí celkovou délku všech pořadů, které uživatel zhlédl.
# Vytvoř si ukázkové objekty a ověř, že vše funguje.

class Item:
  def __init__(self, title, genre):
    self.title = title
    self.genre = genre

  def getInfo(self):
    return f"Pořad má název {self.title} a žánrem spadá do kategorie {self.genre}."

class Movie(Item):
  def __init__(self, title, genre, lenght):
    super().__init__(title, genre)
    self.lenght = lenght

  def getTotalLenght(self):
    totalLenght = self.lenght
    return totalLenght

class Serial(Item):
  def __init__(self, title, genre, numberOfEpisodes, episodeLenght):
    super().__init__(title, genre)
    self.numberOfEpisodes = numberOfEpisodes
    self.episodeLenght = episodeLenght

  def getTotalLenght(self):
    totalLenght = self.numberOfEpisodes * self.episodeLenght
    return totalLenght

class User:
  def __init__(self, username, myList):
     self.username = username
     self.myList = myList


  def watchItem(self, newItem):
    myNewList = self.myList + [newItem]
    return myNewList

  def lenghtOfWatching(self):
    total = 0
    for item in myNewList:
      itemLenght = item.getTotalLenght()
      total += itemLenght
      return total


movie1 = Movie("Přelet nad kukaččím hnízdem", "drama", 133)
serial1 = Serial("The Big Bang Theory", "sitcom", 12, 20)
movie2 = Movie("Forrest Gump", "drama/komedie/romantický", 142)

user = User("Pavel", [movie1.title, movie2.title])
print(user.watchItem(serial1.title))
print(user.lenghtOfWatching())