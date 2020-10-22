from django.urls import path
from core import views as core_views

urlpatterns = [
    
    path('store/', core_views.store, name="store"),
    path('about-me/', core_views.about, name="about"),
    path('', core_views.home, name="home"),
    
]