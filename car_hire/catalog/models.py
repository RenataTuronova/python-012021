from django.db import models
from django.utils import timezone

class Car(models.Model):
  vehicle_registration_mark = models.CharField(max_length=100)
  vehicle_make_and_model = models.CharField(max_length=100)
  mileage_in_kilometers = models.IntegerField()
  date_of_last_technical_inspection = models.DateField()


  @property
  def days_from_last_inspection(self):
    last_inspection = self.date_of_last_technical_inspection
    now = timezone.localdate()
    difference = now - last_inspection
    return difference.days


class Customer(models.Model):
  CUSTOMER_PROGRAMS = (
    ("g", "Zlatý program"),
    ("p", "Platinový program"),
    ("o", "Běžný program"),
  )

  first_name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  drivers_licence_number = models.CharField(max_length=10)
  date_of_birth = models.DateField()
  customer_program = models.CharField(max_length=1, choices=CUSTOMER_PROGRAMS, null=True)


class Hire(models.Model):
  start_of_the_hire = models.DateTimeField()
  end_of_the_hire = models.DateTimeField()
  hire_price_in_euros = models.IntegerField()
  car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


  @property
  def time_information(self):
    if self.start_of_the_hire < timezone.now():
      if self.end_of_the_hire < timezone.now():
        return f"vypůjčka proběhla v minulosti"
      else:
        return f"vypůjčka aktuálně probíhá"
    else:
      return f"vypůjčka je naplánována v budoucnosti"

