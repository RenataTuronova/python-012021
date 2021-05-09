from django.views import View
from django.http import HttpResponse

from django.views.generic import ListView
from . import models

class IndexView(View):
    def get(self, request):
#     return HttpResponse("Zde bude titulní strana.")
      return HttpResponse("""<h1>Autopůjčovna CAR HIRE</h1>   
<h2>Zarezervujte si své auto osobně či online ještě dnes!</h2>  
<p>CAR HIRE nabízí zákazníkům široký sortiment aut k zapůjčení. Poskytneme Vám vůz pro každou příležitost, ať už se chystáte na dovolenou, stěhujete se, či potřebujete auto pro své podnikání. Díky naším komplexním službám si můžete bezstarostně půjčit vůz krátkodobě i dlouhodobě, a to za akční ceny. Přesvědčte se sami!</p>
<h3>Využijte našich skvělých služeb.</h3> 
<p>Na odkazech níže naleznete vozidla k zapůjčení, přehled vypůjček a seznam našich zákazníků.</p>
<p><a href='http://localhost:8000/catalog/carlist/'>Zobrazit seznam vozidel</a></p>
<p><a href='http://localhost:8000/catalog/hirelist/'>Zobrazit přehled vypůjček</a></p>
<p><a href='http://localhost:8000/catalog/customerlist/'>Zobrazit seznam zakazníků</a></p>
""")

class CarListView(ListView):
    model = models.Car
    template_name = "catalog/carlist.html"

class HireListView(ListView):
    model = models.Hire
    template_name = "catalog/hirelist.html"


class CustomerView(ListView):
    model = models.Customer
    template_name = "catalog/customerlist.html"

#       ("""<ul>
#   <li>Coffee</li>
#   <li>Tea</li>
#   <li>Milk</li>
# </ul>""")
