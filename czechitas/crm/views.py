
from django.views import View

from django.views.generic import ListView
from django.http import HttpResponse
from . import models

class Index(View):
  def get(self, request):
    return HttpResponse("Vítej v CRM systému Czechitas!")
#
# class ContactView(ListView):
#   model = models.Contact
#   template_name = "templates/contact_list.html"
