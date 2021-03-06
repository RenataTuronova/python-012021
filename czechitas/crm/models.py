from django.db import models

class Contact(models.Model):
  first_name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  email = models.CharField(max_length=20)
  date_of_last_contact = models.DateTimeField()



