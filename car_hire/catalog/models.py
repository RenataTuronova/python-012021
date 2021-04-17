from django.db import models

class Car(models.Model):
  vehicle_registration_mark = models.CharField(max_length=100)
  vehicle_make_and_model = models.CharField(max_length=100)
  mileage_in_kilometers = models.IntegerField()
  date_of_last_technical_inspection = models.DateField()


class Customer(models.Model):
  first_name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  drivers_licence_number = models.CharField(max_length=10)
  date_of_birth = models.DateField()

class Hire(models.Model):
  start_of_the_hire = models.DateTimeField()
  end_of_the_hire = models.DateTimeField()
  hire_price_in_euros = models.IntegerField()




