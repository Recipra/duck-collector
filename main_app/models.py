from django.db import models

# Create your models here.
class Duck(models.Model):
  name = models.CharField(max_length=100)
  cool = models.BooleanField(default=False)
  description = models.TextField(max_length=250)
  quack_snack = models.CharField(max_length=100)

  def __str__(self):
    return self.name