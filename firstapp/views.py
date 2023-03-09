from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {
        'allProduct': product
    }
    return render(request, 'frontend/home.html', context)


def about(request):
    return render(request, 'frontend/about.html')


def portfolio(request):
    return render(request, 'frontend/portfolio.html')
