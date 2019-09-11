from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cows/', views.cows_index, name='index'),
  path('cows/<int:cow_id>/', views.cows_detail, name='detail'),
  path('cows/create/', views.CowCreate.as_view(), name='cows_create'),
  path('cows/<int:pk>/update/', views.CowUpdate.as_view(), name='cows_update'),
  path('cows/<int:pk>/delete/', views.CowDelete.as_view(), name='cows_delete'), 

]
 