from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Duck

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ducks_index(request):
  ducks = Duck.objects.all()
  return render(request, 'ducks/index.html', {'ducks': ducks})

def ducks_detail(request, duck_id):
  duck = Duck.objects.get(id=duck_id)
  return render(request, 'ducks/detail.html', {'duck': duck})

class DuckCreate(CreateView):
  model = Duck
  fields = '__all__'