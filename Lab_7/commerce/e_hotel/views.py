from django.shortcuts import render
from .models import Hotel

def home(request):
    featured = Hotel.objects.order_by('?')[:3]
    return render(request, 'index.html', {'featured': featured})

def search_form(request):
    return render(request, 'search.html')

def get_hotel(request):
    city  = request.GET.get('city')
    price = request.GET.get('price')
    hotels = Hotel.objects.filter(
        city__iexact=city,
        rooms_free__gt=0,
        price__lte=price
    )
    return render(request, 'results.html', {'hotels': hotels})
