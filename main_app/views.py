from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cow

class CowCreate(CreateView):
  model = Cow
  fields = ['name', 'breed', 'description', 'age']

# View functions

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cows_index(request):
  cows = Cow.objects.all()
  return render(request, 'cows/index.html', { 'cows': cows })

def cows_detail(request, cow_id):
  cow = Cow.objects.get(id=cow_id)
  return render(request, 'cows/detail.html', { 'cow': cow })