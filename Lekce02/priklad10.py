#program10 - Klíč k úspěchu
#Obchodníci v naší softwarové firmě používají jednoduchý systém, aby odhadli šanci na úspěch potenciální zakázky. Každé zakázce přiřadí body od 0 do 10 a platí:
#
#Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
#Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
#Pokud má zakázka více bodů, šance na získání je vysoká.
#Body přidělují podle následujících kritérií:
#
#Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu. Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.
#Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje, u velkých občas ano. Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.
#Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod). Ostatním zemím dej 0.
#Konference: Firma loni pořádala odbornou konferenci pro zákazníky. Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.
#Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.
#Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria. Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False. Funkce vrátí šanci na získání zakázky jako řetězec.


industry = input("Zadejte odvětví, ve kterém zákazník podniká: ")

finance = input("Zadejte obrat firmy zákazníka v eurech: ")
finance = finance.replace(" ", "")
finance = int(finance)

country = input("Zadejte zemi, ve které zákazník podniká: ")

conference = input("Byl zákazník na konferenci? [ano/ne] ")

newsletter = input("Odebírá zákazník newsletter? [ano/ne] ")

def probability(industry, finance, country, conference=False, newsletter=False):
  points = 0
# industry
  if industry == "automotive":
    points += 3
  elif industry == "retail":
    points += 2
  else:
    points += 0

# finance
  if finance < 10000000:
    points += 0
  elif finance >= 10000000 and finance <= 1000000000:
    points += 3
  else:
    points += 1

# country
  if country == "Česko" or country == "Slovensko":
    points += 2
  elif country == "Německo" or country == "Francie":
    points += 1
  else:
    points += 0

# conference
  if conference == "ano":
    points += 1

# newsletter
  if newsletter == "ano":
    points += 1

  return points

sumPoints = probability(industry, finance, country, conference, newsletter)
if sumPoints <= 5:
  probability = "malá"
elif sumPoints >= 6 and sumPoints <= 8:
  probability = "střední"
elif sumPoints > 8:
  probability = "vysoká"

print(f"Zakázka získala dle zadaných kritérií {sumPoints} bodů. Šance na její získání je {probability}.")






