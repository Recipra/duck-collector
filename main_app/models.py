from django.db import models
from django.urls import reverse
from datetime import date


DEEDS = (
  ('A', 'Atrocity'),
  ('B', 'Bad'),
  ('G', 'Good'),
  ('M', 'Miracle')
)

# Create your models here.
class Duck(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quack_snack = models.CharField(max_length=100)
  cool = models.BooleanField(default=False)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('ducks_detail', kwargs={'duck_id': self.id})

  def deeds_for_today(self):
    return self.public_relations_set.filter(date=date.today()).count() >= 3

class Public_Relations(models.Model):
  date = models.DateField('Deed date')
  deed = models.CharField(max_length=1, choices=DEEDS, default=DEEDS[2][0]
  )
  duck = models.ForeignKey(Duck, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_deed_display()} on {self.date}'

  class Meta:
    ordering = ['date']