from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('ducks/', views.ducks_index, name='ducks_index'),
  path('ducks/<int:duck_id>/', views.ducks_detail, name='ducks_detail'),
  path('ducks/create/', views.DuckCreate.as_view(), name='ducks_create'),
  path('ducks/<int:pk>/update/', views.DuckUpdate.as_view(), name='ducks_update'),
  path('ducks/<int:pk>/delete/', views.DuckDelete.as_view(), name='ducks_delete')
]