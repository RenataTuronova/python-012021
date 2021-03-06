from django.urls import path
from . import views

 # ted je treba vytvorit seznam se jmenem urlpatterns
# urlpatterns = [
#   path("", views.MyFirstView.as_view(), name="index")
# ]
# pojmenuju si to "index, protoze je to titulni stranka

urlpatterns = [
  path("", views.CourseView.as_view(), name="index")
]