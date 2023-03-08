from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'frontend/home.html')


def about(request):
    return render(request, 'frontend/about.html')


def portfolio(request):
    return render(request, 'frontend/portfolio.html')
