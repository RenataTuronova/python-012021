# html je jazyk, ktery nam ukazuje, jak by mela vypadat nejaka webova stranka.
# ukazka webove stranky:

# <html> # typ souboru
# <head> # hlavicka, ktera neni viditelna
#   <meta charset="UTF-8">
#   <title>Ukazka</title> # titulek webove stranky, napr. kodim.cz
# </head>
# <body> # telo stranky
#   <h1>Nadpis prvni urovně</h1> # h1 je znacka nadpisu, existuje h1-h6, jako podnadpisy, h1 je nejvetsi, h6 nejmensi
#   <p>
#     Text nějakeho odstavce, který obsahuje
#     <em>zvýrazněný text</em> a také <strong> # strong = tucne(lze pouzit i "b" jako ve wordu), em = kurziva (lze pouzit i "i" jako ve wordu)
#     důležitý text</strong> a <u>podtrzeny text </u>.
#   </p>
#
#   <h2>Nadpis druhé úrovně</h2>
#   <div class="sekce1">
#     <p>
#       Druhý odstavec je v takzvaném divu, což je
#       značka, která nemá sama o sobě žádný význam.
#       Také zde máme
#       <a href="http;://www.czechitas.cz"> odkaz na
#       stránky Czechitas</a>., # mezi to vkladame text odkazu, a = odkaz na stranku, href = odkaz
#     </p>
#
#     <ol type="a"> # orderlist (ul = tecka...)
#       <li>Prvni položka seznamu</li>
#       <li>Druha položka seznamu</li>
#       <li>Třeti položka seznamu</li>
#     </ol>
#   </div>
# </body>
# </html>

<html>
<head>
  <meta charset="UTF-8">
  <title>Ukazka</title>
</head>
<body>
  <h1>Nadpis prvni urovně</h1>
  <p>
    Text nějakeho odstavce, který obsahuje
    <em>zvýrazněný text</em> a také <strong>
    důležitý text</strong> a <u>podtrzeny text </u>.
  </p>

  <h2>Nadpis druhé úrovně</h2>
  <div class="sekce1">
    <p>
      Druhý odstavec je v takzvaném divu, což je
      značka, která nemá sama o sobě žádný význam.
      Také zde máme
      <a href="http;://www.czechitas.cz"> odkaz na
      stránky Czechitas</a>.,
    </p>

    <ol type="a"> )
      <li>Prvni položka seznamu</li>
      <li>Druha položka seznamu</li>
      <li>Třeti položka seznamu</li>
    </ol>
  </div>
</body>
</html

# !pokazde po urcite zmene je potreba stisknout f5.
# v prohlizeci pokud na jakekoli strance klikneme na f12, ukaze se nam kod.