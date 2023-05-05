from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('index/', views.index, name='index'),
    path('logout/', views.log_out, name='logout'),
    path('add-item/', views.add_item, name='add-item'),
    path('search/', views.search, name='search'),
]