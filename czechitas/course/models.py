from django.db import models

# text = CharField
# datum a cas = DateTimeField
# cele cislo = IntegrField
# ruzne dalsi moznosti na webu: https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
# napr. desetinne cislo = DecimalField

class Course(models.Model):
  title = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
