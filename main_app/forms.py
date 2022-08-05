from django.forms import ModelForm
from .models import Public_Relations

class PRForm(ModelForm):
  class Meta:
    model = Public_Relations
    fields = ['date', 'deed']