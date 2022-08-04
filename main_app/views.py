from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Duck:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, cool, description, quack_snack):
    self.name = name
    self.cool = cool
    self.description = description
    self.quack_snack = quack_snack

ducks = [
  Duck('Lolo', False, 'Kinda rude.', 'bread'),
  Duck('Sachi', False, 'Looks like a turtle.', 'blueberry'),
  Duck('Fancy', False, 'Happy fluff ball.', 'McNugget'),
  Duck('Bonk', True, 'Meows loudly.', 'shoe')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello, sir duck</h1>')

def about(request):
  return render(request, 'about.html')

def ducks_index(request):
  return render(request, 'ducks/index.html', {'ducks': ducks})