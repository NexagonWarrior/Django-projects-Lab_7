from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # index.html
    path('search/', views.search_form, name='search'),   # search.html
    path('results/', views.get_hotel, name='results'),   # results.html
]
