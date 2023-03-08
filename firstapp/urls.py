from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('portfolio/', views.portfolio, name='portfolioPage')
]