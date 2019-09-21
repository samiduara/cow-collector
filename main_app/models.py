from django.db import models
from django.urls import reverse
# add this import
# from datetime import date

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cow(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cow_id': self.id})
