from django.urls import path

from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('django', views.ex01_django, name='django'),
    path('affichage', views.ex01_affichage, name='affichage'),
    path('templates', views.ex01_templates, name='templates')

]
# path('', views.ex00, name='index'),
