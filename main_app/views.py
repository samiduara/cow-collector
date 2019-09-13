from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cow
from .forms import FeedingForm

class CowCreate(CreateView):
  model = Cow
  fields = ['name', 'breed', 'description', 'age']
  
class CowUpdate(UpdateView):
  model = Cow
  fields = ['breed', 'description', 'age']

class CowDelete(DeleteView):
  model = Cow
  success_url = '/cows/'
# View functions
def add_feeding(request, cow_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cow_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cow_id = cow_id
    new_feeding.save()
  return redirect('detail', cow_id=cow_id)
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cows_index(request):
  cows = Cow.objects.all()
  return render(request, 'cows/index.html', { 'cows': cows })

def cows_detail(request, cow_id):
  cow = Cow.objects.get(id=cow_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cows/detail.html', {
    # include the cow and feeding_form in the context
   'cow': cow, 'feeding_form': feeding_form
    


  })