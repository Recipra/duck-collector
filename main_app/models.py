from django.db import models
from django.urls import reverse

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
  