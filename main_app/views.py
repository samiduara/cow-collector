from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cow
# from .forms import FeedingForm

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
  #feeding_form = FeedingForm()
  return render(request, 'cows/detail.html', {
   'cow': cow, #'feeding_form': feeding_form
    })

# def add_feeding(request, cow_id):
#   form = FeedingForm(request.POST)
#   if form.is_valid():
#     new_feeding = form.save(commit=False)
#     new_feeding.cow_id = cow_id
#     new_feeding.save()
#   return redirect('detail', cow_id=cow_id)    