from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('ducks/', views.ducks_index, name='ducks_index'),
  path('ducks/<int:duck_id>/', views.ducks_detail, name='ducks_detail'),
  path('ducks/create/', views.DuckCreate.as_view(), name='ducks_create'),
  path('ducks/<int:pk>/update/', views.DuckUpdate.as_view(), name='ducks_update'),
  path('ducks/<int:pk>/delete/', views.DuckDelete.as_view(), name='ducks_delete'),
  path('ducks/<int:duck_id>/add_deed/', views.add_deed, name='add_deed'),
  path('ducks/<int:duck_id>/assoc_hat/<int:hat_id>/', views.assoc_hat, name='assoc_hat'),
  path('ducks/<int:duck_id>/remove_hat/<int:hat_id>/', views.remove_hat, name='remove_hat'),
  path('hats/create/', views.HatCreate.as_view(), name='hats_create'),
  path('hats/', views.HatList.as_view(), name='hats_index'),
  path('hats/<int:pk>/', views.HatDetail.as_view(), name='hats_detail'),
  path('hats/<int:pk>/update/', views.HatUpdate.as_view(), name='hats_update'),
  path('hats/<int:pk>/delete/', views.HatDelete.as_view(), name='hats_delete')
]