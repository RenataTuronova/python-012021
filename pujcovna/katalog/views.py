from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
#     return HttpResponse("Zde bude titulní strana.")
      return HttpResponse("""<h1>Autopůjčovna CAR HIRE Brno</h1>   
<h2>Zarezervujte si své auto osobně či online ještě dnes!</h2>  
<p>CAR HIRE nabízí zákazníkům široký sortiment aut k zapůjčení. Poskytneme Vám vůz pro každou příležitost, ať už se chystáte na dovolenou, stěhujete se, či potřebujete auto pro své podnikání. Díky naším komplexním službám si můžete bezstarostně půjčit vůz krátkodobě i dlouhodobě, a to za akční ceny. Přesvědčte se sami!<br>
<h3>Využijte našich skvělých služeb.</h3> 
</p>Nabídku vozidel naleznete na odkazu níže:</p>
<a href='http://localhost:8000/katalog/seznam/'>Zobrazit vozidla</a><br>
""")

class SeznamView(View):
    def get(self, request):
      return HttpResponse("Zde bude seznam aut.")


#       ("""<ul>
#   <li>Coffee</li>
#   <li>Tea</li>
#   <li>Milk</li>
# </ul>""")
