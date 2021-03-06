from django.shortcuts import render
from django.views import View
 # View je jakoby trida od ktere budeme dedit

from django.views.generic import ListView
from django.http import HttpResponse
from . import models
 # HttpResponse je jakoby odpoved  ... odpoved na nejaky nas pozadavek, odpoved bude web
# http = Hypertext Transfer Protocol - protokol na kterem je zalozeny web

class MyFirstView(View):
  def get(self, request):
    return HttpResponse("Vítej na webu Czechitas!")

# nyni musim pridadit url adresu, pro kterou chci My FirstView

class CourseView(ListView):
  model = models.Course
  template_name = "course/course_list.html"