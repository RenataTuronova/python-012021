# def greetUser():
#   print("Ahoj")
# greetUser()

# def greetUser(name):
#   print(f"Ahoj {name}")
# greetUser("Jirko")

# def sumTwoNumbers(a, b):
#   return a + b
# result = sumTwoNumbers(5, 9)
# print(result)

# def getMark(points):
#   if points <= 60:
#     mark = 5
#   elif points <= 70:
#     mark = 4
#   elif points <= 80:
#     mark = 3
#   elif points <= 90:
#     mark = 2
#   else:
#     mark = 1
#   return mark
#
# points = input("Zadej pocet bodu: ")
# points = int(points)
# mark = getMark(points)
# if mark == 5:
#   points = input("Pocet bodu z opravneho testu: ")
#   points = int(points)
#   mark = getMark(points)
# print(f"Vysledna znamka je {mark}.")

# def getMark(points, bonus=0):
#   if points + bonus <= 60:
#     mark = 5
#   elif points + bonus <= 70:
#     mark = 4
#   elif points + bonus <= 80:
#     mark = 3
#   elif points + bonus <= 90:
#     mark = 2
#   else:
#     mark = 1
#   return mark
#
# points = input("Zadej pocet bodu: ")
# points = int(points)
# bonus = input("Zadejte bonusove body: ")
# bous = int(bonus)
# mark = getMark(points)
# if mark == 5:
#   points = input("Pocet bodu z opravneho testu: ")
#   points = int(points)
#   mark = getMark(points)
# print(f"Vysledna znamka je {mark}.")
