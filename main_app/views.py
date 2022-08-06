from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Duck, Hat
from .forms import PRForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def ducks_index(request):
  ducks = Duck.objects.all()
  return render(request, 'ducks/index.html', {'ducks': ducks})

def ducks_detail(request, duck_id):
  duck = Duck.objects.get(id=duck_id)
  hats_duck_doesnt_have = Hat.objects.exclude(id__in = duck.hats.all().values_list('id'))
  pr_form = PRForm()
  return render(request, 'ducks/detail.html', {'duck': duck, 'pr_form': pr_form, 'hats': hats_duck_doesnt_have})

def add_deed(request, duck_id):
  form = PRForm(request.POST)
  if form.is_valid():
    new_deed = form.save(commit=False)
    new_deed.duck_id = duck_id
    new_deed.save()
  return redirect('ducks_detail', duck_id=duck_id)

def assoc_hat(request, duck_id, hat_id):
  Duck.objects.get(id=duck_id).hats.add(hat_id)
  return redirect('ducks_detail', duck_id=duck_id)

def remove_hat(request, duck_id, hat_id):
  Duck.objects.get(id=duck_id).hats.remove(hat_id)
  return redirect('ducks_detail', duck_id=duck_id)

class DuckCreate(CreateView):
  model = Duck
  fields = ['name', 'description', 'quack_snack', 'cool']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DuckUpdate(UpdateView):
  model = Duck
  fields = ['description', 'quack_snack', 'cool']

class DuckDelete(DeleteView):
  model = Duck
  success_url = '/ducks/'

class HatCreate(CreateView):
  model = Hat
  fields = '__all__'

class HatList(ListView):
  model = Hat

class HatDetail(DetailView):
  model = Hat

class HatUpdate(UpdateView):
  model = Hat
  fields = ['type', 'color']

class HatDelete(DeleteView):
  model = Hat
  success_url = '/hats/'